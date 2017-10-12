import sys
sys.path.append('../')
import requests
import unittest
import ddt
from common.read_data import ReadExcel
from common.logger import Log

testdata=ReadExcel('../data/test_cases.xlsx','config').data_dict()

@ddt.ddt
class Ads_config(unittest.TestCase):

	def setUp(self):
		self.log=Log()

	@ddt.data(*testdata)	
	def test_get_config(self,data):

		self.log.info('----start----')
		r=requests.request(data['mothod'], data['url'])
		self.log.info(data['url'])
		try:
			if r.status_code==int(data['status_code']):

				self.assertEqual(len(r.json()),int(data['except_data']))

		except:
			print('test failed')
		self.log.info('----end----')

	def tearDown(self):

		pass 

if __name__ == '__main__':
	
	unittest.main()

