import pymysql
from tools import get_path
from tools.do_config import Do_Config
from tools.my_log import My_Log


class Do_Mysql():

    def do_mysql(self, sql, state=1):
        global res
        # 数据库连接信息
        db_config = eval(Do_Config.do_config(get_path.conf_path, "DB", "db_config"))
        # 创建数据库连接
        conn = pymysql.connect(**db_config)
        # 创建数据库游标
        cur = conn.cursor()
        # 执行sql语句
        cur.execute(sql)
        if state == 1:
            res = cur.fetchone()
        elif state == "all":
            res = cur.fetchall()
        else:
            My_Log().error("state报错：{0}".format(state))

        # 关闭数据库连接
        cur.close()
        conn.close()

        return res


if __name__ == '__main__':
    sql = "select ID,nickname from t_user where phone = 14731650116"
    res = Do_Mysql().do_mysql(sql, "all")[0][0]
    print(type(res))
