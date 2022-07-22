# -*- coding: utf-8 -*-
__author__ = 'hd'
__date__ = '2022/7/10 11:50'
import json
import ddt
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.operation_excel import OperationExcel
from util.send_email import SendEmail
from util.send_dingding import sendDing
from util.log1 import logger
import getpathInfo
from BeautifulReport import BeautifulReport
import os
from logging.handlers import TimedRotatingFileHandler
from util.Log import  logging
import util.Log
import unittest
log =util.Log.logger
data=OperationExcel().get_xls("case1.xls","sheet1")
#print(data)

#data = GetData()
com_util = CommonUtil()
op = OperationExcel()
send_mai = SendEmail()
send_din = sendDing()
@ddt.ddt
class RunTest(unittest.TestCase):
    def setUp(self) :
        self.runmin=RunMethod()
    @ddt.data(*data)
    def test_run(self,data):
        res = None
        header = None
        method = data[4]
        data1=data[9]
        url = data[2]
        expect=data[10]
        res = self.runmin.run_main(method, url, data1, header)
        print(method)
        print(res)
       # res1=json.dumps(res)
        #self.assertEqual(expect['uid'],res['status'])
        #print(type(res))
    def tearDown(self):
        pass
     #return res
if __name__ == '__main__':
    unittest.main()

    """case_path = "C:/Users/admin/Desktop/api_test/main"
    report_path = "C:/Users/admin/Desktop/api_test/report"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run4.py")
    result = BeautifulReport(discover)
    result.report(filename='测试报告', description='自动化测试报告', report_dir=report_path,
              theme='theme_default')"""
