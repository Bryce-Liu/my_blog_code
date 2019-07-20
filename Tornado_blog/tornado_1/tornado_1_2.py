# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 23:50
# @Author  : Bryce Liu
# @FileName: tornado_1_2.py

import tornado.web
import tornado.ioloop
import tornado.httpserver


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', HelloHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)  # 根据app对象生成http server实例对象
    http_server.listen(8000)  # 使用http server对象监听端口
    tornado.ioloop.IOLoop.current().start()
