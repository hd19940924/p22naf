# -*- coding: utf-8 -*-
__author__ = 'hd'
__date__ = '2022/7/10 11:50'
import sys
sys.path.append("/root/.jenkins/workspace/自动化测试")
import json
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.operation_excel import OperationExcel
from util.send_email import SendEmail
from util.send_dingding import sendDing
from util.log1 import logger
import getpathInfo
import os
from logging.handlers import TimedRotatingFileHandler
from util.Log import  logging
import util.Log
import sys
sys.path.append("/root/.jenkins/workspace/自动化测试")
log =util.Log.logger
class RunTest(object):
    def __init__(self):#构造内部函数，进行实例化，以便调用
        self.runmin = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.op=OperationExcel()
        self.send_mai = SendEmail()
        self.send_din=sendDing()
       # log.info()  #
        #log.info()  #
        #log.info()  #
    def run(self):
        res = None
        pass_count = []
        fail_count = []
        row_counts = self.data.get_case_lines()  # 获取excel表格行数
        #print(row_counts) #5
        for i in range(1, 10):#for循环遍历达到参数化接口测试
            print(i)# 1,2,3,4
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            #expect = self.data.get_expcet_data_for_mysql(i)
            expect = self.data.get_expcet_data(i)
            header = self.data.is_header(i)
            log.info("第{0}条case测试开始".format(i))
            log.info("url:"+url)
            log.info('method:' +method)
            #log.info('is_run:'+is_run)
            log.info('data:'+json.dumps(data))
            #log.info('header:'+header)
            log.info("expect:"+expect)
            logger.warning('颜色')
            logger.error('error')
            logger.info("ppp")
            logger.critical('critical')
            #log.info("第{0}条case测试结束".format(i))
            print('url:', url)
            print('method:', method)
            print('is_run:', is_run)
            print('data:', data)
            print('header:', header)
            print("expect:",expect)
            """print(type(expect))
            print(type(data))
            print(type(res))"""
            if is_run:
                res = self.runmin.run_main(method, url, data, header)
               # print(res[2])
                print(res)
                #print(type(res))
                #log.info(res)
                if self.com_util.is_contains(expect, res):
                  print("测试通过")
                  log.info("测试通过")
                  pass_count.append("success")
                  self.data.write_result(i, 'pass')#写入测试结果
                  pass_count.append("success")
                else:
                  #print("测试失败")
                  print("\033[31m测试失败\033[0m")
                  log.info("测试失败")
                  log.info("第{0}条case测试结束".format(i))
                  log.info(
                      "========================================================================================================================")
                  self.data.write_result(i, 'fail')#写入测试结果
                  fail_count.append("fail")
        print("pass:",(len(pass_count)))#统计通过的结果数
        print("fail:",(len(fail_count)))#统计失败
        #m.send_email()
        #self.send_mai.send_main(pass_count, fail_count)#邮件发送测试结果
       # self.send_din.Send_Ding(pass_count, fail_count)#钉钉发送测试结果


        #return res
if __name__ == '__main__':
    run=RunTest()
    print(run.run())
