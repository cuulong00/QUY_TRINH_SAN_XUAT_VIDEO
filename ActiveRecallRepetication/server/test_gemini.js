import { GoogleGenerativeAI } from '@google/generative-ai';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, '.env') });

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  console.error('No API key found in .env');
  process.exit(1);
}

const genAI = new GoogleGenerativeAI(apiKey);

const testModel = async (modelName) => {
  try {
    console.log(`Testing model: ${modelName}...`);
    const model = genAI.getGenerativeModel({ model: modelName });
    const result = await model.generateContent("Say hello in Vietnamese");
    console.log(`✅ Success with ${modelName}:`, result.response.text());
    return true;
  } catch (err) {
    console.error(`❌ Failed with ${modelName}:`, err.message);
    return false;
  }
};

const run = async () => {
  const models = ['gemini-3.5-flash', 'gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-3.5-pro', 'gemini-2.5-pro', 'gemini-1.5-pro'];
  for (const m of models) {
    const success = await testModel(m);
    if (success) {
      console.log(`Use this model name: ${m}`);
      process.exit(0);
    }
  }
  process.exit(1);
};

run();
