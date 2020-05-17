from requests import post
from json import dumps
#https://oapi.dingtalk.com/robot/send?access_token=5dd4ff5d073291cd2e2cd8ede59dab434a722b9b2e782e5d297e042b58fd33bd


class bot:
    def __init__(self, token, kw='', secret='', note=''):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token='+token
        self.kw = kw
        self.note = note
        self.secret = secret
        self.head = {'Content-Type': 'application/json','Charset':'UTF-8'}
    def __str__(self):
        return f'DingDing Bot\n    Request head: {self.head}\n    Note: {self.note}\n    Token: {self.url[50::]}'
    def send(self, req):
        if self.secret:
            from sign import Sign
            tick, sign = Sign(self.secret)
            self.url += f'&timestamp={tick}&sign={sign}'
        res = post(self.url, data=dumps(req), headers=self.head).json()
        if res['errmsg'] == 'ok': return res
        else: raise Exception(f'Error code: {res["errcode"]}; Error message: {res["errmsg"]}\n' + str(res))
    def send_text(self, text, at=None, atAll=False):  # text类型
        """ 参数        类型         说明
            'text'      string      发送的消息
            'at'        list        要@的人
            'atAll'     boolean     @全体?"""
        req = {"msgtype": "text",
               "text": {"content": self.kw + text},
               "at": {"atMobiles": at, "isAtAll": atAll}}
        return self.send(req)
    def send_link(self, link, title, text, pic=''):  # link类型
        req = {"msgtype": "link",
            "link": {"text": self.kw + text,
            "title": self.kw + title,
            "picUrl": pic,
            "messageUrl": link}}
        return self.send(req)
    def send_md(self, title, text, at=None, atAll=False):  # markdown类型
        req = {"msgtype": "markdown",
               "markdown": {"title": self.kw + title, "text": text},
               "at": {"atMobiles": at, "isAtAll": atAll}}
        return self.send(req)
    def send_accard1(self, title, text, hide_avatar=False, orientation=False):  # 整体ActionCard类型
        req = {"msgtype": "actionCard",
            "actionCard": {
                "title": title,
                "text": text,
                "hideAvatar": "1" if hide_avatar else "0",
                "btnOrientation": "1" if orientation else "0",
                "singleTitle": "阅读全文",
                "singleURL": "https://www.dingtalk.com/"}}
        return self.send(req)
