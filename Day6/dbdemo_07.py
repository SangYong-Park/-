import sqlite3

# Python DB API 구현
con = sqlite3.connect('user.db')
cursor = con.cursor()

def selectData():
    sql1 = 'SELECT * FROM tblAddr'
    cursor.execute(sql1)
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('이름: {0}, 전화번호: {1}, 주소: {2}'.format(row[0],row[1],row[2]))

# def updateData(isInsert):
#     if isInsert == True:
#         sql = "INSERT"
#     else:
#         sql = "UPDATE"
#     cursor.execute(sql)
#     con.commit()
#     print(isInsert,"성공")

def updateData():
    updateSql = "UPDATE tblAddr SET addr='서울' WHERE name='홍길동'"
    cursor.execute(updateSql)
    con.commit()
    print("수정 성공")

def closeConnection():
    cursor.close()
    con.close()

def main():
    selectData()
    updateData()
    selectData()
    closeConnection()

main()


# def connection(dbPath):
#     con = sqlite3.connect(dbPath)
#     return con

# def select(con, cursor, sqlSentence):
#     cursor.execute(sqlSentence)
#     table = cursor.fetchall()
#     return table

# def update(con, cursor, sqlSentence):
#     cursor.execute(sqlSentence)
#     con.commit()

# def main():
#     con = connection("user.db")
#     cursor = con.cursor()
#     sql1 = "SELECT * FROM tblAddr"
#     sql2 = "UPDATE tblAddr SET addr='광주' WHERE name='박상용'"
#     table1 = select(con,cursor,sql1)
#     update(con,cursor,sql2)
#     print(table1)


# main()
