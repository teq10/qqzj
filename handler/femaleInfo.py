# -*- coding: utf-8 -*-
from handler.base import BaseHandler


class FemaleHandler(BaseHandler):
    def get_default(self):
        self.render("femaleInfo.html", message="")

    def isNull(self, value, message):
        if not value:
            self.render("femaleInfo.html", message=message)

    def post_default(self):
        nickName = self.get_argument('nickName', '')
        if not nickName:
            self.render("femaleInfo.html", message="昵称不能为空")
            return

        wechatId = self.get_argument('wechatId', '')
        if not wechatId:
            self.render("femaleInfo.html", message="微信号不能为空")
            return

        phone = self.get_argument('phone', '')
        if not phone:
            self.render("femaleInfo.html", message="手机号不不能为空")
            return

        birth = self.get_argument('birth', '')
        if not birth:
            self.render("femaleInfo.html", message="出生年月不能为空")
            return

        height = self.get_argument('height', '')
        if not height:
            self.render("femaleInfo.html", message="身高不能为空")
            return

        city = self.get_argument('city', '')
        if not city:
            self.render("femaleInfo.html", message="城市不能为空")
            return

        job = self.get_argument('job', '')
        if not job:
            self.render("femaleInfo.html", message="职业不能为空")
            return

        income = self.get_argument('income', '')
        if not income:
            self.render("femaleInfo.html", message="收入不能为空")
            return

        parents = self.get_argument('parents', '')
        if not parents:
            self.render("femaleInfo.html", message="父母情况不能为空")
            return

        isSingleton = self.get_argument('isSingleton', '')
        if not isSingleton:
            self.render("femaleInfo.html", message="是否独生子女不能为空")
            return

        # print isSingleton
        # isSingleton = 1 if isSingletonStr == u"是" else 0
        hobby = self.get_argument('hobby', '')
        if not hobby:
            self.render("femaleInfo.html", message="兴趣爱好不能为空")
            return

        intro = self.get_argument('intro', '')
        if not intro:
            self.render("femaleInfo.html", message="自我介绍不能为空")
            return

        idealMate = self.get_argument('idealMate', '')
        if not idealMate:
            self.render("femaleInfo.html", message="伴侣要求不能为空")
            return

        lifePhoto = self.get_argument('lifePhoto', '')
        if not lifePhoto:
            self.render("femaleInfo.html", message="个人生活照不能为空")
            return

        girl = self.db.get("SELECT id FROM female WHERE wechatId = %s", wechatId)
        if girl:
            self.render("femaleInfo.html", message="您已经填写过资料了，如有疑问，请在公众号留言")
        else:
            self.db.execute("insert into female "
                            "(nickName, wechatId, phone, birth, height, "
                            " city, job, income, parents, isSingleton, hobby,"
                            " intro, idealMate, img, applyDate) "
                            "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            , nickName, wechatId, phone, birth, height,
                            city, job, income, parents, isSingleton, hobby,
                            intro, idealMate, lifePhoto, self.curr_now)
            self.render("femaleInfo.html", message="提交成功，如有合适对象，我们会联系您")
