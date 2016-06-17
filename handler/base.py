# -*- coding: utf-8 -*-
import tornado.web
import datetime,time
import requests,json
from setting import settings
import constant as Const
class BaseHandler(tornado.web.RequestHandler):
    @property
    def wxapps(self):
        return settings['wxapps']
    @property
    def curr_now(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get(self):
        method = self.get_argument('m', 'default')
        getattr(self, 'get_' + method)()

    def post(self):
        method = self.get_argument('m', 'default')
        getattr(self, 'post_' + method)()

    def renew_access_token(self,wxapp=Const.WXAPP):

        if (not self.wxapps[wxapp]['access_token']) or\
                                int(time.time())-self.wxapps[wxapp]['create_time'] > self.wxapps[wxapp]['expires_in']/2:
            html = requests.get(Const.URL_ACCESS_TOKEN % (wxapp, self.wxapps[wxapp]['app_secret']))
            token = json.loads(html.content)

            if token and token.get("access_token", 0) != 0:

                access_token = token['access_token']
                expires_in = token['expires_in']
                access_token_create_time = int(time.time())
                self.wxapps[wxapp]['access_token'] = access_token
                self.wxapps[wxapp]['expires_in'] = expires_in
                self.wxapps[wxapp]['create_time'] = access_token_create_time
                return True
            else:
                return False

        return True

    def get_access_token(self, wxapp=Const.WXAPP):
        if self.renew_access_token(wxapp):
            return self.wxapps[wxapp]['access_token']
        else:
            return ""

    def get_default(self):
       # print self.curr_now
        pass
        #self.render("index.html",message = u"")

    def get_current_user(self):
        pass
