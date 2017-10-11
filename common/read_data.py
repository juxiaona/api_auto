import xlrd

class ReadExcel():

	def __init__(self,excelpath,sheetname):

		self.data=xlrd.open_workbook(excelpath)
		self.table=self.data.sheet_by_name(sheetname)
		#获取第一列作为key
		self.keys=self.table.row_values(0)
		#获取总行数
		self.row_nums=self.table.nrows
		#获取总列数
		self.col_nums=self.table.ncols


	def data_dict(self):

		if self.row_nums<=1:
			print('总行数小于1，请补充数据')

		else:
			L=[]

			for i in range(1,self.row_nums):

				#从第二行开始读取数据
				values=self.table.row_values(i)
				D={}
				for x in range(self.col_nums):
					D[self.keys[x]]=values[x]
				L.append(D)
		return L 

