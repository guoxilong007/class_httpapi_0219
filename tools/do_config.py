import configparser
from tools import get_path

class Do_Config():

    @staticmethod
    def do_config(file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        res = cf.get(section, option)
        return res



if __name__ == '__main__':
    res = Do_Config.do_config(get_path.conf_path, "CASE", "case")
    print(res)