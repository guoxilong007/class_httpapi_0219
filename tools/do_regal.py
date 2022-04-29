import re
from tools import get_data


class Do_Regal():

    @staticmethod
    def do_regal(s):
        # 对该正则表达式进行替换，使用while循环可以进行多次替换
        while re.search("\$\{(.*?)\}", s):
            # key变量对应整个参数化的变量，例：${timing_phone}
            key = re.search("\$\{(.*?)\}", s).group(0)
            # value变量对应参数话变量括号内的变量名，例：timing_phone
            value = re.search("\$\{(.*?)\}", s).group(1)
            # 对参数化的变量进行替换
            s = s.replace(key, str(getattr(get_data.Get_Data(), value)))
        return s



if __name__ == '__main__':
    s = '{"sql":"select ID from t_user where phone=${timing_phone}"}'
    res = Do_Regal.do_regal(s)
    print(res)
