# -*- coding: utf-8 -*-
from setting import settings
from handler.base import BaseHandler

class UploadHandler(BaseHandler):

    def post(self):
        filename = self.upload_file(settings["upload_path"])
        if filename:
            filename = "/static/upload/" + filename
        self.write({"imgUrl": filename})