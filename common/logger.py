import logging
import time
import os

#获取当前路径
cur_path=os.path.dirname(os.path.realpath(__file__))
#存放log的路径
log_path=os.path.join(os.path.dirname(cur_path),'logs')
#如果不存在logs文件夹，自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class Log():

	def __init__(self):

		#日志文件的名称
		self.logname=os.path.join(log_path,'%s.log'%time.strftime('%Y-%m-%d-%H-%M'))
		#创建一个logger
		self.logger=logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		#定义日志的输出格式
		self.formatter=logging.Formatter('[%(asctime)s]-%(filename)s]-%(levelname)s:%(message)s')

	 # 创建一个FileHandler，用于写到本地		
	def file_handler_console(self,level,msg):

		self.fh=logging.FileHandler(self.logname,'a')
		self.fh.setLevel(logging.DEBUG)
		self.fh.setFormatter(self.formatter)
		self.logger.addHandler(self.fh)

		if level=='info':
			self.logger.info(msg)
		elif level=='debug':
			self.logger.debug(msg)
		elif level=='warning':
			self.logger.warning(msg)
		elif level=='error':
			self.logger.error(msg)

		#为了避免日志输出重复
		self.logger.removeHandler(self.fh)
		self.fh.close()

	def debug(self,msg):

		self.file_handler_console('debug', msg)

	def info(self,msg):

		self.file_handler_console('info', msg)

	def warning(self,msg):

		self.file_handler_console('warning', msg)

	def error(self,msg):

		self.file_handler_console('error', msg)


