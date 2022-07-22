import json
import unittest
from base.runmethod import RunMethod
import paramunittest
from ddt import ddt, data  # 引入ddt模块
import os
from base import HTMLTestRunner_PY3
#import geturlParams
import urllib.parse
# import pythoncom
from util.operation_excel import OperationExcel
# pythoncom.CoInitialize()
import pytest
#url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
login_xls = OperationExcel().get_xls("case1.xls","Sheet2")

@paramunittest.parametrized(*login_xls)
class TestUserLogin(unittest.TestCase):
    def setParameters(self, id, url, method,data):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.id= str(id)
        self.url = str(url)
        self.data = str(data)
        self.method = str(method)
    def setUp(self):
        print("测试开始前准备")
    def test_01case(self):
         self.checkResult()
    def tearDown(self):
       print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        #url1 = "http://www.xxx.com/login?"
        #new_url = url1 + self.query
       # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMethod().run_main(self.url, self.method,self.data)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)# 将响应转换为字典格式
        """if self.id == 1:# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.id == 2:# 同上
            self.assertEqual(ss['code'], -1)
        if self.id == 3:# 同上
            self.assertEqual(ss['code'], 10001)"""



