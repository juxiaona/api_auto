import sys
sys.path.append('../')
from common.request import Request
from common.business_common import Common
from common.logger import Log
from common.read_data import ReadExcel
import unittest
import ddt

#读取Excelsmile_tasks 中createtask sheet的内容
testdata=ReadExcel('../data/smile_tasks.xlsx', 'createtask').data_dict()

@ddt.ddt
class CreateTasks(unittest.TestCase):

	def setUp(self):

		self.log=Log()
		self.common=Common()
		self.request=Request()

	@ddt.data(*testdata)
	def test_create_task(self,data):

		#获取请求方法
		method=data['method']
		#获取请求URL
		url=data['url']
		#获取请求参数
		desc=data['desc']
		title=data['title']
		param={'title':title,'desc':desc}
		#获取token
		token=self.common.login()
		header={'Authorization':'Bearer '+token}
		#记录日志
		self.log.info('----createtask test start----')
		#请求
		r=self.request.request(method, url, param,header)
		r_json=r.json()

		#断言
		if data['result']==1:
			try:
				self.assertEqual(r_json['desc'], data['desc'])
				self.assertEqual(r_json['title'], data['title'])
			except Exception as e:
				raise e
		elif data['result']==0:
			try:
				self.assertEqual(r_json['msg']['name'], 'SequelizeValidationError')
			except Exception as e:
				raise e
		self.log.info('----createtask test end----')

	def tearDown(self):
		pass

if __name__ == '__main__':

	unittest.main()
	
