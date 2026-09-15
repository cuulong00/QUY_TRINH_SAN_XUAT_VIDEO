#!/usr/bin/env node
import { debugLog } from './debug-log.js';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { runAuth, queryGem } from './automation.js';

const SERVER_NAME = 'gemini-gems-mcp';
const SERVER_VERSION = '1.0.0';

class GeminiGemsMCPServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: SERVER_NAME,
        version: SERVER_VERSION,
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupHandlers();
    this.setupShutdownHandlers();
  }

  private setupHandlers(): void {
    // 1. List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      debugLog('📋 [Gemini Gems MCP] Yêu cầu list_tools được gọi');
      return {
        tools: [
          {
            name: 'gemini_gems_auth',
            description: 'Xác thực tài khoản Google để truy cập Gemini Gems. Mở cửa sổ trình duyệt Chromium để người dùng đăng nhập thủ công. Hãy chạy công cụ này đầu tiên hoặc khi phiên làm việc bị hết hạn.',
            inputSchema: {
              type: 'object',
              properties: {},
            },
          },
          {
            name: 'query_gem',
            description: 'Gửi câu hỏi tới một Gemini Gem được chỉ định qua URL và nhận về văn bản câu trả lời.',
            inputSchema: {
              type: 'object',
              properties: {
                gemUrl: {
                  type: 'string',
                  description: 'URL đầy đủ của Gem (ví dụ: https://gemini.google.com/gem/ae781ffc92e7)',
                },
                prompt: {
                  type: 'string',
                  description: 'Nội dung câu hỏi/yêu cầu nghiên cứu gửi tới Gem',
                },
                headless: {
                  type: 'boolean',
                  description: 'Chạy trình duyệt ẩn danh dưới nền (mặc định là true). Đặt là false nếu muốn theo dõi trực quan quá trình robot điền text.',
                },
              },
              required: ['gemUrl', 'prompt'],
            },
          },
        ],
      };
    });

    // 2. Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;
      debugLog(`🛠️ [Gemini Gems MCP] Đang gọi tool: ${name}`);

      try {
        switch (name) {
          case 'gemini_gems_auth': {
            await runAuth();
            return {
              content: [
                {
                  type: 'text',
                  text: 'Xác thực hoàn tất! Phiên làm việc (session profile) đã được lưu thành công.',
                },
              ],
            };
          }

          case 'query_gem': {
            const gemUrl = String(args?.gemUrl || '');
            const prompt = String(args?.prompt || '');
            const headless = args?.headless !== false; // mặc định là true

            if (!gemUrl.startsWith('https://gemini.google.com/')) {
              throw new Error('URL của Gem không hợp lệ. Phải bắt đầu bằng https://gemini.google.com/');
            }
            if (!prompt.trim()) {
              throw new Error('Prompt không được để trống.');
            }

            debugLog(`💬 Đang truy vấn Gem tại URL: ${gemUrl}`);
            const responseText = await queryGem(gemUrl, prompt, headless);

            return {
              content: [
                {
                  type: 'text',
                  text: responseText,
                },
              ],
            };
          }

          default:
            throw new Error(`Tool không tồn tại hoặc chưa được hỗ trợ: ${name}`);
        }
      } catch (error: any) {
        debugLog(`❌ Lỗi xảy ra khi thực thi tool ${name}:`, error);
        return {
          isError: true,
          content: [
            {
              type: 'text',
              text: `Lỗi thực thi: ${error.message || error}`,
            },
          ],
        };
      }
    });
  }

  private setupShutdownHandlers(): void {
    const shutdown = async () => {
      debugLog('🔌 Đang tắt Gemini Gems MCP Server...');
      await this.server.close();
      process.exit(0);
    };

    process.on('SIGINT', shutdown);
    process.on('SIGTERM', shutdown);
  }

  public async start(): Promise<void> {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    debugLog('🚀 Gemini Gems MCP Server đã kết nối thành công qua Stdio!');
  }
}

const server = new GeminiGemsMCPServer();
server.start().catch((err) => {
  debugLog('💥 Lỗi nghiêm trọng khi chạy server:', err);
  process.exit(1);
});