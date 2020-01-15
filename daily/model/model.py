import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    database='blog',
    password='123456',
    charset='utf8'
)


