import sys
sys.path.append('../')
from common.logger import Log
from common.read_data import ReadExcel
import unittest
import ddt
from common.request import Request

#读取excel 中的数据
testdata=ReadExcel('../data/smile_tasks.xlsx', 'login').data_dict()


#数据驱动
@ddt.ddt
class Login(unittest.TestCase):

	def setUp(self):

		self.log=Log()
		self.request=Request()

	@ddt.data(*testdata)
	def test_login(self,data):

		#获取requests 的post/get方法
		post_method=data['method']
		#获取需要提交的参数
		post_data={'username':data['username'],'password':data['password']}
		#获取请求的url
		post_url=data['url']
		#获取请求头
		post_header={}
		#记录日志
		self.log.info('----login %s start----' %data['testname'])

		#请求
		r=self.request.request(post_method,post_url,post_data)
		result=r.json()

		#断言
		if r.status_code==200:

			try:
				self.assertEqual(result['username'], data['username'])
			except Exception as e:
				raise e
				

		elif r.status_code==400:

			try:
				self.assertEqual(str(result['code']), data['code'])
				self.assertEqual(result['msg'], data['msg'])
			except Exception as e:
				raise e
				

		elif r.status_code==401:
			try:
				self.assertEqual(str(result['code']), data['code'])
				self.assertEqual(result['msg'], data['msg'])
			except Exception as e:
				raise e
				
		self.log.info('----login %s end----' %data['testname'])


	def tearDown(self):
		pass


if __name__ == '__main__':
	 
	 unittest.main()