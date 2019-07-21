# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 11:44
# @Author  : Bryce Liu
# @FileName: tornado_3_3.py


import tornado.web
import tornado.ioloop
import time


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie("cookie1", "version1")
        self.set_cookie("cookie2", "version2", path="/cookie2",
                        expires=time.strptime("2019-08-11 23:59:59", "%Y-%m-%d %H:%M:%S"))
        self.set_cookie("cookie3", "version3", expires_days=20)
        # 利用time.mktime将本地时间转换为UTC标准时间
        self.set_cookie("cookie4", "version4",
                        expires=time.mktime(time.strptime("2019-08-11 23:59:59", "%Y-%m-%d %H:%M:%S")))
        self.write("OK")


class ClearOneCookieHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("cookie3")  # 清除cookie3对应的cookie值
        self.write("OK")


class ClearAllCookieHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_all_cookies()  # 清除所有cookie
        self.write("OK")


class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("OK")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),  # 生成服务实例，通常包含路由信息
        (r'/clear_one', ClearOneCookieHandler),
        (r'/clear_all', ClearAllCookieHandler),
        (r'/cookie2', CookieHandler)
    ], debug=True)
    app.listen(8000)  # 监听端口
    tornado.ioloop.IOLoop.current().start()  # 开启服务
