# A - Z ASCII 값 출력  ==> 한 줄로 출력
for c in range(ord('A'),ord('Z') +1):
    print(chr(c), '=', c, end='') 

len() # 길이
 - len("안녕하세요")
type() # 자료형
 - type("안녕하세요")
 - type(len("안녕하세요"))
float() 
 - float("3.14") # 문자를 실수형으로 형변환
str()
 - a = str("3.14") # 다시 문자형으로 변환
 - print(type(a))

 print("안녕하세요" * 3)
 print("안녕하세요"[0])
 print("안녕하세요"[4])

 print("안녕하세요"[0])
print("안녕하세요"[4])
print("안녕하세요"[0:1])
print("안녕하세요"[1:3])
print("안녕하세요"[:3])
print("안녕하세요"[1:])
print("안녕하세요"[:-1])
print("안녕하세요"[-2:-1])