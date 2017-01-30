# -*- coding: utf-8 -*-
from handler.base import BaseHandler

class MaleHandler(BaseHandler):
    def get_default(self):
        self.render("maleInfo.html", message="")

    def isNull(self, value, message):
        if not value:
            self.render("maleInfo.html", message=message)

    def post_default(self):
        nickName = self.get_argument('nickName', '')
        self.isNull(nickName, "昵称不能为空")
        wechatId = self.get_argument('wechatId', '')
        self.isNull(wechatId, "微信号不能为空")
        phone = self.get_argument('phone', '')
        self.isNull(phone, "手机号不能为空")
        birth = self.get_argument('birth', '')
        self.isNull(birth, "出生年月不能为空")
        height = self.get_argument('height', '')
        self.isNull(height, "身高不能为空")
        city = self.get_argument('city', '')
        self.isNull(city, "城市不能为空")
        job = self.get_argument('job', '')
        self.isNull(job, "职业不能为空")
        income = self.get_argument('income', '')
        self.isNull(income, "收入不能为空")
        parents = self.get_argument('parents', '')
        self.isNull(parents, "父母情况不能为空")
        isSingleton = self.get_argument('isSingleton', '')
        self.isNull(isSingleton, "是否独生子女不能为空")
        hasCar = self.get_argument('isSingleton', '')
        self.isNull(hasCar, "是否有车不能为空")
        hasHouse = self.get_argument('isSingleton', '')
        self.isNull(hasHouse, "是否有房不能为空")

        hobby = self.get_argument('hobby', '')
        self.isNull(hobby, "兴趣爱好不能为空")
        intro = self.get_argument('intro', '')
        self.isNull(intro, "自我介绍不能为空")
        idealMate= self.get_argument('idealMate', '')
        self.isNull(idealMate, "伴侣要求不能为空")
        # = self.get_argument('', '')

        boy = self.db.get("SELECT id FROM male WHERE wechatId = %s", wechatId)
        if boy:
            self.render("maleInfo.html", message="您已经填写过资料了，如有疑问，请在公众号留言")
        else:
            self.db.execute("insert into male "
                       "(nickName, wechatId, phone, birth, height, "
                        " city, job, income, parents, isSingleton,"
                            " hasCar, hasHouse,hobby,"
                        " intro, idealMate, applyDate) "
                       "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                       , nickName, wechatId, phone, birth, height,
                        city, job, income, parents, isSingleton,
                            hasCar, hasHouse, hobby,
                        intro, idealMate, self.curr_now)
            self.render("maleInfo.html", message="提交成功，如有合适对象，我们会联系您")
