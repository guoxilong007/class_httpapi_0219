import requests
from tools.my_log import My_Log
import pprint



class Http_Requests():

    @staticmethod
    def http_requests(url, data, method, cookies=None):
        global res
        try:
            if method.lower() == "get":
                res = requests.get(url, data)
            elif method.lower() == "post":
                res = requests.post(url, data, cookies)
            else:
                My_Log().error("http请求错误：{0}".format(method))
        except Exception as e:
            My_Log().error("报错信息是：{0}".format(e))
            raise e
        return res


if __name__ == '__main__':
    url = "http://api.kr-cell.net/login-register/login-by-phone"
    data = {"phone":"10000000573","password":"111111"}
    res = Http_Requests.http_requests(url, data, "post")
    # pprint.pprint(type(res.json()["userID"]))
    pprint.pprint(res.json())
