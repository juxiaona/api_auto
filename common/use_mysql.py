import sys
sys.path.append('../')
import pymysql
from config import read_config
from common.logger import Log

class Op_Mysql():

	def __init__(self):

		#从配置文件读取MySQL的信息
		self.host=read_config.mysql_host
		self.user=read_config.mysql_user
		self.pasw=read_config.mysql_pasw
		self.port=read_config.mysql_port
		self.database=read_config.database
		self.log=Log()

	def db_conn(self):

		#组合connect参数
		config={
			'host':self.host,
			'user':self.user,
			'passwd':'',
			'port':int(self.port),
			'db':self.database
			}

		try:
			#打开一个数据库连接
			self.db=pymysql.connect(**config)
			#创建一个游标
			self.cursor=self.db.cursor()
			#记录日志
			self.log.info('database connect successfully')
		except ConnectionError as e:
			self.log.error(e)

	#执行sql语句
	def execute_sql(self,sql):

		self.db_conn()

		try:
			self.cursor.execute(sql)
			self.db.commit()
			self.log.info('execute sql: (%s) successfully' %sql)

		except Exception as e:
			self.log.error(e)
		
		return self.cursor

	#获取全部数据
	def get_all(self,sql):

		cur=self.execute_sql(sql)
		result=cur.fetchall()
		return result

	#获取一条数据
	def get_one(self,sql):

		cur=self.execute_sql(sql)
		result=cur.fetchone()
		return result

	#关闭数据库连接
	def db_close():

		self.db.close()
		self.log.info('db close')


		

