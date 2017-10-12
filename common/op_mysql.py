import sys
sys.path.append('../')
import pymysql
from config import read_config
from common.logger import Log

class Op_Mysql():

	def __init__(self):

		self.host=read_config.mysql_host
		self.user=read_config.mysql_user
		self.pasw=read_config.mysql_pasw
		self.port=read_config.mysql_port
		self.database=read_config.database
		self.log=Log()

	def db_conn(self):

		#config={'host':self.host,'user':self.user,'passwd':self.pasw,'port':self.port,'db':self.database}
		try:
			self.conn=pymysql.connect(self.host,self.user,self.database)
			#self.conn=pymysql.connect('127.0.0.1','root','','test_db')
			self.cusor=self.conn.cursor()
			self.log.info('database connect successfully')
		except ConnectionError as e:
			self.log.error(e)

	def test(self):
		print(self.host)
		print(self.user)
		print(self.pasw)
		print(self.port)
		print(self.database)
if __name__ == '__main__':
	
	op=Op_Mysql()
	op.test()
	op.db_conn()
		

