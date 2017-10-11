import logging
import time
import os

#获取当前路径
cur_path=os.path.dirname(os.path.realpath(__file__))
#存放log的路径
log_path=os.path.join(os.path.dirname(cur_path),'logs')
#如果不存在logs文件夹，自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)
