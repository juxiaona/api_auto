import sys
sys.path.append('../')
from common.logger import Log
from common.read_data import ReadExcel
import unittest
import ddt
import requests

testdata=ReadExcel('../data/smile_tasks.xlsx', 'login').data_dict()

@ddt.ddt
class Login(unittest.TestCase):

	def setUp(self):

		self.log=Log()

	@ddt.data(*testdata)
	def test_login(self,data):

		post_data={'username':data['username'],'password':data['password']}

		self.log.info('----login test start----')

		if data['method']=='post':
			r=requests.post(data['url'],data=post_data)
			result=r.json()

		if r.status_code==200:

			try:
				self.assertEqual(result['username'], data['username'])
			except Exception as e:
				self.log.error(e)

		elif r.status_code==400:

			try:
				self.assertEqual(str(result['code']), data['code'])
				self.assertEqual(result['msg'], data['msg'])
			except Exception as e:
				self.log.error(e)

		elif r.status_code==401:
			try:
				self.assertEqual(str(result['code']), data['code'])
				self.assertEqual(result['msg'], data['msg'])
			except Exception as e:
				self.log.error(e)

		self.log.info('----login test end----')


	def tearDown(self):
		pass


if __name__ == '__main__':
	 
	 unittest.main()