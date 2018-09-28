#dbdemo_01.py
import sqlite3

con = sqlite3.connect('user.db')  ## sqlite3.connect('db이름') --> 연결해서 객체 반환
cursor = con.cursor() ## con 객체를 기반으로 cursor 객체 반환

print(con,"연결 성공")
cursor.execute("DROP TABLE IF EXISTS tblAddr") # info 테이블이 존재하는 경우에만 삭제
cursor.execute("""CREATE TABLE tblAddr(
    name CHAR(10) PRIMARY KEY, 
    phone CHAR(15),
    addr TEXT
    )""")
    # PRIMARY KEY - 식별자로 중복된 내용이 올 수 없다.
print("테이블 생성 성공")

cursor.execute("""INSERT INTO tblAddr VALUES('박상용','010-4661-7166','서울시 성북구') """) # 데이터 삽입
cursor.execute("""INSERT INTO tblAddr VALUES('홍길동','010-2351-0896','부산시') """) # VALUES 안에는 ' '만 사용
print("데이터 추가 성공")

con.commit()
cursor.close()
con.close()