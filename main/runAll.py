#from case.chandaologin2 import login
#from HTMLyy.HTMLYY import HTMLTestRunner
from testcase.testcase01 import TestUserLogin
from base import HTMLTestRunner_PY3
import unittest
import time
if __name__ == '__main__':
    print(type(TestUserLogin))
    suite =unittest.TestSuite()
    #tests=[TestUserLogin("test_01case")]
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestUserLogin))
    #suite.addTests(TestUserLogin("test_01case"))
    #suite.addTests(tests)
    a =time.strftime("%Y-%m-%d %H_%M_%S")
    #fp="//report/(a+"result.html")
    #fp='./report/' + a + '_result.html'
    fp="C:/Users/admin/PycharmProjects/test_interface/report/"+a+'_result.html'
    with open(fp, 'w',encoding="utf-8",errors='ignore') as f:
               runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f,
                                title='测试报告',
                                description='测试用例的执行情况',
                                verbosity=2,

                                )
               runner.run(suite)