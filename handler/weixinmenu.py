# -*- coding: utf-8 -*-

from base import *
import logging


class WeixinMenuHandler(BaseHandler):
    def get_default(self):
        #get old menu message
        access_token = self.get_access_token()
        menu_history = ""
        if access_token:
            html = requests.get(Const.URL_GET_MENU % access_token)
            menu_history = json.loads(html.content)
        self.render("menu_history.html", menu_history=menu_history)
        log_info = {"handler":__name__ + '.' + self.__class__.__name__, "event":"get_menu"}
        logging.info(log_info)

    def post_menusave(self):
        #edit menu
        name0 = self.get_argument("name0",'')
        if not name0:
            return
        body = {}
        newmenu = []
        for i in range(3):
            name = self.get_argument("name"+str(i),'')
            url = self.get_argument("url"+str(i),'')
            if url and name :
                newmenu.append({'type': 'view', 'name': name, 'url': url})
            elif name:
                subbutton = []
                for j in range(5):
                    subname = self.get_argument("name"+str(i)+str(j),'')
                    suburl = self.get_argument("url"+str(i)+str(j),'')
                    if not suburl or not subname:
                        break
                    subbutton.append({'type': 'view', 'name': subname, 'url': suburl})
                newmenu.append({'name': name, 'sub_button': subbutton})
            else:
                break
        body['button'] = newmenu
        #print body
        '''
        access_token = self.get_access_token()
        if access_token:
            html = requests.get(Const.URL_CREATE_MENU % access_token,json.dump(body))
        '''
        for wxapp in self.wxapps:
            access_token = self.get_access_token(wxapp)
            if access_token:
                data = json.dumps(body,ensure_ascii=False).encode("utf-8")
                html = requests.post(Const.URL_CREATE_MENU % access_token, data)
                #print data

                result = json.loads(html.content)
                #print result
                log_info = {"handler":__name__ + '.' + self.__class__.__name__, "event":"edit_menu",'result':result}
                logging.info(log_info)
        self.get_default()



