from setting import settings
import logging
import tornado

class test(tornado.web.RequestHandler):
    def get(self):
        self.write("respond test")