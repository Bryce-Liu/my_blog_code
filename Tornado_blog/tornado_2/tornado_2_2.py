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
        url = self.reverse_url("python_url")
        self.write('<a href="%s">python_url</a>' % url)


class TestHandler(tornado.web.RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', HelloHandler),
        (r'/test', TestHandler, {"subject": "c++"}),
        tornado.web.url(r'/python', TestHandler, {"subject": "python"}, name="python_url"),
    ], debug=True
    )
    app.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
