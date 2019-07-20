# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 23:42
# @Author  : Bryce Liu
# @FileName: tornado_1_1.py

import tornado.web
import tornado.ioloop


class HelloHandler(tornado.web.RequestHandler):  # 封装一个请求对应的所有方法
    def get(self):
        self.write("hello world")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', HelloHandler),  # 生成服务实例，通常包含路由信息
    ])
    app.listen(8000)  # 监听端口
    tornado.ioloop.IOLoop.current().start()  # 开启服务
