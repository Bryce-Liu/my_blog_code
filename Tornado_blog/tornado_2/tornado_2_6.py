# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 13:33
# @Author  : Bryce Liu
# @FileName: tornado_2_6.py

import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        err_code = self.get_argument("code", None)
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        if err_code:
            self.send_error(int(err_code), title=err_title, content=err_content)
        else:
            self.write("主页")

    def write_error(self, status_code, **kwargs):
        self.write(u"<h1>出错，需要尽快解决！</h1>")
        self.write(u"<p>error_name：%s</p>" % kwargs["title"])
        self.write(u"<p>error_detail：%s</p>" % kwargs["content"])


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler),  # 生成服务实例，通常包含路由信息
    ], debug=True)
    app.listen(8000)  # 监听端口
    tornado.ioloop.IOLoop.current().start()  # 开启服务
