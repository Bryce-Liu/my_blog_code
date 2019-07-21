# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 11:40
# @Author  : Bryce Liu
# @FileName: tornado_3_2.py


import tornado.web
import tornado.ioloop
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie("cookie1", "version1")  # 设置cookie
        cookie = self.get_cookie("cookie1")  # 获取cookie
        self.write(cookie)  # 将cookie打印出来


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler)
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
