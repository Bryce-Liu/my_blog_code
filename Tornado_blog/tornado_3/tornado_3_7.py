# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 17:04
# @Author  : Bryce Liu
# @FileName: tornado_3_7.py

import tornado.web
import tornado.ioloop


class XSRFTokenHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main3.html")

    def post(self):
        self.write("OK")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', XSRFTokenHandler),
    ],
            debug=True,
            cookie_secret="hhLgDUloTO2hKpawAGathnZEwNDbDEAOrNZQLj1DAzk=",
            xsrf_cookies=True  # 打开xsrf验证需求
    )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
