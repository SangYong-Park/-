""" 성적관리 어플리케이션
[입력, 전체출력, 검색]
입력
 1. 사용자로부터 [이름, 국어, 영어, 수학] 성적 입력
    - 3명 사용자 입력
    - dictionrary로 관리
       ex) 
           sungjuk = {
               '홍길동' : [100, 100, 90],
               '박민지' : [100, 100, 90],
               '김유신' : [100, 100, 90]
           }

           sungjuk = {}
           sungjuk['name'] = [---]
전체출력
    1. 전체 데이터를 성적순으로 출력
검색 
    1. 사용자 이름 입력해서 조회
"""    


import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='',
db='test_python', charset='utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor) 
# array_base cursor[list]] : 어떤 파라미터도 주지 않으면, 커서는 리스트 형태로만 사용 가능. 
# conn.cursor(pymysql.cursors.DictCursor)      --> dictionary(key,value)로 바꿀 수 있음

def displaySungjuk(searchUser):
    rows = selectList(searchUser)
    for row in rows:
        # print("%s\t%s\t%s\t%s\t%s\t%s" % (row[1],row[2],row[3],row[4],row[5],row[6]))
        print("%s\t%s\t%s\t%s\t%s\t%s" % (row['name'],row['kor'],row['eng'],row['mat'],row['total'],row['average']))

def selectList(searchUser):
    if len(searchUser) == 0:
        #전체사용자
        selectSql = """
        SELECT idx, name, kor, eng, mat,(kor+eng+mat) as total, (kor+eng+mat)/3 as average
        FROM sungjuk 
        ORDER BY total DESC """
        cursor.execute(selectSql)
    
    else:
        #개별사용자
        selectSql = """
        SELECT idx, name, kor, eng, mat,(kor+eng+mat) as total, (kor+eng+mat)/3 as average
        FROM sungjuk WHERE name=%s
        ORDER BY total DESC """    
        cursor.execute(selectSql, searchUser)
    
    rows = cursor.fetchall()
    return rows

def addData(data): #['홍길동','100','200','300']
    insertSql = """INSERT INTO sungjuk(name, kor, eng, mat, reg_date) 
    VALUES (%s, %s, %s, %s, NOW())"""

    cursor.execute(insertSql,(data[0], data[1], data[2], data[3]))
    conn.commit()
    print('## 사용자 정보 추가 성공!')
    pass

def closeConnection():
    cursor.close()
    conn.close()

def main():
    while True:
        print("##현재 등록자 수:")
        # 1. 입력값이 숫자(1~4) 인지 확인
        try:
            cmd = int(input("1) 성적입력 2) 성적출력 3) 성적조회 (1~3) 4) 종료 -> "))
        except:
            print("1~4 사이의 정수를 입력해주세요.")
            continue

        if cmd == 1:
                # 2. 이름 뒤의 3개의 과목인지, ','로 구분되어 있는지
                # 3. 각 과목의 점수는 0~100     
                while True:
                    try:
                        userData = input('성적을 입력하세요. (이름, 국어, 영어, 수학) ->')
                        data = userData.split(',') # len(data) = 4 # split은 문자열을 쪼개는 함수. 인자는 ','를 받아서 이것 단위로 쪼갬
                        if len(data) != 4: #Error
                            raise Exception
                        else:
                            try:
                                kor = int(data[1]) 
                                eng = int(data[2])
                                mat = int(data[3])

                                if kor < 0 or kor > 100:
                                    raise Exception
                                if eng < 0 or eng > 100:
                                    raise Exception
                                if mat < 0 or mat > 100:
                                    raise Exception

                            except:
                                raise Exception
                    except:
                        print("** 성적데이터를 정확하게 입력해주세요.")
                        continue
                    else:
                        print(data) 
                        # DB에 저장.
                        addData(data)
                        break
        elif cmd == 2:
            # 정보 출력 
            print('###################################################')
            print('이름\t국어\t영어\t수학\t총점\t평균')
            print('###################################################')
            displaySungjuk('')            
        elif cmd == 3:
            # 정보 조회 -> 출력
            searchUser = input("검색할 학생이름을 입력하세요->")
            # DB 검색
            displaySungjuk(searchUser) 
        elif cmd == 4:
            closeConnection()
            quit()
        else:
            print("잘못된 명령어입니다. 다시 입력해 주세요.")
            continue





main()







