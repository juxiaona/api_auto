import sys
sys.path.append('../')
from common.request import Request
from common.business_common import Common
from common.logger import Log
import unittest

class CreateTasks(unittest.TestCase):

	def setUp(self):

		self.log=Log()
		self.common=Common()
		self.request=Request()

	def test_create_task(self):

		method='post'
		url='http://139.199.192.100:3000/api/tasks'
		param={'title':'test','desc':'12345'}
		token=self.common.login()
		header={'Authorization':'Bearer '+token}
		r=self.request.request(method, url, param,header)
		print(r.json())

	def tearDown(self):
		pass

if __name__ == '__main__':

	unittest.main()
	
