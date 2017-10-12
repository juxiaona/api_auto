import sys
sys.path.append('../')
import unittest
import requests
from common.logger import Log

class Baidu(unittest.TestCase):

	def setUp(self):
		self.log=Log()

	def tearDown(self):
		pass

	def test_baidu(self):
		self.log.info('----start----')
		r=requests.get('http://www.baidu.com')
		self.log.info('----end----')

if __name__ == '__main__':
	
	unittest.main()