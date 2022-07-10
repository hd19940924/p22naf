import sys
#sys.path.append("C:/Users/admin/Desktop\p22naf")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mai = SendEmail()
    def go_on_run(self):
        res =  None
        #rows_count = self.data.get_case_lines()
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                is_run = self.data.get_is_run(i)
                data = self.data.get_data_for_json(i)
                # expect = self.data.get_expcet_data_for_mysql(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                res = self.run_method.run_main(method, url, data, header)
                # print(res)
            return res
if __name__ == '__main__':
    run=RunTest()
    print(run.go_on_run())
