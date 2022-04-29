import unittest
import HTMLTestRunnerNew
from tools.http_api import Test_Http_Api
from tools import get_path


class Run():


    def run(self):
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(Test_Http_Api))
        with open(get_path.report_path, "wb") as file:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                      verbosity=2,
                                                      title="wepie测试报告",
                                                      description="接口测试报告",
                                                      tester="GXL")
            runner.run(suite)


if __name__ == '__main__':
    Run().run()