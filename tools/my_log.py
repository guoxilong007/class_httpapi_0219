import logging
from tools import get_path

class My_Log():

    def my_log(self, level, msg):
        # 创建log名称
        loger = logging.Logger("wepie")
        # 收集log级别
        loger.setLevel(level)
        # 设置输出log样式
        format_loger = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")
        # 输出日志到控制台
        sh = logging.StreamHandler()
        sh.setLevel(level)
        sh.setFormatter(format_loger)
        # 输出日志到txt文件
        fh = logging.FileHandler(get_path.log_path, encoding="utf-8")
        fh.setLevel(level)
        fh.setFormatter(format_loger)
        # 收集和输出合并
        loger.addHandler(sh)
        loger.addHandler(fh)

        if level == "INFO":
            loger.info(msg)
        elif level == "DEBUG":
            loger.debug(msg)
        elif level == "ERROR":
            loger.error(msg)
        elif level == "WARNING":
            loger.warning(msg)
        elif level == "CRITICAL":
            loger.critical(msg)

        # 关闭日志文件
        loger.removeHandler(sh)
        loger.removeHandler(fh)

    def info(self, msg):
        self.my_log("INFO", msg)

    def debug(self, msg):
        self.my_log("DEBUG", msg)

    def error(self, msg):
        self.my_log("ERROR", msg)

    def warning(self, msg):
        self.my_log("WARNING", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)


if __name__ == '__main__':
    My_Log().error("hhhhh")

