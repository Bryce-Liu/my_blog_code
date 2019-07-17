# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 23:55
# @Author  : Bryce Liu
# @FileName: tornado_1_3.py

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
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(8000)  # 服务绑定到8000端口
    http_server.start(0)  # 根据设备核数开启指定数量子进程
    tornado.ioloop.IOLoop.current().start()
