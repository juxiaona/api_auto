import sys 
sys.path.append('../')
from common.read_excel import Read_Excel
from common.request import Request
from common.logger import Log

class Common():

	def __init__(self):

		#打开用例获取login_sheet 中的第一行用例		
		self.login_case=Read_Excel('../data/smile_tasks.xlsx', 'login')
		self.login_case.open_excel()
		self.table=self.login_case.get_sheet_table()
		self.ncols=self.login_case.get_ncols(self.table)
		self.login_case_data=self.login_case.get_test_case(self.table,self.ncols)
		#定义一个request
		self.request=Request()
		#定义log
		self.log=Log()

	
	def login(self):

		#request所需要的参数
		method=self.login_case_data['method']
		url=self.login_case_data['url']
		username=self.login_case_data['username']
		password=self.login_case_data['password']
		param={'username':username,'password':password}

		#发送请求
		try:
			r=self.request.request(method, url, param)
			r_json=r.json()
			token=r_json['token']
		except:
			self.log.error('get token failed')

		return token




