import pg from 'pg';
import sqlite3 from 'sqlite3';
import path from 'path';
import fs from 'fs';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

dotenv.config();

const __dirname = path.dirname(fileURLToPath(import.meta.url));

let usePostgres = true;
let pgPool = null;
let sqliteDb = null;

// Initialize Postgres connection pool
pgPool = new pg.Pool({
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '5432'),
  user: process.env.DB_USER || 'n8n',
  password: process.env.DB_PASSWORD || 'n8npassword',
  database: process.env.DB_DATABASE || 'dental_clinic',
  connectionTimeoutMillis: 5000, // Timeout fast if postgres is locked up
  onConnect: async (client) => {
    await client.query('SET search_path TO learning_recall, public');
  }
});

// Unified Query Handler
export const query = async (text, params) => {
  if (usePostgres) {
    try {
      return await pgPool.query(text, params);
    } catch (err) {
      // If postgres connection fails or too many clients, fallback to sqlite
      const isConnectionError = 
        err.code === 'ECONNREFUSED' || 
        err.message.includes('ECONNREFUSED') || 
        err.message.includes('too many clients') || 
        err.message.includes('timeout') ||
        (err.errors && err.errors.some(e => e.code === 'ECONNREFUSED' || e.message.includes('ECONNREFUSED')));
        
      if (isConnectionError) {
        console.warn('⚠️ PostgreSQL connection failed/busy. Falling back to local SQLite database...', err.message || err.code);
        usePostgres = false;
        await initSqlite();
        return await querySqlite(text, params);
      }
      throw err;
    }
  } else {
    return await querySqlite(text, params);
  }
};

// SQLite database initialization
const initSqlite = () => {
  return new Promise((resolve, reject) => {
    if (sqliteDb) return resolve();
    
    const dbPath = path.join(__dirname, 'database.sqlite');
    sqliteDb = new sqlite3.Database(dbPath, (err) => {
      if (err) {
        console.error('Failed to open SQLite database:', err);
        return reject(err);
      }
      console.log('📦 Local SQLite database initialized at:', dbPath);
      resolve();
    });
  });
};

// Convert PostgreSQL query format ($1, $2) to SQLite (? or :param)
const pgToSqliteQuery = (text) => {
  // Replace $1, $2... with ?
  return text.replace(/\$\d+/g, '?');
};

// Execute query on SQLite
const querySqlite = (text, params = []) => {
  return new Promise((resolve, reject) => {
    const sqliteText = pgToSqliteQuery(text);
    
    // Check if query is a SELECT
    const isSelect = sqliteText.trim().toUpperCase().startsWith('SELECT');
    
    if (isSelect) {
      sqliteDb.all(sqliteText, params, (err, rows) => {
        if (err) return reject(err);
        resolve({ rows });
      });
    } else {
      sqliteDb.run(sqliteText, params, function (err) {
        if (err) return reject(err);
        resolve({ 
          rows: [], 
          rowCount: this.changes,
          lastID: this.lastID 
        });
      });
    }
  });
};

// Database Schema Initialization
export const initDatabase = async () => {
  console.log('🔄 Checking database connection...');
  try {
    // Test postgres connection
    const client = await pgPool.connect();
    console.log('✅ Connected to PostgreSQL on VPS successfully!');
    client.release();
    
    // Create schema and tables in Postgres
    await pgPool.query(`CREATE SCHEMA IF NOT EXISTS learning_recall;`);
    
    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE,
        color_code VARCHAR(20) NOT NULL
      );
    `);

    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.chapters (
        id SERIAL PRIMARY KEY,
        subject_id INT REFERENCES learning_recall.subjects(id) ON DELETE CASCADE,
        name VARCHAR(250) NOT NULL,
        parent_chapter VARCHAR(250),
        sub_chapter VARCHAR(250),
        title_vn VARCHAR(250),
        title_en VARCHAR(250),
        url VARCHAR(500),
        original_score INT DEFAULT 0,
        current_score INT DEFAULT 0,
        box_number INT DEFAULT 1,
        interval_days INT DEFAULT 0,
        next_review_date DATE DEFAULT CURRENT_DATE,
        sort_order INT DEFAULT 0,
        theory TEXT
      );
    `);

    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.questions (
        id SERIAL PRIMARY KEY,
        chapter_id INT REFERENCES learning_recall.chapters(id) ON DELETE CASCADE,
        question_text TEXT NOT NULL,
        question_type VARCHAR(50) DEFAULT 'multiple_choice',
        options TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        explanation TEXT,
        hint TEXT,
        difficulty VARCHAR(50),
        cognitive_level VARCHAR(50),
        grade_level INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.topic_practice_logs (
        id SERIAL PRIMARY KEY,
        chapter_id INT REFERENCES learning_recall.chapters(id) ON DELETE CASCADE,
        score INT NOT NULL,
        total_questions INT NOT NULL,
        correct_answers INT NOT NULL,
        practiced_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.flashcards (
        id SERIAL PRIMARY KEY,
        chapter_id INT REFERENCES learning_recall.chapters(id) ON DELETE CASCADE,
        sub_topic_id INT,
        front_content TEXT NOT NULL,
        back_content TEXT NOT NULL,
        hint TEXT,
        image_url TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.spaced_repetition_states (
        id SERIAL PRIMARY KEY,
        flashcard_id INT REFERENCES learning_recall.flashcards(id) ON DELETE CASCADE UNIQUE,
        box_number INT DEFAULT 1,
        easiness_factor REAL DEFAULT 2.5,
        repetition_count INT DEFAULT 0,
        interval_days INT DEFAULT 0,
        next_review_date DATE DEFAULT CURRENT_DATE,
        last_reviewed_at TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.study_logs (
        id SERIAL PRIMARY KEY,
        flashcard_id INT REFERENCES learning_recall.flashcards(id) ON DELETE CASCADE,
        score INT NOT NULL,
        review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await pgPool.query(`
      CREATE TABLE IF NOT EXISTS learning_recall.achievements (
        id SERIAL PRIMARY KEY,
        streak_days INT DEFAULT 0,
        total_score INT DEFAULT 0,
        last_active_date DATE,
        badges_unlocked TEXT[]
      );
    `);
    
    console.log('🚀 PostgreSQL tables verified/created successfully.');
    
    // Check if subjects table is empty, and seed it
    const subjectsCheck = await pgPool.query('SELECT COUNT(*) FROM learning_recall.subjects');
    if (parseInt(subjectsCheck.rows[0].count) === 0) {
      await seedDefaultData(pgPool.query.bind(pgPool));
    }

    // Check if flashcards table is empty, and seed it
    const cardsCheck = await pgPool.query('SELECT COUNT(*) FROM learning_recall.flashcards');
    if (parseInt(cardsCheck.rows[0].count) === 0) {
      await seedDefaultFlashcards(pgPool.query.bind(pgPool), true);
    }

  } catch (err) {
    console.warn('⚠️ PostgreSQL initialization failed, switching to local SQLite database...', err.message);
    usePostgres = false;
    await initSqlite();
    
    // Create tables in SQLite
    await querySqlite(`
      CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        color_code TEXT NOT NULL
      );
    `);

    await querySqlite(`
      CREATE TABLE IF NOT EXISTS chapters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER REFERENCES subjects(id) ON DELETE CASCADE,
        name TEXT NOT NULL,
        parent_chapter TEXT,
        sub_chapter TEXT,
        title_vn TEXT,
        title_en TEXT,
        url TEXT,
        original_score INTEGER DEFAULT 0,
        current_score INTEGER DEFAULT 0,
        box_number INTEGER DEFAULT 1,
        interval_days INTEGER DEFAULT 0,
        next_review_date TEXT DEFAULT CURRENT_DATE,
        sort_order INTEGER DEFAULT 0,
        theory TEXT
      );
    `);

    await querySqlite(`
      CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id INTEGER REFERENCES chapters(id) ON DELETE CASCADE,
        question_text TEXT NOT NULL,
        question_type TEXT DEFAULT 'multiple_choice',
        options TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        explanation TEXT,
        hint TEXT,
        difficulty TEXT,
        cognitive_level TEXT,
        grade_level INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await querySqlite(`
      CREATE TABLE IF NOT EXISTS topic_practice_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id INTEGER REFERENCES chapters(id) ON DELETE CASCADE,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        correct_answers INTEGER NOT NULL,
        practiced_at DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await querySqlite(`
      CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id INTEGER REFERENCES chapters(id) ON DELETE CASCADE,
        sub_topic_id INTEGER,
        front_content TEXT NOT NULL,
        back_content TEXT NOT NULL,
        hint TEXT,
        image_url TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await querySqlite(`
      CREATE TABLE IF NOT EXISTS spaced_repetition_states (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flashcard_id INTEGER REFERENCES flashcards(id) ON DELETE CASCADE UNIQUE,
        box_number INTEGER DEFAULT 1,
        easiness_factor REAL DEFAULT 2.5,
        repetition_count INTEGER DEFAULT 0,
        interval_days INTEGER DEFAULT 0,
        next_review_date TEXT DEFAULT CURRENT_DATE,
        last_reviewed_at DATETIME,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await querySqlite(`
      CREATE TABLE IF NOT EXISTS study_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flashcard_id INTEGER REFERENCES flashcards(id) ON DELETE CASCADE,
        score INTEGER NOT NULL,
        review_date DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await querySqlite(`
      CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        streak_days INTEGER DEFAULT 0,
        total_score INTEGER DEFAULT 0,
        last_active_date TEXT,
        badges_unlocked TEXT -- SQLite stores arrays as JSON string
      );
    `);

    console.log('🚀 SQLite tables verified/created successfully.');
    
    // Seed SQLite default subjects if empty
    const subjectsCheck = await querySqlite('SELECT COUNT(*) as count FROM subjects');
    if (subjectsCheck.rows[0].count === 0) {
      await seedDefaultData(querySqlite);
    }

    // Seed SQLite default flashcards if empty
    const cardsCheck = await querySqlite('SELECT COUNT(*) as count FROM flashcards');
    if (cardsCheck.rows[0].count === 0) {
      await seedDefaultFlashcards(querySqlite, false);
    }
  }
};

// Seed default subjects
const seedDefaultData = async (queryFunc) => {
  console.log('🌱 Seeding default subjects...');
  try {
    await queryFunc(`DELETE FROM subjects`);
    await queryFunc(`INSERT INTO subjects (id, name, color_code) VALUES 
      (1, 'Toán', 'hsl(210, 100%, 50%)'), 
      (2, 'Tiếng Việt', 'hsl(14, 100%, 53%)'), 
      (3, 'Tiếng Anh', 'hsl(145, 63%, 42%)')
    `);
    console.log('✅ Database seeding finished successfully.');
  } catch (err) {
    console.error('Failed to seed default database:', err);
  }
};

const subTopicKeywords = {
  // Toán
  101: { subject: 1, term: '%phân số%' },
  102: { subject: 1, term: '%số thập phân%' },
  103: { subject: 1, term: '%dãy số%' },
  104: { subject: 1, term: '%Tính nhanh%' },
  201: { subject: 1, term: '%tỉ số%' },
  202: { subject: 1, term: '%tỉ số phần trăm%' },
  203: { subject: 1, term: '%lãi%' },
  204: { subject: 1, term: '%hạt tươi%' },
  301: { subject: 1, term: '%tuổi%' },
  302: { subject: 1, term: '%trồng cây%' },
  303: { subject: 1, term: '%vòi%' },
  304: { subject: 1, term: '%giả thiết tạm%' },
  401: { subject: 1, term: '%vận tốc%' },
  402: { subject: 1, term: '%ngược chiều%' },
  403: { subject: 1, term: '%dòng nước%' },
  404: { subject: 1, term: '%tàu hỏa%' },
  501: { subject: 1, term: '%thang%' },
  502: { subject: 1, term: '%lập phương%' },
  601: { subject: 1, term: '%Dirichlet%' },
  602: { subject: 1, term: '%Dirichlet%' },
  603: { subject: 1, term: '%tổ hợp%' },
  // Tiếng Việt
  701: { subject: 2, term: '%láy%' },
  702: { subject: 2, term: '%nghĩa của từ%' },
  703: { subject: 2, term: '%tục ngữ%' },
  801: { subject: 2, term: '%từ loại%' },
  802: { subject: 2, term: '%chủ ngữ%' },
  803: { subject: 2, term: '%câu ghép%' },
  901: { subject: 2, term: '%nhân hóa%' },
  902: { subject: 2, term: '%điệp ngữ%' },
  903: { subject: 2, term: '%ẩn dụ%' },
  1001: { subject: 2, term: '%đọc hiểu%' },
  1002: { subject: 2, term: '%cảm thụ%' },
  1101: { subject: 2, term: '%tả cảnh%' },
  1102: { subject: 2, term: '%tả người%' },
  // Tiếng Anh
  1201: { subject: 3, term: '%ed%' },
  1202: { subject: 3, term: '%trọng âm%' },
  1301: { subject: 3, term: '%school%' },
  1302: { subject: 3, term: '%job%' },
  1303: { subject: 3, term: '%food%' },
  1401: { subject: 3, term: '%present%' },
  1402: { subject: 3, term: '%past%' },
  1403: { subject: 3, term: '%perfect%' },
  1404: { subject: 3, term: '%future%' },
  1501: { subject: 3, term: '%comparison%' },
  1502: { subject: 3, term: '%conditional%' },
  1503: { subject: 3, term: '%passive%' },
  1504: { subject: 3, term: '%modal%' },
  1601: { subject: 3, term: '%cloze%' },
  1602: { subject: 3, term: '%reading%' },
  1701: { subject: 3, term: '%write%' },
  1702: { subject: 3, term: '%reorder%' },
};

// Seed default flashcards
export const seedDefaultFlashcards = async (queryFunc, isPostgres) => {
  console.log('🌱 Seeding default flashcards...');
  const cards = [
    { chapter_id: 1, sub_topic_id: 101, front_content: 'Tính nhanh: 3/4 + 1/5 + 1/4 + 4/5', back_content: 'Gộp các phân số cùng mẫu:\n(3/4 + 1/4) + (1/5 + 4/5) = 1 + 1 = 2.', hint: 'Nhóm các phân số có mẫu số giống nhau.' },
    { chapter_id: 1, sub_topic_id: 102, front_content: 'Tìm X: X x 1.2 + X x 1.8 = 15', back_content: 'Áp dụng tính chất phân phối:\nX x (1.2 + 1.8) = 15\nX x 3 = 15\nX = 15 / 3 = 5.', hint: 'Đặt X ra làm nhân tử chung.' },
    { chapter_id: 1, sub_topic_id: 103, front_content: 'Tính tổng dãy số: 1 + 3 + 5 + ... + 19', back_content: 'Số số hạng: (19 - 1) / 2 + 1 = 10 số.\nTổng = (19 + 1) x 10 / 2 = 100.', hint: 'Áp dụng công thức tính tổng dãy số cách đều.' },
    { chapter_id: 1, sub_topic_id: 104, front_content: 'Tính nhanh: 12.5 x 8.8', back_content: 'Tách 8.8 = 8 x 1.1\n12.5 x 8 x 1.1 = 100 x 1.1 = 110.', hint: 'Số 12.5 nhân với 8 sẽ ra số tròn trăm.' },
    { chapter_id: 2, sub_topic_id: 201, front_content: 'Tổng của hai số là 80, tỉ số của chúng là 3/5. Tìm hai số đó.', back_content: 'Tổng số phần bằng nhau: 3 + 5 = 8 phần.\nSố bé: 80 / 8 x 3 = 30.\nSố lớn: 80 - 30 = 50.', hint: 'Tìm tổng số phần bằng nhau trước.' },
    { chapter_id: 2, sub_topic_id: 202, front_content: 'Một chiếc áo giá 200.000đ được giảm giá 15%. Hỏi giá sau giảm là bao nhiêu?', back_content: 'Số tiền được giảm: 200.000 x 15% = 30.000đ.\nGiá sau giảm: 200.000 - 30.000 = 170.000đ.', hint: 'Tính số tiền giảm trước hoặc tính phần trăm còn lại.' },
    { chapter_id: 2, sub_topic_id: 203, front_content: 'Mua 100.000đ bán 125.000đ. Hỏi lãi bao nhiêu phần trăm so với vốn?', back_content: 'Số tiền lãi: 125.000 - 100.000 = 25.000đ.\nTỉ lệ lãi so với vốn: 25.000 / 100.000 x 100% = 25%.', hint: 'Lấy tiền lãi chia cho tiền vốn.' },
    { chapter_id: 2, sub_topic_id: 204, front_content: 'Tỉ lệ nước trong hạt tươi là 20%, hạt khô là 10%. Hỏi 180kg hạt tươi thu được bao nhiêu kg hạt khô?', back_content: 'Lượng chất khô trong hạt tươi là: 180 x (100% - 20%) = 144kg.\nKhối lượng hạt khô thu được: 144 / (100% - 10%) = 160kg.', hint: 'Khối lượng chất khô không thay đổi trước và sau khi phơi.' },
    { chapter_id: 3, sub_topic_id: 301, front_content: 'Hiện nay mẹ 30 tuổi, con 6 tuổi. Hỏi sau bao nhiêu năm nữa tuổi mẹ gấp 3 lần tuổi con?', back_content: 'Hiệu số tuổi luôn không đổi: 30 - 6 = 24 tuổi.\nKhi tuổi mẹ gấp 3 lần tuổi con, hiệu số phần là: 3 - 1 = 2 phần.\nTuổi con lúc đó: 24 / 2 = 12 tuổi.\nSố năm cần tìm: 12 - 6 = 6 năm.', hint: 'Nhớ rằng hiệu số tuổi của hai mẹ con không thay đổi theo thời gian.' },
    { chapter_id: 3, sub_topic_id: 302, front_content: 'Một đường thẳng dài 100m, trồng cây hai đầu đường, khoảng cách giữa 2 cây là 5m. Tính số cây trồng được.', back_content: 'Số cây = (Chiều dài / Khoảng cách) + 1\nSố cây = (100 / 5) + 1 = 21 cây.', hint: 'Trồng ở hai đầu đường thì số cây nhiều hơn số khoảng cách là 1.' },
    { chapter_id: 3, sub_topic_id: 303, front_content: 'Vòi A chảy đầy bể mất 4 giờ, vòi B mất 6 giờ. Hỏi cả hai vòi cùng chảy mất bao lâu?', back_content: '1 giờ vòi A chảy: 1/4 bể. 1 giờ vòi B chảy: 1/6 bể.\n1 giờ cả hai chảy: 1/4 + 1/6 = 5/12 bể.\nThời gian đầy bể: 1 / (5/12) = 2.4 giờ (2 giờ 24 phút).', hint: 'Tính lượng nước mỗi vòi chảy được trong 1 giờ.' },
    { chapter_id: 3, sub_topic_id: 304, front_content: 'Vừa gà vừa chó có 36 con, 100 chân. Hỏi có bao nhiêu con gà, bao nhiêu con chó?', back_content: 'Giả sử tất cả 36 con đều là gà. Số chân là: 36 x 2 = 72 chân. Số chân thiếu so với thực tế: 100 - 72 = 28 chân. Số con chó: 28 / (4 - 2) = 14 con. Số con gà: 36 - 14 = 22 con.', hint: 'Áp dụng phương pháp giả thiết tạm: giả sử tất cả đều là gà.' },
    { chapter_id: 4, sub_topic_id: 401, front_content: 'Xe máy đi từ A lúc 7 giờ và đến B lúc 9h30 với vận tốc 40km/h. Tính quãng đường AB.', back_content: 'Thời gian đi: 9h30 - 7h = 2.5 giờ.\nQuãng đường AB: 40 x 2.5 = 100 km.', hint: 's = v x t. Đổi 2 giờ 30 phút thành 2.5 giờ.' },
    { chapter_id: 4, sub_topic_id: 402, front_content: 'Hai xe cùng xuất phát lúc 7 giờ từ A và B cách nhau 120km, đi ngược chiều nhau. Xe 1 đi từ A với v = 35km/h, xe 2 đi từ B với v = 25km/h. Hỏi hai xe gặp nhau lúc mấy giờ?', back_content: 'Tổng vận tốc hai xe: 35 + 25 = 60 km/h. Thời gian đi để gặp nhau: 120 / 60 = 2 giờ. Thời điểm gặp nhau: 7 + 2 = 9 giờ.', hint: 'Thời gian gặp nhau = Khoảng cách / Tổng vận tốc.' },
    { chapter_id: 4, sub_topic_id: 403, front_content: 'Cano đi xuôi dòng nước có vận tốc 25km/h, vận tốc dòng nước là 3km/h. Tính vận tốc thực của cano.', back_content: 'Vận tốc thực = Vận tốc xuôi dòng - Vận tốc dòng nước\nVận tốc thực = 25 - 3 = 22 km/h.', hint: 'Vận tốc xuôi dòng bằng vận tốc thực cộng vận tốc dòng nước.' },
    { chapter_id: 4, sub_topic_id: 404, front_content: 'Một tàu hỏa dài 150m đi qua một cây cầu dài 450m với vận tốc 36 km/h. Hỏi tàu hỏa đi qua cầu mất bao nhiêu giây?', back_content: 'Đổi 36 km/h = 10 m/s. Quãng đường tàu hỏa đi được để qua hết cầu: 150 + 450 = 600m. Thời gian tàu hỏa đi qua cầu: 600 / 10 = 60 giây (1 phút).', hint: 'Quãng đường đi được bằng chiều dài tàu cộng với chiều dài cầu.' },
    { chapter_id: 5, sub_topic_id: 501, front_content: 'Tính diện tích hình thang có đáy lớn 12cm, đáy bé 8cm và chiều cao 6cm.', back_content: 'S = (12 + 8) x 6 / 2 = 60 cm².', hint: 'S = (đáy lớn + đáy bé) x chiều cao / 2' },
    { chapter_id: 5, sub_topic_id: 502, front_content: 'Thể tích của hình lập phương có cạnh 4cm là bao nhiêu?', back_content: 'V = 4 x 4 x 4 = 64 cm³.', hint: 'V = cạnh x cạnh x cạnh' },
    { chapter_id: 6, sub_topic_id: 601, front_content: 'Có 5 quả bóng đỏ và 4 quả bóng xanh. Cần bốc ít nhất bao nhiêu quả để chắc chắn có 2 quả cùng màu?', back_content: 'Có 2 màu (đỏ và xanh).\nTheo Dirichlet, bốc 3 quả sẽ chắc chắn có ít nhất 2 quả cùng màu.', hint: 'Áp dụng nguyên lý Dirichlet.' },
    { chapter_id: 6, sub_topic_id: 602, front_content: 'Trong một lớp học có 37 học sinh. Chứng minh rằng có ít nhất 4 học sinh có cùng tháng sinh.', back_content: 'Một năm có 12 tháng sinh. Ta chia 37 học sinh cho 12 tháng: 37 = 3 x 12 + 1. Theo nguyên lý Dirichlet, phải có ít nhất 3 + 1 = 4 học sinh có cùng tháng sinh.', hint: 'Áp dụng nguyên lý Dirichlet: Lấy số học sinh chia cho số tháng sinh.' },
    { chapter_id: 6, sub_topic_id: 603, front_content: 'Từ các chữ số 1, 2, 3 có thể lập được bao nhiêu số tự nhiên có 3 chữ số khác nhau?', back_content: 'Chữ số hàng trăm có 3 cách chọn, chữ số hàng chục có 2 cách chọn (khác chữ số hàng trăm), chữ số hàng đơn vị có 1 cách chọn. Số các số lập được: 3 x 2 x 1 = 6 số.', hint: 'Dùng quy tắc nhân chọn số từng hàng từ trăm đến đơn vị.' },
    { chapter_id: 7, sub_topic_id: 701, front_content: 'Từ "xinh xắn" là từ ghép hay từ láy?', back_content: 'Là từ láy bộ phận vần (lặp lại âm đầu "x" và vần gần giống nhau).', hint: 'Xem hai tiếng có quan hệ âm thanh hay không.' },
    { chapter_id: 7, sub_topic_id: 702, front_content: 'Xác định nghĩa của từ "chạy" trong câu: "Nhà này chạy ăn từng bữa."', back_content: 'Nghĩa chuyển: Hoạt động lo toan, xoay xở khẩn trương để có được thứ cần thiết.', hint: 'Từ "chạy" ở đây không chỉ hoạt động của chân.' },
    { chapter_id: 7, sub_topic_id: 703, front_content: 'Giải thích ý nghĩa câu tục ngữ: "Ăn quả nhớ kẻ trồng cây".', back_content: 'Khuyên răn chúng ta phải có lòng biết ơn đối với những người đã có công lao tạo dựng nên thành quả mà chúng ta đang được hưởng thụ ngày hôm nay.', hint: 'Qủa là thành quả được hưởng, kẻ trồng cây là người tạo ra nó.' },
    { chapter_id: 8, sub_topic_id: 801, front_content: 'Trong câu: "Em rất thích học Tiếng Việt.", từ "thích" thuộc từ loại nào?', back_content: 'Thuộc từ loại: Động từ (chỉ trạng thái tâm lý).', hint: 'Từ chỉ cảm xúc, mong muốn là động từ chỉ trạng thái.' },
    { chapter_id: 8, sub_topic_id: 802, front_content: 'Tìm chủ ngữ trong câu: "Dưới bóng tre xanh, ta gìn giữ một nền văn hóa lâu đời."', back_content: 'Chủ ngữ là "ta".\n"Dưới bóng tre xanh" là trạng ngữ chỉ nơi chốn.', hint: 'Chủ ngữ thực hiện hành động "gìn giữ".' },
    { chapter_id: 8, sub_topic_id: 803, front_content: 'Xác định cặp quan hệ từ và quan hệ ý nghĩa trong câu ghép: "Mặc dù trời mưa to nhưng các em vẫn đến trường đúng giờ."', back_content: 'Cặp quan hệ từ: "Mặc dù ... nhưng ...". Quan hệ ý nghĩa: Quan hệ tương phản.', hint: 'Chú ý từ "Mặc dù" ở vế 1 và "nhưng" ở vế 2.' },
    { chapter_id: 9, sub_topic_id: 901, front_content: 'Xác định biện pháp tu từ trong câu: "Trẻ em như búp trên cành."', back_content: 'Biện pháp: So sánh (so sánh trẻ em với búp trên cành qua từ "như").', hint: 'Có từ so sánh "như".' },
    { chapter_id: 9, sub_topic_id: 902, front_content: 'Chỉ ra và nêu tác dụng của biện pháp điệp ngữ trong câu thơ: "Tre giữ làng, giữ nước, giữ mái nhà tranh, giữ đồng lúa chín."', back_content: 'Điệp từ: "giữ". Tác dụng: Nhấn mạnh vai trò bảo vệ, chở che kiên cường, bền bỉ của cây tre đối với cuộc sống của người dân Việt Nam.', hint: 'Từ nào được lặp lại nhiều lần liên tiếp?' },
    { chapter_id: 9, sub_topic_id: 903, front_content: 'Xác định biện pháp tu từ trong câu: "Thuyền về có nhớ bến chăng / Bến thì một dạ khăng khăng đợi thuyền."', back_content: 'Biện pháp tu từ: Nhân hóa ("bến" biết mong nhớ, đợi chờ) và ẩn dụ ("thuyền" chỉ người đi xa, "bến" chỉ người ở lại chung thủy).', hint: 'Thuyền và bến được gán cho những cảm xúc nào của con người?' },
    { chapter_id: 10, sub_topic_id: 1001, front_content: 'Đọc câu thơ: "Quê hương là chùm khế ngọt / Cho con trèo hái mỗi ngày". Tác giả so sánh Quê hương với gì và có ý nghĩa gì?', back_content: 'Tác giả so sánh Quê hương với "chùm khế ngọt", gợi tả sự gần gũi, ngọt ngào, giản dị của gia đình và đất nước gắn liền với tuổi thơ.', hint: 'Gợi tả cảm giác thân thuộc của tuổi thơ.' },
    { chapter_id: 10, sub_topic_id: 1002, front_content: 'Trong câu: "Ôi Tổ quốc, ta yêu như xương thịt / Như mẹ cha ta, như vợ như chồng", tác giả dùng biện pháp so sánh nhằm mục đích gì?', back_content: 'Tác giả dùng phép so sánh liên tiếp để biểu lộ tình yêu Tổ quốc thiêng liêng, gắn bó sâu sắc, máu thịt như những tình cảm ruột thịt, gần gũi nhất.', hint: 'So sánh Tổ quốc với xương thịt, mẹ cha, vợ chồng.' },
    { chapter_id: 11, sub_topic_id: 1101, front_content: 'Nêu các phần chính của dàn ý bài văn tả cảnh.', back_content: '1. Mở bài: Giới thiệu cảnh định tả.\n2. Thân bài: Tả bao quát rồi tả chi tiết theo trình tự thời gian/không gian.\n3. Kết bài: Nêu cảm nghĩ về cảnh vật.', hint: 'Văn miêu tả luôn có bố cục 3 phần.' },
    { chapter_id: 11, sub_topic_id: 1102, front_content: 'Khi tả ngoại hình một người, em nên lựa chọn những chi tiết như thế nào?', back_content: 'Nên chọn lọc những chi tiết tiêu biểu, đặc sắc nhất của người đó (như ánh mắt, nụ cười, mái tóc, bàn tay...) để vừa gợi tả ngoại hình vừa làm nổi bật tính cách.', hint: 'Tránh tả tràn lan mà hãy chọn những nét riêng biệt.' },
    { chapter_id: 12, sub_topic_id: 1201, front_content: 'Từ "watched" có phát âm đuôi -ed là gì?', back_content: '/t/ vì kết thúc bằng âm vô thanh /tʃ/.', hint: 'Phát âm là /t/ sau các âm vô thanh như ch, sh, p, k, f, s.' },
    { chapter_id: 12, sub_topic_id: 1202, front_content: 'Trọng âm chính của từ "beautiful" rơi vào âm tiết thứ mấy?', back_content: 'Âm tiết thứ nhất (BEAU-ti-ful).', hint: 'Từ 3 âm tiết có hậu tố -ful thường nhấn âm 1.' },
    { chapter_id: 13, sub_topic_id: 1301, front_content: 'Dịch sang tiếng Anh: "môn Lịch sử", "môn Địa lý", "môn Khoa học".', back_content: 'History, Geography, Science.', hint: 'Subject names.' },
    { chapter_id: 13, sub_topic_id: 1302, front_content: 'Dịch sang tiếng Anh các từ chỉ nghề nghiệp sau: "bác sĩ thú y", "kiến trúc sư", "kế toán".', back_content: '- Bác sĩ thú y: veterinarian (hoặc vet)\n- Kiến trúc sư: architect\n- Kế toán: accountant', hint: 'Kiến trúc sư bắt đầu bằng chữ "a".' },
    { chapter_id: 13, sub_topic_id: 1303, front_content: 'Dịch sang tiếng Anh các từ sau: "sốt", "đau họng", "chế độ ăn uống cân đối".', back_content: '- Sốt: fever\n- Đau họng: sore throat\n- Chế độ ăn uống cân đối: balanced diet', hint: 'Sore throat là đau họng.' },
    { chapter_id: 14, sub_topic_id: 1401, front_content: 'Chia động từ: "He (write) a book since 2024."', back_content: 'has been writing (hoặc has written) - Hiện tại hoàn thành.', hint: 'Có từ "since".' },
    { chapter_id: 14, sub_topic_id: 1402, front_content: 'Chia động từ trong ngoặc: "When I arrived home, my family (have) dinner."', back_content: 'was having (hoặc were having)\nGiải thích: Diễn tả một hành động đang diễn ra tại thời điểm đó trong quá khứ.', hint: 'Hành động đang diễn ra tại một thời điểm xác định.' },
    { chapter_id: 14, sub_topic_id: 1403, front_content: 'Chọn giới từ đúng: "I have lived in Hanoi ... 5 years." (for / since)', back_content: 'for\nGiải thích: Dùng "for" trước một khoảng thời gian (5 years). Dùng "since" trước mốc thời gian.', hint: '"5 years" là một khoảng thời gian.' },
    { chapter_id: 14, sub_topic_id: 1404, front_content: 'Chia động từ trong ngoặc: "We (visit) our grandparents this weekend. We already bought the bus tickets."', back_content: 'are going to visit (hoặc are visiting)\nGiải thích: Hành động có kế hoạch, dự định rõ ràng từ trước và có bằng chứng (bought tickets).', hint: 'Sử dụng cấu trúc tương lai gần (be going to).' },
    { chapter_id: 15, sub_topic_id: 1501, front_content: 'Viết dạng so sánh hơn của "bad" và "good".', back_content: 'bad -> worse\ngood -> better.', hint: 'Dạng so sánh bất quy tắc.' },
    { chapter_id: 15, sub_topic_id: 1502, front_content: 'Chuyển sang bị động: "She cleans the room every day."', back_content: 'The room is cleaned by her every day.', hint: 'Hiện tại đơn chuyển sang bị động dùng am/is/are + V3.' },
    { chapter_id: 15, sub_topic_id: 1503, front_content: 'Chuyển sang câu bị động: "The fire destroyed the building yesterday."', back_content: 'The building was destroyed by the fire yesterday.', hint: 'Quá khứ đơn bị động dùng was/were + V3.' },
    { chapter_id: 15, sub_topic_id: 1504, front_content: 'Điền từ khuyết: "You ... touch that wire. It is very dangerous." (mustn\'t / needn\'t / don\'t have to)', back_content: 'mustn\'t\nGiải thích: Chỉ sự cấm đoán, không được phép làm vì có nguy hiểm.', hint: 'Mang tính chất cấm vì nguy hiểm đến tính mạng.' },
    { chapter_id: 16, sub_topic_id: 1601, front_content: 'Chọn từ điền vào chỗ trống: "She is interested ... reading books." (on/in/at)', back_content: 'Đáp án: "in" (cấu trúc be interested in).', hint: 'Giới từ đi với interested.' },
    { chapter_id: 16, sub_topic_id: 1602, front_content: 'Đọc câu sau và điền từ thích hợp vào câu trả lời: "Although English is widely spoken, Chinese has the most native speakers." -> Question: Which language has more native speakers, English or Chinese? -> Answer: ...', back_content: 'Chinese (Tiếng Trung Quốc).', hint: 'Xem thông tin vế sau của câu.' },
    { chapter_id: 17, sub_topic_id: 1701, front_content: 'Viết lại câu: "Although it rained heavily, they went to school." -> "In spite of..."', back_content: 'In spite of the heavy rain, they went to school.', hint: 'In spite of + danh từ/cụm danh từ.' },
    { chapter_id: 17, sub_topic_id: 1702, front_content: 'Sắp xếp các từ sau thành câu đúng: "she / because / tired / went / bed / early / was / to / she"', back_content: 'She went to bed early because she was tired.', hint: 'Mệnh đề kết quả trước, "because" nối mệnh đề nguyên nhân.' }
  ];

  try {
    for (const c of cards) {
      // Dynamically lookup the correct chapter_id in the database matching subTopicKeywords
      const mapItem = subTopicKeywords[c.sub_topic_id];
      let chapterId = null;
      if (mapItem) {
        const queryTerm = mapItem.term.toLowerCase();
        const dbRes = await queryFunc(
          'SELECT id FROM chapters WHERE subject_id = $1 AND (LOWER(name) LIKE $2 OR LOWER(parent_chapter) LIKE $2) LIMIT 1',
          [mapItem.subject, queryTerm]
        );
        if (dbRes && dbRes.rows && dbRes.rows.length > 0) {
          chapterId = dbRes.rows[0].id;
        }
      }
      if (!chapterId) {
        // Find any chapter for this subject as fallback
        const dbRes = await queryFunc('SELECT id FROM chapters WHERE subject_id = $1 LIMIT 1', [mapItem ? mapItem.subject : 1]);
        if (dbRes && dbRes.rows && dbRes.rows.length > 0) {
          chapterId = dbRes.rows[0].id;
        } else {
          chapterId = mapItem ? (mapItem.subject === 1 ? 1 : (mapItem.subject === 2 ? 98 : 129)) : 1;
        }
      }

      if (isPostgres) {
        const insertRes = await queryFunc(
          'INSERT INTO learning_recall.flashcards (chapter_id, sub_topic_id, front_content, back_content, hint) VALUES ($1, $2, $3, $4, $5) RETURNING id',
          [chapterId, c.sub_topic_id, c.front_content, c.back_content, c.hint]
        );
        const newCardId = insertRes.rows[0]?.id;
        if (newCardId) {
          await queryFunc(
            'INSERT INTO learning_recall.spaced_repetition_states (flashcard_id, box_number, easiness_factor, repetition_count, interval_days, next_review_date) VALUES ($1, 1, 2.5, 0, 0, CURRENT_DATE) ON CONFLICT (flashcard_id) DO NOTHING',
            [newCardId]
          );
        }
      } else {
        const insertRes = await queryFunc(
          'INSERT INTO flashcards (chapter_id, sub_topic_id, front_content, back_content, hint) VALUES (?, ?, ?, ?, ?)',
          [c.chapter_id, c.sub_topic_id, c.front_content, c.back_content, c.hint]
        );
        const newCardId = insertRes.lastID;
        if (newCardId) {
          await queryFunc(
            'INSERT INTO spaced_repetition_states (flashcard_id, box_number, easiness_factor, repetition_count, interval_days, next_review_date) VALUES (?, 1, 2.5, 0, 0, CURRENT_DATE)',
            [newCardId]
          );
        }
      }
    }
    console.log(`✅ Seeded ${cards.length} default flashcards successfully.`);
  } catch (err) {
    console.error('Failed to seed default flashcards:', err);
  }
};

export const getUsePostgres = () => usePostgres;
