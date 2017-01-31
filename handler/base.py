# -*- coding: utf-8 -*-
import os
import uuid
import tornado.web
import datetime,time
import json
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

    def upload_file(self, store_path, file_name=None, p_file_name="uploadImage"):
        """
        上传通用函数,文件上传后如果不填写文件名，
        系统自动生成唯一文件名。
        @:param store_path * :上传文件的存储路径 /file/store/
        @:param file_name :文件上传后的存储名 123.xls
        """
        try:
            if len(self.request.files) == 0:
                imgData = self.request.body
                fileName = self.get_argument(p_file_name)
            else:
                image = self.request.files[p_file_name][0]
                imgData = image["body"]
                fileName = image["filename"]

            if file_name is None:
                file_name = str(uuid.uuid1()).replace("-", "") + os.path.splitext(fileName)[-1]

            filepath = os.path.join(store_path, file_name)

            if not os.path.exists(store_path):
                os.makedirs(store_path)
            with open(filepath, 'wb') as up:
                up.write(imgData)

        except Exception, e:
            file_name = None

        finally:
            return file_name
