import sqlalchemy as sqla
import pymysql
import pandas as pd


# 定义从数据库读取数据转换成dataframe函数
def sql_query(sql):
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='my_test', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    columnDes = cursor.description  # 获取连接对象的描述信息
    cursor.close()
    conn.close()
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    results = pd.DataFrame([list(i) for i in results], columns=columnNames)
    return results


# 编写sql语句并保存执行结果
sql2 = "select * from data"
result1 = sql_query(sql2)
print(result1)

# 将dataframe数据写入数据库
engine = sqla.create_engine('mysql+pymysql://root:123456@localhost:3306/my_test')
result1.to_sql('data',con=engine, index=False, if_exists='replace')

