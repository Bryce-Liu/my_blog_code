# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 11:13
# @Author  : Bryce Liu
# @FileName: tornado_3_1.py

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
        # 通过set_header来设置cookie
        self.set_header("Set-Cookie", "cookie5=version5; expires=Fri, 11 Aug 2019 15:59:59 GMT; Path=/")
        self.write("OK")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),  # 生成服务实例，通常包含路由信息
    ], debug=True)
    app.listen(8000)  # 监听端口
    tornado.ioloop.IOLoop.current().start()  # 开启服务
