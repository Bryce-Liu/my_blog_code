# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:56
# @Author  : Bryce Liu
# @FileName: tornado_2_2.py

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int, help="define port")


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        url = self.reverse_url("python_url")  # url=127.0.0.1:8000/python
        self.write('<a href="%s">python_url</a>' % url)  # 生成一个简单的连接，访问


class TestHandler(tornado.web.RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)  # 根据请求的url取得不同的subject值


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', HelloHandler),
        (r'/test', TestHandler, {"subject": "c++"}),  # /test传到TestHandler中的subject参数是c++
        tornado.web.url(r'/python', TestHandler, {"subject": "python"}, name="python_url"),
        # 即/python的name=python_url，/python传到TestHandler中的subject参数是python
    ], debug=True
    )
    app.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
