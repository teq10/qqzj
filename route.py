# -*- coding: utf-8 -*-

routes = [
    (r"/", "handler.weixin.WeixinHandler"),
    (r"/menu", "handler.weixinmenu.WeixinMenuHandler"),
    (r"/test", "handler.test.test"),
    (r"/oauth", "handler.oauth.WxOauthHandler")
]
