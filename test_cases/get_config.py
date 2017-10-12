import sys
sys.path.append('../')
from common.read_excel import Read_Excel
import unittest
import requests
from common.logger import Log

class Read_Cases(unittest.TestCase):

	def setUp(self):
		
		get_config=Read_Excel('../data/test_cases.xlsx', 'config')
		get_config.open_excel()
		self.table=get_config.get_sheet_table()
		self.nrows=get_config.get_nrows(self.table)
		self.ncols=get_config.get_ncols(self.table)
		self.test_name=get_config.get_test_name(self.table,self.nrows)
		self.test_mothod=get_config.get_test_method(self.table,self.nrows)
		self.test_url=get_config.get_test_url(self.table, self.nrows)
		self.test_data=get_config.get_test_data(self.table, self.nrows)
		self.status_code=get_config.get_test_code(self.table, self.nrows)
		self.except_result=get_config.get_except_result(self.table, self.nrows)
		self.log=Log()

	def test_read(self):

		for i in range(self.nrows-1):
			self.log.info('---start----')
			r=requests.request(self.test_mothod[i], self.test_url[i])

			try:
				if str(r.status_code)==self.status_code[i]:
					self.assertEqual(len(r.json()),int(self.except_result[i]))
					print('pass')
			except :
				print('test failed')

	def tearDown(self):
		pass

if __name__ == '__main__':
	
	unittest.main()