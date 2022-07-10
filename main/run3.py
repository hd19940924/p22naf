# -*- coding: utf-8 -*-
__author__ = 'cdtaogang'
__date__ = '2019/6/21 11:57'
import json
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.operation_excel import OperationExcel
class RunTest(object):
    def __init__(self):
        self.runmin = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.op=OperationExcel()
    def run(self):
        res = None
        pass_count = []
        fail_count = []
        row_counts = self.data.get_case_lines()  # 获取excel表格行数
        #print(row_counts) #5
        for i in range(1, row_counts):
            print(i)# 1,2,3,4
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            #expect = self.data.get_expcet_data_for_mysql(i)
            expect = self.data.get_expcet_data(i)
            header = self.data.is_header(i)

            print('url:', url)
            print('method:', method)
            print('is_run:', is_run)
            print('data:', data)
            print('header:', header)
            print("expect:",expect)
            if is_run:
                res = self.runmin.run_main(method, url, data, header)
               # print(res[2])
                print(res)
                if self.com_util.is_contains(expect,res):
                    print("测试通过")
                    self.data.write_result(i, 'pass')
                    #pass_count.append(i)
                else:
                    print("测试失败")
                    self.data.write_result(i, 'fail')
                    #fail_count.append(i)

        #return res
if __name__ == '__main__':
    run=RunTest()
    print(run.run())