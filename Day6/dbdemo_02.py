#dbdemo_02.py (SELECT)

import sqlite3, os

con = sqlite3.connect('user.db')
cursor = con.cursor()

# DML - CRUD(INSERT, SELECT, UPDATE, DELETE) # SELECT 결과의 반환값은 결과집합.
sql1 = 'SELECT * FROM tblAddr WHERE name=\'박상용\' or addr=\'부산시\''

cursor.execute(sql1)
# fetch - SELECT 결과 집합에 대해서 몇 개 만큼 사용할 것인지 결정
# fetchall() - 전체
# fetchone() - 하나
# fetchmany() - 일부
# table = cursor.fetchall() 

# <class 'list'>
# [('박상용', '010-4661-7166', '서울시 성북구'), ('홍길동', '010-2351-0896', '부산시')]

while True:
    row = cursor.fetchone()
    if row == None:
        break
    # print('이름: {0}, 전화번호: {1}, 주소: {2}'.format(row[0],row[1],row[2]))
    print('이름:%s, 전화번호:%s, 주소:%s' % (row[0],row[1],row[2]))
    # print('이름:%s, 전화번호:%s, 주소:%s' % row)

print('-------------- execute update -------------------------')
updateSql = "UPDATE tblAddr SET addr='서울' WHERE name='홍길동'"
cursor.execute(updateSql)
con.commit()

# print(type(table))
# print(table)

# 변경사항이 없기 때문에 commit은 사용안해도 됨.
cursor.close()
con.close()