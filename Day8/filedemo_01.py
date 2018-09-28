# mysqldemo_01.py (connection)
import pymysql

# 1. connection # mysql(remote) -> url, username, password. 받아올 서버, 사용자 이름, 패스워드, 초기 DB
conn = pymysql.connect(host='127.0.0.1',user='root',password='', db='test_python', charset='utf8') 

cursor = conn.cursor()


# insert member(idx, id, pwd, name, reg_data)
# ('admin', '1234', 'Administrator', NOW())   NOW() : 현재 날짜 값을 나타내는 mysql 함수
# insertSql = """INSERT INTO member(id, pwd, name, reg_date) VALUES(
#     'admin', '1234' , 'Administrator' , NOW()
# )"""
# hp'computer


insertSql = """INSERT INTO member(id, pwd, name, reg_date) VALUES(%s, %s , %s , NOW())""" 
cursor.execute(insertSql, ('user1', '1234', 'TEST\'s USER')) ## 파라미터 전달 방식. SQL-injection 문제 우회. 특수문자 사용.
conn.commit()

# SelectSQL
selectSql = 'SELECT * FROM member'
cursor.execute(selectSql)
data = cursor.fetchall()

for row in data:
    print(row)


conn.close()
# 2. Cursor

# 3. Execute SQL

# 4. Select -> fetch()

# 5. Close