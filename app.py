# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import options

from route import routes
from setting import settings

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, routes, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()
