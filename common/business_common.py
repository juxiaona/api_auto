import sys 
sys.path.append('../')
from common.read_excel import Read_Excel
from common.request import Request

class Common():

	def __init__(self):

		self.login_case=Read_Excel('../data/smile_tasks.xlsx', 'login')
		self.login_case.open_excel()
		self.table=self.login_case.get_sheet_table()
		self.ncols=self.login_case.get_ncols(self.table)
		self.login_case_data=self.login_case.get_test_case(self.table,self.ncols)
		self.request=Request()

	
	def login(self):

		method=self.login_case_data['method']
		url=self.login_case_data['url']
		username=self.login_case_data['username']
		password=self.login_case_data['password']
		param={'username':username,'password':password}

		r=self.request.request(method, url, param)
		r_json=r.json()
		token=r_json['token']
		return token




