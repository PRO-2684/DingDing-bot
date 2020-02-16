from requests import post
from json import dumps
#https://oapi.dingtalk.com/robot/send?access_token=5dd4ff5d073291cd2e2cd8ede59dab434a722b9b2e782e5d297e042b58fd33bd
class bot:
    def __init__(self, kw, token):
        self.url='https://oapi.dingtalk.com/robot/send?access_token='+token
        self.kw = kw
        self.head = {'Content-Type': 'application/json;charset=utf-8'}
    def send_text(self, text, at=None, atAll=False):
        """ 参数        类型         说明
            'text'      string      发送的消息
            'at'        list        要@的人
            'atAll'     boolean     @全体?"""
        req = {"msgtype":"text",
               "text":{"content": self.kw + text},
               "at": {"atMobiles": at, "isAtAll": atAll}
               }
        res = post(self.url, data=dumps(req), headers=self.head).json()
        if res['errmsg'] == 'ok': return res
        else: raise Exception(f'Error code: {res["errcode"]}; Error message: {res["errmsg"]}')
if __name__ == '__main__':
    lw = bot("[老王]", token='5dd4ff5d073291cd2e2cd8ede59dab434a722b9b2e782e5d297e042b58fd33bd')
    r = lw.send_text("Hello World!")
    print(r)
