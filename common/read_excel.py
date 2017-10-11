import xlrd
import json

class Read_Excel():

	def __init__(self,path,sheet_name):

		self.path=path
		self.sheet_name=sheet_name

	#打开excel表格
	def open_excel(self):

		self.workbook=xlrd.open_workbook(self.path)

	#获取标签页
	def get_sheet_table(self):

		table=self.workbook.sheet_by_name(self.sheet_name)
		return table
	
	#获取行号
	def get_nrows(self,table):

		nrows=table.nrows
		return nrows
	
	#获取列号
	def get_ncols(self,table):

		ncols=table.ncols
		return ncols
		
	#获取用例名称
	def get_test_name(self,table,nrows):

		test_name=[]
		for i in range(1,nrows):
			test_name.append(table.row_values(i)[0])
		return test_name

	#获取请求方法
	def get_test_method(self,table,nrows):

		test_method=[]
		for i in range(1,nrows):
			test_method.append(table.row_values(i)[1])
		return test_method

	#获取url
	def get_test_url(self,table,nrows):

		test_url=[]
		for i in range(1,nrows):
			test_url.append(table.row_values(i)[2])
		return test_url	
	#获取参数
	def get_test_data(self,table,nrows):

		test_data=[]
		for i in range(1,nrows):
			test_data.append(table.row_values(i)[3])
		return test_data

	#获取状态码
	def get_test_code(self,table,nrows):

		test_code=[]
		for i in range(1,nrows):
			test_code.append(table.row_values(i)[4])
		return test_code

	#获取期望结果
	def get_except_result(self,table,nrows):

		except_result=[]
		for i in range(1,nrows):
			except_result.append(table.row_values(i)[5])
		return except_result


