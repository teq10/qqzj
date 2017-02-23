# -*- coding: utf-8 -*-
from handler.base import BaseHandler
import hashlib
from constant import *
from setting import settings
import os

class InfoViewHandler(BaseHandler):
    def get_default(self):
        self.render("view.html")

    def get_photo(self):
        img = self.get_argument("img", "")
        print img

        if img:
            img = os.path.join(settings['upload_path'] , img)
            # img = "file://" + img
            print img
            self.render("photo.html",img=img)
        else:
            self.render("error.html",message="找不到照片")

    def post_female(self):
        password = self.get_argument('password', '')
        hs = hashlib.md5()
        hs.update(password)
        if PASSWORD == hs.hexdigest():
            females = self.db.query("SELECT * FROM female")
            self.render("infoView.html", users=females,password=password,m="female")
        else:
            self.render("error.html", message="密码错误")

    def post_male(self):
        password = self.get_argument('password', '')
        hs = hashlib.md5()
        hs.update(password)
        if PASSWORD == hs.hexdigest():
            males = self.db.query("SELECT * FROM male ")
            self.render("infoView.html", users=males,password=password,m="male")
        else:
            self.render("error.html", message="密码错误")


