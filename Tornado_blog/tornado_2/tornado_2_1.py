# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:56
# @Author  : Bryce Liu
# @FileName: tornado_2_1.py

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int, help="define port")


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")


class TestHandler(tornado.web.RequestHandler):
    def initialize(self, subject, score):
        # 将参数取出
        self.subject = subject
        self.score = score

    def get(self):
        self.write(self.subject)
        self.write(str(self.score))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', HelloHandler),
        (r'/test', TestHandler, {"subject": "c++", "score": 90})  # 定义TestHandler的参数
    ], debug=True
    )
    app.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
