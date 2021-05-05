import pymysql
import redis
import json

try:
    # 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', password='root', database='test')
    cursor = db.cursor()
except pymysql.Error as e:
    print("数据库操作失败：" + str(e))

sql = "select * from employee"
cursor.execute(sql)
employees = cursor.fetchall()
print(employees)
db.close()

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('name', 'runoob')
name = str(r.get('name'), 'utf-8')
print(name)
r.set('employee', json.dumps(employees))
employeeJson = str(r.get('employee'), 'utf-8')
print(employeeJson)
employeeJsonToDecode = json.loads(employeeJson)
print(employeeJsonToDecode)
print(tuple(employeeJsonToDecode))