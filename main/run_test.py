#coding:utf-8
import sys
sys.path.append("C:/Users/admin/Desktop\p22naf")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
from util.ding2 import sendDing
class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommonUtil()
		self.send_mai = SendEmail()
		self.send_din = sendDing()

	#程序执行的
	def go_on_run(self):
		res = None
		pass_count = []
		fail_count = []
		#10  0,1,2,3
		rows_count = self.data.get_case_lines()
		for rows_count in range(1,9):
			is_run = self.data.get_is_run(rows_count)
			if is_run:
				url = self.data.get_request_url(rows_count)
				method = self.data.get_request_method(rows_count)
				request_data = self.data.get_data_for_json(rows_count)
				#expect = self.data.get_expcet_data_for_mysql(i)
				expect=self.data.get_expcet_data(rows_count)
				header = self.data.is_header(rows_count)
				depend_case = self.data.is_depend(rows_count)
				#print("url：",url)
				#print("method",method)
				#if is_run:
					#res=self.run_method.run_main(url,method,data,header)"""
				if depend_case != None:
					self.depend_data = DependdentData(depend_case)
					#获取的依赖响应数据
					depend_response_data = self.depend_data.get_data_for_key(rows_count)
					#获取依赖的key
					depend_key = self.data.get_depend_field(rows_count)
					request_data[depend_key] = depend_response_data
				if header == 'write':
					res = self.run_method.run_main(method,url,request_data)
					op_header = OperationHeader(res)
					op_header.write_cookie()

				elif header == 'yes':
					op_json = OperetionJson('../dataconfig/cookie.json')
					cookie = op_json.get_data('apsid')
					cookies = {
						'apsid':cookie
					}
					res = self.run_method.run_main(method,url,request_data,cookies)
				else:
					res = self.run_method.run_main(method,url,request_data)

				if self.com_util.is_equal_dict(expect,res) == 0:
					self.data.write_result(rows_count,'pass')
					pass_count.append(rows_count)
				else:
					self.data.write_result(rows_count,res)
					fail_count.append(rows_count)
		self.send_mai.send_main(pass_count,fail_count)
		self.send_din.Send_Ding(pass_count, fail_count)  # 钉钉发送测试结果


	#将执行判断封装
	#def get_cookie_run(self,header):


if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()

