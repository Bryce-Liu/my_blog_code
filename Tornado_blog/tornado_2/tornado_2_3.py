# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 12:44
# @Author  : Bryce Liu
# @FileName: tornado_2_3.py

import tornado.web
import tornado.ioloop


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.request.headers)


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', HelloHandler),  # 生成服务实例，通常包含路由信息
    ])
    app.listen(8000)  # 监听端口
    tornado.ioloop.IOLoop.current().start()  # 开启服务
