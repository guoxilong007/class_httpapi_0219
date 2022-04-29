import os
import datetime

# 获取到顶级目录
top_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 获取到日志文件路径
log_path = os.path.join(top_path, "data", "log", "{}".format(datetime.datetime.now())+"_http_api.txt")

# 获取到测试用例文件路径
case_path = os.path.join(top_path, "data", "test_case", "test_case.xlsx")

# 获取到测试报告文件路径
report_path = os.path.join(top_path, "data", "test_report", "test_api.html")

# 获取到配置文件路径
conf_path = os.path.join(top_path, "conf", "data.config")



if __name__ == '__main__':
    print(top_path)
    print(log_path)
    print(case_path)
    print(report_path)
    print(conf_path)