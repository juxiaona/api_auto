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

		config={
			'host':self.host,
			'user':self.user,
			'passwd':'',
			'port':int(self.port),
			'db':self.database
			}

		try:
			self.db=pymysql.connect(**config)
			self.cursor=self.db.cursor()
			self.log.info('database connect successfully')
		except ConnectionError as e:
			self.log.error(e)

	def execute_sql(self,sql):

		self.db_conn()

		try:
			self.cursor.execute(sql)
			self.db.commit()
			self.log.info('execute sql: (%s) successfully' %sql)

		except Exception as e:
			self.log.error(e)
		
		return self.cursor

	def get_all(self,sql):

		cur=self.execute_sql(sql)
		result=cur.fetchall()
		return result

	def get_one(self,sql):

		cur=self.execute_sql(sql)
		result=cur.fetchone()
		return result

	def db_close():

		self.db.close()
		self.log.info('db close')


		

