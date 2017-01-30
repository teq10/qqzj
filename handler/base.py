# -*- coding: utf-8 -*-
import tornado.web
import datetime,time
import requests,json
from setting import settings
import constant as Const
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    @property
    def curr_now(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get(self):
        method = self.get_argument('m', 'default')
        getattr(self, 'get_' + method)()

    def post(self):
        method = self.get_argument('m', 'default')
        getattr(self, 'post_' + method)()
