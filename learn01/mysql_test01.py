import pymysql
try:
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='root', database='test')
except pymysql.Error as e:
    print("数据库操作失败：" + str(e))
else:
    # 使用cursor()方法创建一个游标对象
    cursor = conn.cursor()
    # 使用execute()方法执行SQL查询
    sql = 'select * from user'
    cursor.execute(sql)
    # 使用fetchone()方法获取单条数据
    one = cursor.fetchone()
    # 打印
    print('first user: %s' %str(one))

    # 使用execute()方法执行SQL，如果表存在则将其删除
    cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
    # 使用预处理语句创建表
    sql = """CREATE TABLE `employee` (
      `first_name` varchar(255) DEFAULT NULL COMMENT '姓',
      `last_name` varchar(255) DEFAULT NULL COMMENT '名',
      `age` int(11) DEFAULT NULL COMMENT '年龄',
      `sex` varchar(255) DEFAULT NULL COMMENT '性别',
      `income` varchar(255) DEFAULT NULL COMMENT '收入'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    # 执行SQL语句
    result = cursor.execute(sql)
    print("create table employee result is :  "+ str(result))

    # SQL 插入语句
    sql = "insert into employee(first_name, \
           last_name, age, sex, income) \
           values ('%s', '%s', %s, '%s', %s )" % \
          ('mac', 'mohan', 20, 'm', 2000)

    try:
        result = cursor.execute(sql)
        result = cursor.execute(sql)
        result = cursor.execute(sql)
        result = cursor.execute(sql)
        print("insert into table employee result is :  "+ str(result))
    except pymysql.Error as e:
        print(e)
        conn.rollback()

    # SQL 查询语句
    sql = "select * from employee \
           where income > %s" % (1000)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print(
                "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                (fname, lname, age, sex, income)
            )
    except:
        print("Error: unable to fecth data")

    # SQL 更新语句
    sql = "update employee set age = age + 1 where sex = '%c'" % ('m')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()

    #关闭连接
    conn.close()