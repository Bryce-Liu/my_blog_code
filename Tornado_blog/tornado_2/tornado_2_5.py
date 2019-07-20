# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 13:27
# @Author  : Bryce Liu
# @FileName: tornado_2_5.py


import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("主页")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<form method="post"><input type="submit" value="登陆"></form>')

    def post(self):
        self.redirect("/")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler),  # 生成服务实例，通常包含路由信息
        (r'/login', LoginHandler)
    ], debug=True)
    app.listen(8000)  # 监听端口
    tornado.ioloop.IOLoop.current().start()  # 开启服务
