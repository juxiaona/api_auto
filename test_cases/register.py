import sys
sys.path.append('../')
from common.read_data import ReadExcel
from common.logger import Log
import unittest
import requests
import ddt
import json 

testdata=ReadExcel('../data/smile_tasks.xlsx', 'register').data_dict()

@ddt.ddt
class Register(unittest.TestCase):

	def setUp(self):

		self.log=Log()

	@ddt.data(*testdata)
	def test_register(self,data):

		post_data={'username':data['username'],'password':data['password'],'password_confirmation':data['password_confirmation']}
		self.log.info('----register test start----')

		if data['mothod']=='post':
			r=requests.post(data['url'],data=post_data)
			result=r.json()

		if r.status_code==200:
			
			try:
				self.assertEqual(data['username'], result['username'])
			except Exception as e:
				self.log.error(e)

		elif r.status_code==400:
			
			try:
				self.assertEqual(int(data['code']), result['code'])
				self.assertEqual(data['msg'], result['msg'])
			except Exception as e:
				self.log.error(e)

		self.log.info('----register test end----')

	def tearDown(self):
		pass

if __name__ == '__main__':
	 unittest.main()
