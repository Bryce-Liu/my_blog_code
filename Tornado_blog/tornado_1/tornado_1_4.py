# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 23:40
# @Author  : Bryce Liu
# @FileName: tornado_1_4.py

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# 定义options涉及的参数
tornado.options.define("port", default=8000, type=int, help="define port")
tornado.options.define("language", default=[], type=str, multiple=True, help="just for test")


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


if __name__ == '__main__':
    # tornado.options.parse_command_line()获取命令中传递的参数，并保存到tornado.options.options的属性中
    tornado.options.parse_command_line()

    print(tornado.options.options.language)  # 打印language
    app = tornado.web.Application([
        (r'/', HelloHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)  # 获得传入的port
    tornado.ioloop.IOLoop.current().start()

    # 使用如下命令传入参数
    # python tornado_1_4.py --port=9000 --language=python,c++,java
