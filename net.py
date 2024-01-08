from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # 构造 JSON 响应
        response_data = {'message': 'Hello, this is a JSON response!'}
        response_json = json.dumps(response_data)

        # 发送响应内容
        self.wfile.write(response_json.encode('utf-8'))


def startNet():
    # 指定监听的端口
    port = 8080

    # 创建 HTTP 服务器，使用 SimpleRequestHandler 处理请求
    server = HTTPServer(('0.0.0.0', port), SimpleRequestHandler)
    print(f'Starting server on port {port}...')

    try:
        # 启动服务器
        server.serve_forever()
    except KeyboardInterrupt:
        # 如果接收到 Ctrl+C，则停止服务器
        print('Server stopped.')
        server.server_close()
