#coding:utf-8
import unittest
import json
#from base import  HTMLTestRunner
#from base import HTMLTestRunner_PY3
from mock import mock
from unittest import mock
#from runmethod import RunMethod
from base.demo import RunMain
from base.mock_demo import mock_test
class TestMethod(unittest.TestCase):
	def setUp(self):
		self.run=RunMain()
	def test_03(self):
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp':'1507034803124',
			'uid':'5249191',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd37ddd5efeb04aa591ec12',
			'token':'7d6f14f21ec96d755de41e6c076758dd',
			'cid':'0',
			'errorCode':1001
		}
		mock_data=mock.Mock(return_value=data)
		self.run.run_main=mock_data
		#self.run.run_main = mock.Mock(return_value=data)
		res = mock_test(self.run.run_main,data,url,"POST",data)
		print(res)
		#res = self.run.run_main(url,'POST',data)

		#print(res)
		self.assertEqual(res['errorCode'],1001,"测试失败")
		print ("这是第一个case")

	#@unittest.skip('test_02')	
	def test_02(self):
		
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp':'1507034803124',
			'uid':'5249191',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd37ddd5efeb04aa591ec12',
			'token':'7d6f14f21ec96d755de41e6c076758dd',
			'cid':'0'
		}

		res = self.run.run_main(url,'POST',data)
		self.assertEqual(res['errorCode'],1001,"测试失败")
		print("这是第二个case")
		#mock
	"""def test_03(self):
		url="https://www.baidu.com/sugrec?pre=1&p=3&ie=utf-8&json=1&prod=pc&from=pc_web&wd=111&bs=111&pbs=111&csor=3&pwd=111&cb=jQuery110204119675480574152_1657349414365&_=1657349414371"
		data={}
		res=self.run.run_main(url,"get",data)"""

if __name__ == '__main__':
	unittest.main()