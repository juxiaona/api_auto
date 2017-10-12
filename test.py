from common.op_mysql import Op_Mysql

op=Op_Mysql()
sql="insert into user values(7,'jxn');"
op.execute_sql(sql)
sql1='select * from user;'
result=op.get_all(sql1)
print(result)