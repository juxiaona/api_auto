import sys
sys.path.append('../')
from common.read_data import ReadExcel
from common.logger import Log
import unittest
import requests
import ddt
from common.request import Request

#读取Excel中的数据
testdata=ReadExcel('../data/smile_tasks.xlsx', 'register').data_dict()

#使用数据驱动
@ddt.ddt
class Register(unittest.TestCase):

	def setUp(self):

		self.log=Log()
		self.request=Request()


	@ddt.data(*testdata)
	def test_register(self,data):

		#获取请求方法
		post_method=data['method']
		#获取请求的URL
		post_url=data['url']
		#需要传递的参数
		post_data={'username':data['username'],'password':data['password'],'password_confirmation':data['password_confirmation']}
		#记录日志
		self.log.info('----register test start----')

		#请求
		r=self.request.request(post_method,post_url,post_data)
		result=r.json()

		#断言
		if r.status_code==200:
			
			try:
				self.assertEqual(data['username'], result['username'])
			except Exception as e:
				raise e

		elif r.status_code==400:
			
			try:
				self.assertEqual(int(data['code']), result['code'])
				self.assertEqual(data['msg'], result['msg'])
			except Exception as e:
				raise e

		self.log.info('----register test end----')

	def tearDown(self):
		pass

if __name__ == '__main__':
	 unittest.main()
