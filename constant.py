# -*- coding: utf-8 -*-

URL_ACCESS_TOKEN = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
URL_GET_MENU = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s"
URL_CREATE_MENU = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s"
URL_DEL_MENU = ""

URL_MAIN = "http://166.111.180.96:8080/Smart_Service_Platform/SearchResultOnly_WeiXin.jsp?SearService=%s"
URL_WEB = "http://166.111.180.96:8080/Smart_Service_Platform/SearchResultOnly_WeiXinWeb.jsp?SearService=%s"
URL_HOTEL = "http://166.111.180.96:8080/Smart_Service_Platform/Weixin_Hotel.jsp"
URL_SPOT = "http://166.111.180.96:8080/Smart_Service_Platform/Weixin_Spot.jsp"
URL_RESTAURANT = "http://166.111.180.96:8080/Smart_Service_Platform/Weixin_Restaurant.jsp"
URL_SERVICE = "http://166.111.180.96:8080/Smart_Service_Platform/Weixin_%s.jsp"


#need to change
#test
#WXAPP = "wxfd670b21fe078e9a"
#WXAPP_SECRET = "d4624c36b6795d1d99dcf0547af5443d"
WXAPP = "wxff3a9fc0253c008e"
WXAPP_SECRET = "dfb32f5ce12c49001ea700d709233083"

URL = "http://wxtest.teq6.com/"


# 微信api常量定义
WXAPI_AUTHORIZE = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={APPID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}&state={STATE}#wechat_redirect"
WXAPI_WXUSER_ACCESS_TOKEN = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={APPID}&secret={SECRET}&code={CODE}&grant_type=authorization_code"
WXAPI_USERINFO = "https://api.weixin.qq.com/sns/userinfo?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN"

