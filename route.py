# -*- coding: utf-8 -*-

routes = [
    (r"/", "handler.test.test"),
    (r"/test", "handler.test.test"),
    (r"/female", "handler.femaleInfo.FemaleHandler"),
    (r"/male", "handler.maleInfo.MaleHandler"),
    (r"/upload", "handler.upload.UploadHandler"),
    (r"/view", "handler.infoView.InfoViewHandler")
]
