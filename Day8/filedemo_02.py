# mysqldemo_02.py (connection)
import pymysql

# 1. connection # mysql(remote) -> url, username, password. 받아올 서버, 사용자 이름, 패스워드, 초기 DB
conn = pymysql.connect(host='127.0.0.1',user='root',password='', db='test_python', charset='utf8') 

cursor = conn.cursor()

inputId = input("아이디를 입력해 주세요->")
inputPwd = input("비밀번호를 입력해 주세요->")

# select sql 작성
# selectSql = 'SELECT * FROM member where id=\'' + inputId + '\' AND pwd=\'' + inputPwd + '\''
# 문자열 조합 방식 - string interpolation 사용 금지. parameter.placeholder 방식 권장
# selectSql = "SELECT * FROM member where id='" + inputId + "'AND pwd='" + inputPwd + "'"
## SQL-injection : inputId에 ' or 1=1 # 를 입력하면, SELECT * FROM member where id='' or 1=1 #'AND pwd='testasdas'로 로그인 확인 쿼리 발생.
## 문자열 조합이 아니라, 입력하고자 하는 값을 parameter로 전달.

selectSql = "SELECT * FROM member where id=%s AND pwd=%s"

print(selectSql)
cursor.execute(selectSql,(inputId,inputPwd))
row = cursor.fetchone()
if row == None:
    print("로그인 실패 : ID나 패스워드가 잘못되었습니다.")
else:
    print("로그인 성공", row)

cursor.close()
conn.close()
