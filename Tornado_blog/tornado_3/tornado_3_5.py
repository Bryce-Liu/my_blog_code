# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 15:30
# @Author  : Bryce Liu
# @FileName: tornado_3_5.py

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1
        self.set_secure_cookie("count", str(count))
        self.write(
                '<html><head><title>Cookie Counter</title></head>'
                '<body><h1>访问量：%d次。</h1>' % count +
                '</body></html>'
        )


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),
    ],
            debug=True,
            cookie_secret="hhLgDUloTO2hKpawAGathnZEwNDbDEAOrNZQLj1DAzk="
    )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()