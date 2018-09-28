# f = open("C:\work\day01\my_test.txt",'wt',encoding="utf-8")
# f.write("\n\n파이썬 파일읽기 쓰기 예제")
# f.close()  ## close는 반드시 해줘야함. 아니면 나중에 자원을 사용하고 있어서 문제 생길 수 있음.

with open("my_test.txt", 'rt',encoding="utf-8") as f:  ## with에 묶여있던 작업은 close를 자동으로 해줌. 
    text = f.read()  ## 모드에 따라서 read, write 사용 가능/불가능 결정됨. at 모드일 경우 readable하지 않다는 오류 발생

with open("new_test.txt", 'wt', encoding="utf-8") as g:
    g.write(text)

with open("new_test.txt", 'r+', encoding="utf-8") as g:
    text2 = g.read()   ## r+ 읽기 쓰기 모드 둘 다 가능함.
    g.write(text)

# rows = f.readlines()
# for row in rows:
#     print(row, end= '')
# f.close()

# for line in f:
#     print(line, end=";")
# f.close()

# f.seek(12,0) ## 12번째 바이트를 건너뛰고 데이터를 가져와라. # 두번째 인자는 0-처음부터,1-현재위치에서,2-뒤에서부터 건너뛰고 올 수 있음.
# print(f.tell()) ## 몇번째 위치에 있는지 불러옴 # 현재는 12
# text= f.read()
# f.close()
# print(text)

## 34567890123456
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# HELLO