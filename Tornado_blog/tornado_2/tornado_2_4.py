# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 13:06
# @Author  : Bryce Liu
# @FileName: tornado_2_4.py


import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int, help="define port")


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


class TestHandler(tornado.web.RequestHandler):
    def get(self, subject, city):  # 按顺序传递需要注意参数的顺序，避免混乱
        self.write(("Subject: %s<br/>City: %s" % (subject, city)))


class PythonHandler(tornado.web.RequestHandler):
    def get(self, city, subject):  # 这里将顺序写反，但因为按名称传递，也能够正确获得url中的参数
        self.write(("Subject: %s<br/>City: %s" % (subject, city)))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', HelloHandler),
        (r'/test/(.+)/([a-z]+)', TestHandler),  # 没有定义名称，因此按顺序传递
        (r'/python/(?P<subject>.+)/(?P<city>[a-z]+)', PythonHandler),  # 定义了名称，因此按名称传递
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

    # python hello_tornado_options.py --port=9000 --language=python,c++,java
