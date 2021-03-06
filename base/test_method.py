#coding:utf-8
import unittest
import json
from base import  HTMLTestRunner
from base import HTMLTestRunner_PY3
from mock import mock
from unittest import mock, TestSuite
#from runmethod import RunMethod
from base.demo import RunMain
import time
from base.mock_demo import mock_test
import os
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
		#self.run.run_main = mock.Mock(return_value=data)
		res = mock_test(self.run.run_main,data,url,"POST",data)
		#res = self.run.run_main(url,'POST',data)

		print(res)
		#print(mock_test(self.run.run_main,data,url,"POST",data))
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

if __name__ == '__main__':
	unittest.main()
