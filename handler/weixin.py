# -*- coding: utf-8 -*-

import sys
import xml.etree.ElementTree as ET
from hashlib import sha1

import hashlib
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from base import *
from setting import settings
import logging



class WeixinHandler(BaseHandler):

    def check_xsrf_cookie(self):
        return True

    def get_default(self):

        echostr = self.get_argument('echostr', '')
        if echostr and self.verification():
            # sanitize xss filter
            self.write(echostr)
            res = "weixin callback success"
        else:
            self.write("")
            res = "weixin callback failed"
        log_info = {"handler":__name__ + '.' + self.__class__.__name__, "event":sys._getframe().f_code.co_name,
                    "event_description":"", "res_type":"xml", "res_content":{"message":res, "echostr":echostr}}
        logging.info(log_info)

    def get_current_user(self):

        return None

    def post_default(self):
        msg = self.get_msg()
        #print msg
        try:

            msg_type = msg['MsgType']

            if self.verification():
                #print "True"
                info = getattr(self, 'post_' + msg_type)(msg)
            else :
                #print "False"
                info = u"Message verification failed"
            logging.info(info)
            if info:
                self.write(self.rep_text(msg, info))
        except Exception, e:
            logging.error(e)

    def get_msg(self):
        return self.parse_msg(self.request.body)

#事件处理
    def post_event(self, msg):
        event = msg['Event']
        getattr(self, 'event_' + event)(msg)

    def event_subscribe(self, msg):
        weixinid = msg["FromUserName"]
        user = self.db.get("SELECT id FROM user WHERE openid = %s", weixinid)

        if not user:
            self.db.execute("insert into user "
                        "(openid) "
                        "values (%s) "
                        ,weixinid)

        #print weixinid
        self.write(self.rep_follow(msg))

    def event_unsubscribe(self, msg):
        self.write(self.rep_unfollow(msg))

    def event_CLICK(self, msg):
        msg['Content'] = msg['EventKey']
        self.post_text(msg)

    def event_VIEW(self, msg):
        pass


    def event_LOCATION(self, msg):
        # Need log to record location information of users
        weixinid = msg['FromUserName']
        Latitude = msg['Latitude']
        Longitude = msg['Longitude']
        user = self.db.get("SELECT id FROM user WHERE openid = %s", weixinid)

        if not user:
            self.db.execute("insert into user "
                        "(openid) "
                        "values (%s) "
                        ,weixinid)
        self.db.execute("update user set latitude=%s,longitude = %s,time=%s"
                        "where openid = %s"
                        ,Latitude, Longitude,weixinid,self.curr_now)
        print Latitude
        #self.write("success")


#
    def post_text(self, msg):
        try:
            weixinid = msg['FromUserName']
            keyword = msg['Content'].strip().encode('utf-8')
            #图灵机器人
            #url = "http://www.tuling123.com/openapi/api?key=c676b2dd0e54d0612fd37c47fa8c1e5d&info=%s&userid=%s" % (keyword, weixinid)
            #print keyword
            url = Const.URL_MAIN % (keyword)
            #print url
            respond = requests.get(url)
            respond = respond.content.strip()
            #code = respond.get('code')
           # text = respond.encode('utf-8')
            #url = respond.get('url').encode('utf-8')
            url = Const.URL_WEB% (keyword)

            info =respond + "\n\n"+"<a href='"+url+"'>查看更多</a>"
            return info
        except Exception, e:
            #print e
            pass

            '''

            if code == 100000:
                return respond.get('text').encode('utf-8')
            elif code == 200000:#链接
                text = respond.get('text').encode('utf-8')
                url = respond.get('url').encode('utf-8')
                info = text+"\n\n"
                info =info + "<a href='"+url+"'>点击查看</a>"
                return info
            elif code == 305000:#列车
                text = respond.get('text').encode('utf-8')
                lists = respond.get('list')
                info = text+" 点击查看\n\n"
                for train in lists:
                    info =info + "<a href='"+train['detailurl'].encode('utf-8')+"'>"+train['trainnum'].encode('utf-8')+":"\
                          +train['start'].encode('utf-8')+train['terminal'].encode('utf-8')+"</a>\n\n"
                return info
            elif code == 302000:#新闻
                text = respond.get('text').encode('utf-8')
                lists = respond.get('list')
                info = text+" 点击查看\n\n"
                for news in lists:
                    info =info + "<a href='"+news['detailurl'].encode('utf-8')+"'>"+news['article'].encode('utf-8')+"</a>\n\n"
                return info
            elif code == 306000:#航班
                text = respond.get('text').encode('utf-8')
                lists = respond.get('list')
                info = text+" \n\n"
                for plain in lists:
                    info =info +plain['flight'].encode('utf-8')+":"+plain['starttime'].encode('utf-8')+"\n\n"
                return info
            elif code == 308000:#菜谱
                text = respond.get('text').encode('utf-8')
                lists = respond.get('list')
                info = text+" 点击查看\n\n"
                for menu in lists:
                    info =info + "<a href='"+menu['detailurl'].encode('utf-8')+"'>"+menu['name'].encode('utf-8')+":"+menu['info'].encode('utf-8')[:15]+"...</a>\n\n"
                return info

            else:
                    return "error"
         '''

	    pass
    def post_image(self, msg):#图片消息
        self.write("这是一个图片")

    def post_voice(self, msg):#
        self.write(self.rep_default(msg))

    def post_video(self, msg):
        self.write(self.rep_default(msg))

    def post_location(self, msg):
        self.write(self.rep_default(msg))

    def post_link(self, msg):
        self.write(self.rep_default(msg))

    def post_shortvideo(self, msg):
        self.write(self.rep_default(msg))

    def verification(self):

        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')

        token = settings.get("token")

        tmplist = [token, timestamp, nonce]
        tmplist.sort()
        tmpstr = ''.join(tmplist)
        hashstr = hashlib.sha1(tmpstr).hexdigest()

        if hashstr == signature:
            return True
        return False

  #


#回复消息

    def rep_text(self, msg, text):
        rep_info = """
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>
                    """
        info = rep_info % (msg['FromUserName'], msg['ToUserName'],
                           str(int(time.time())), str(text))

        return info

    def rep_news(self, msg, rid):

        ARTICLE_HEAD_TPL = \
            u"""
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>%d</ArticleCount>
            <Articles>
            """
        ARTICLE_ITEM_TPL = \
            u"""
            <item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item>
            """
        ARTICLE_FOOT_TPL = \
            u"""
            </Articles>
            </xml>
            """

        replies = None
        # print replies

        article = ARTICLE_HEAD_TPL % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), len(replies))

        for reply in replies:
            url = reply.url
            if len(url) == 0 or url.find('/cms/article') == 0:
                url = 'http://%s/cms/article?id=%s&m=rule_content&wid=%s&wechat_signature=%s' % (
                self.request.host, reply.id, msg['FromUserName'], self.current_user.wechat.signature)
            elif url.find('http') == -1:
                # generate timetoken
                timetoken = self.gen_timetoken(msg['FromUserName'])
                url = 'http://' + self.request.host + url.replace('WEIXIN_ID',
                        msg['FromUserName']).replace('TIMETOKEN',
                        timetoken).replace('SIGNATURE',self.current_user.wechat.signature)
            else:
                url = url.replace("WEIXIN_ID", msg['FromUserName'])
            thumbpic = self.static_url(reply.thumb)
            item = ARTICLE_ITEM_TPL % (
                reply.title,
                reply.description,
                # urlparse.urljoin('http://' + self.request.host, '/' + settings['upload_path'] + 'img/' + reply.thumb),
                thumbpic if thumbpic.startswith('http') else ('http:'+thumbpic),
                url.replace('WEIXIN_ID', msg['FromUserName']) if url else ''
            )
            article += item

        info = article + ARTICLE_FOOT_TPL

        return info

    def rep_default(self, msg):
        return self.rep_text(msg, '您好！欢迎关注智能旅游服务平台，目前平台仅支持北京3～5日游旅游线路设计，如不明确规定旅游天数，将按照5日游设计线路。欢迎向我提问啦～（回复示例：“打算去北京玩4天，想吃全聚德”、“北京五日游线路推荐，想去八达岭长城”）')


    def rep_follow(self, msg):
        return self.rep_text(msg, '您好！欢迎关注智能旅游服务平台，目前平台仅支持北京3～5日游旅游线路设计，如不明确规定旅游天数，将按照5日游设计线路。欢迎向我提问啦～（回复示例：“打算去北京玩4天，想吃全聚德”、“北京五日游线路推荐，想去八达岭长城”）')
    def rep_unfollow(self, msg):
        return self.rep_text(msg,'byebye,你不要我了，5555')


    def parse_msg(self, rawmsgstr):
        root = ET.fromstring(rawmsgstr)
        msg = {}
        for child in root:
            msg[child.tag] = child.text
        return msg




##
    def gen_timetoken(self, weixinid):
        now = str(time.strftime('%Y%m%d%H',time.localtime(time.time())))
        minite = str(time.localtime(time.time()).tm_min/10)
        timetoken = ''.join([weixinid, now, minite])
        return sha1(timetoken).hexdigest()
