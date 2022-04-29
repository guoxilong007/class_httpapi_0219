import unittest
from tools.my_log import My_Log
from tools.do_mysql import Do_Mysql
from tools.do_excel import Do_Excel
from ddt import ddt,data
from tools import get_path
from tools.get_data import Get_Data
from tools.http_requests import Http_Requests

test_data = Do_Excel().do_excel(get_path.case_path)


@ddt
class Test_Http_Api(unittest.TestCase):

    def setUpClass(cls):
        pass

    def teardown(self):
        pass

    @data(*test_data)
    def test_http_api(self, item):
        global passed
        # 替换${userID}参数化
        if item["data"].find("${userID}") != -1:
            if getattr(Get_Data(), "userID") == None:
                # 在数据库内查询userid的sql语句
                sql = "select ID from t_user where phone = {0}".format(getattr(Get_Data(), "timing_phone"))
                # 调用mysql方法查询userid
                user_id = Do_Mysql().do_mysql(sql, 1)[0][0]
                # 将data内的${userID}参数化变量替换成从数据库内提取出来的userid
                item["data"] = item["data"].replace("${userID}", str(user_id))
                # 将数据库内获取到的userid存储到getdata内
                setattr(Get_Data(), "userID", user_id)
            else:
                item["data"] = item["data"].replace("${userID}", str(getattr(Get_Data(), "userID")))

        # 数据库验证接口返回结果是否正确
        if item["check_sql"] != None:
            # 校验的是那一条用例
            My_Log().info("校验的用例为：{0}".format(item["title"]))
            # 获取到excel内的sql语句
            excel_sql = eval(item["check_sql"])["sql"]
            My_Log().error(excel_sql)
            # 在接口请求前执行sql语句并获取到执行sql语句后的值
            db_value = Do_Mysql().do_mysql(excel_sql, 1)[0]
            # 执行接口请求
            res = Http_Requests.http_requests(item["url"], eval(item["data"]), item["method"], getattr(Get_Data(), "COOKIES"))
            # 接口请求后再获取到请求后的sql数据
            new_db_value = Do_Mysql().do_mysql(excel_sql, 1)[0]
            if db_value == new_db_value:
                sql_result = "数据库验证通过"
            else:
                sql_result = "数据库验证不通过"
            # 将数据库验证结构写入到excel内
            Do_Excel().result_back(get_path.case_path, item["sheet_name"], item["case_id"]+1, 11, sql_result)
        else:
            res = Http_Requests.http_requests(item["url"], eval(item["data"]), item["method"], getattr(Get_Data(), "COOKIES"))

        # 以下为公共代码
        if res.cookies:
            setattr(Get_Data(), "COOKIES", res.cookies)

        # 断言
        try:
            self.assertEqual(item["expected"], res.json()["errorMsg"])
            passed = "PASS"
        except Exception as e:
            passed = "FAIL"
            My_Log().error(e)
            raise e
        finally:
            # 将接口返回数据写入到excel内
            Do_Excel().result_back(get_path.case_path, item["sheet_name"], item["case_id"]+1, 9, str(res.json()))
            # 将接口是否通过写入到excel内
            Do_Excel().result_back(get_path.case_path, item["sheet_name"], item["case_id"]+1, 10, passed)
            My_Log().info(res.json())


if __name__ == '__main__':
    Test_Http_Api().test_http_api()
