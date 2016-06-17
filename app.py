# -*- coding: utf-8 -*-
import tornado.ioloop
import torndb
import tornado.web
import tornado.httpserver
from tornado.options import options

from route import routes
from setting import settings

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, routes, **settings)
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database, time_zone="+8:00",
            user=options.mysql_user, password=options.mysql_password)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    print 1
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    print 2
    http_server.listen(options.port)
    print 3
    tornado.ioloop.IOLoop.instance().start()
