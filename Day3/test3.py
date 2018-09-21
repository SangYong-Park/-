# file = "20171224-104830.jpg"
# print("촬영날짜 : " + file[4:6] + "월" + file [6:8] + "일")
# print("촬영시간 : " + file[9:11] + "시" + file [11:13] + "분")
# print("확장자: " + file[16:])

# p = "  I like Python better than Java  "
# print(len(p))
# print(p.find('e'))  ## 문장 앞에서부터 e를 찾아라 find("문자")
# print(p.rfind('e')) ## 문장 끝에서부터 e를 찾아라 rfind("문자")
# print(p.index('e')) ## 문장 앞에서부터 e를 찾아라 find("문자") - find와 동일
# print(p.count('e')) ## 문장에서 e의 개수를 찾아라 find("문자")
# print('a' in p) ## p 안에 a라는 글자가 있는가? True or False로 반환
# print('b' not in p) ## p 안에 b라는 글자가 없는가? True or False로 반환

# # 대소문자/알파벳/숫자 확인
# print(p.isalpha()) ## alphabet으로만 되어 있는가? -> 공백 있어서 false
# print(p.islower()) ## 모든 문자가 소문자로만 되어있는가?
# print(p.isupper()) ## 모든 문자가 대문자로만 되어있는가?
# print(p.isalnum()) ## 모든 문자가 알파벳 또는 숫자로 되어있는가?
# print(p.isnumeric()) ## 모든 문자가 숫자로 되어있는가?

# ## 변경
# print(p.lower())  ## 원본 데이터는 안바뀜. 표시될 때만 보여줌.
# print(p.upper())  ## 원본 데이터는 안바뀜. 표시될 때만 보여줌.
# print(p.swapcase()) ## 대소문자 스왑.
# print(p.capitalize()) ## 대문자 하나로만 표시
# print(p.title())  ## 단어 앞글자만 대문자로 바꿔줌

# # 웹사이트 - 영문자(대/소), 숫자, 특수문자 1개 이상
# # k -> count('k') > 0

# # 공백 제거
# print(p + ":" + str(len(p)))
# print(p.strip() + ":" + str(len(p)))  ## 공백 제거. 사용자가 입력시 실수로 공백을 입력한 경우, DB query 등에서 문제 생길 수 있음. 그럴 때 사용.
# print(p.lstrip() + ":" + str(len(p))) ## 왼쪽 공백만 제거 
# print(p.rstrip() + ":" + str(len(p))) ## 오른쪽 공백만 제거

# s = """ABCDEFG
# APPLE
# BANANA
# ORANGE GRAPE
# MILK, COFFEE, TEA, WATER"""
# print(s)
# print(s.splitlines())  ## 개행 문자를 기준으로 나눈 뒤 리스트 형태로 표시됨 ['ABCDEFG', 'APPLE', 'BANANA', 'ORANGE GRAPE', 'MILK, COFFEE, TEA, WATER']

# s = ".-."
# print(s.join("파이썬프로그래밍"))

# s = "Java programmer\nweb programmer\nPython programmer\n"
# print(s)
# print(s.replace("programmer","developer")) ## programmer를 developer로 바꿈
# print(s.replace('\n', '<br/>'))  ## 사용자가 엔터를 입력하면 줄바꿈을 <br/> 태그 사용. 그래서 \n을 html이 이해하도록 <br/>로 바꾸면 됨.

# s = """
# <html>
# <body>
# <h1>Hello world</h1>
# </body>
# </html> """
# print(s)
# p = print(s.replace("<","&lt;").replace(">","$gt;"))   ## chain method 사용. 앞에서부터 차례대로 실행.

# s = "PYTHON"
# print(s + ":" + str(len(s)))
# print(s.rjust(10) + ":" + str(len(s))) ## 오른쪽 정렬 
# print(s.ljust(10) + ":" + str(len(s))) ## 왼쪽 정렬

# s2 = """ABCDEFG
# APPLE
# BANANA
# ORANGE GRAPE
# MILK, COFFEE, TEA, WATER""" 
# s3 = s2.splitlines()    ## 분할을 해서 줄별로 불러와서 가운데 정렬해야함. 저 자체가 하나의 문자열이기 때문.
# for line in s3:
#     print(line.center(20))

# fmt = "%d년 %d월 %d일"
# for m in range(7):
#     print(fmt % (2018, m+1 , 1))

# s1 = (100,200,300) ## 튜플 만들기 (100,200,300)
# print(s1)
# s2 = 100,200,300 ## 튜플 만들기 (100,200,300)
# print(s2)
# s3 = 100 ## 일반 변수 100 
# print(type(s3))  
# s4 = 100, ## 튜플 형식의 데이터 (100,)
# print(type(s4))

# a, b = 10,20   ## 튜플형 데이터이기 때문에 가능한 것.
# print(a)
# print(b)

# s = [30, 13500, 2000]
# for price in s:
#     print("가격: %d원" % price)
# print()
# for price in s:
#     print("가격: %-7d원" % price)

# value = 1234567890
# print(value)
# print("%d" % value)
# print("%20d" % value)
# print("{:,}".format(value)) ## 1,234,567,890

# pie = 3.141592
# print(pie)
# print("%10f" % pie)
# print("%10.8f" % pie)
# print("%10.5f" % pie)
# print("%10.2f" % pie)

# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(s)
# print(s[2])
# s[2] = 50 ## [0, 1, 50, 3, 4, 5, 6, 7, 8, 9]
# print(s)
# s[2:5] = 10, 20, 30  ## [0, 1, 10, 20, 30, 5, 6, 7, 8, 9]
# print(s)
# s[6:8] = [100, 200, 300, 400, 500]   ## [0, 1, 10, 20, 30, 5, 100, 200, 300, 400, 500, 8, 9] 값 나옴. 개수가 안맞으면 그 위치에 삽입됨.
# print(s)

# s = [[1,2,3],[4,5],[6,7,8]]  ## [1,2,3]은 0번. [4,5]는 1번. [6,7,8]은 2번
# print(s[0])
# print(s[0][0]) # [1,2,3]의 0번 ==> 1

# s = [[1 ,2 ,3], [4 ,5], [6 ,7 ,8 ,9]]
# print(s)
# for outerEl in s:
#     # print(outerEl)   ## outerEl = list 형태의 데이터
#     print("LEN=" + str(len(outerEl)))
#     for innerEL in outerEl:
#         print(innerEL,end="\t")
#     print()

# A B C D E F

# nums = [1,2,3,4]
# nums[2:2]=[90,91,92]  ## num : [1, 2, 90, 91, 92, 3, 4] 요소 6개
# print(nums)
# print(str(len(nums)))

# nums = [1,2,3,4]
# nums[2]=[90,91,92]   ## num : [1, 2, [90, 91, 92], 4] 요소 4개
# print(nums)
# print(str(len(nums)))

# score = [88, 95, 100, 70, 99, 80, 50]
# perfect = score.index(100) + 1
# print("만점 받은 학생은 %d번입니다." % perfect)
# perfectNum = score.count(100)
# print("만점 받은 학생은 {}명 입니다.".format(perfectNum))

# score.sort()  ## 오름차순 정렬
# print(score)
# score.reverse()  ## score.sort()와 결합하여 내림차순 정렬
# print(score)

# words = ['apple', 'banana', 'orange', 'melon', 'grape', 'coffee', 'tea', 'black-tea']
# words.sort()
# print(words)
# words.sort(reverse=True)
# print(words)
# words.sort(key=len) ## 'len=단어길이'를 가지고 오름차순 정렬
# print(words)

# sungjuk = [('HONG', 100, 90), ('KIM', 80, 70), ('LEE', 95, 55)]
# print(sungjuk)
# sungjuk.sort(key = lambda element : element[1] )  ## 튜플에 대해서 누굴 가지고 정렬해야 할지 모름. 그 기준을 key로 지정해주어야함.
#                                                    ## lambda는 함수 이름이 없는 단일성 함수. 요소 1번 기준으로 정렬
# print(sungjuk)

# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#     a.pop()
#     print(a)

# city, latitude, longtitude = 'Seoul', 37.541, 126.986
# print(city)
# print(latitude)
# print(longtitude)

dic = {}
dic['파이썬'] = 'www.python.org'  ## 딕셔너리 값 추가 key:파이썬 value:'www.python.org'
dic['마이크로소프트'] = 'www.microsoft.com'
dic['애플'] = 'www.apple.com'
print(dic['파이썬'])
print(dic['마이크로소프트'])
print(dic['애플'])
print(type(dic)) ## <class 'dict'>
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())  ## key-value를 묶어서 튜플 형태로 리스트에 담아서 보여줌

items = dic.items()
for item in items:
    print(item)
    print(type(item))
print()
for key in dic.keys():  ## key값을 가져와서 개별 dictionary의 key로 사용함.
    print(dic[key])
print()
inputKey = "애플"
if inputKey in dic.keys():
    print("선택한 값은:" + dic[inputKey])
else:
    print("선택한 값에 해당하는 데이터가 없습니다.")