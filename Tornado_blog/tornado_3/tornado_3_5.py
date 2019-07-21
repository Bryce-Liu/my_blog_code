# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 15:30
# @Author  : Bryce Liu
# @FileName: tornado_3_5.py

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):  # 向当前url发送post请求
        self.write(
                """<form method="post"><input type="text" name="message"/><input type="submit" value="Post"/></form>""")

    def post(self):
        self.write("hello world")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),
    ],
            debug=True,
            cookie_secret="hhLgDUloTO2hKpawAGathnZEwNDbDEAOrNZQLj1DAzk=",
            xsrf_cookies=True  # 打开xsrf验证需求
    )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
