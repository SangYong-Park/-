# dic = {'boy':['소년','남자아이'], 'school':['학교','공부하는 곳'], 'book' : ['책', '정보를 얻을 수 있는 것']} # dic.value로 리스트, 튜플 등도 올 수 있음.
# print(dic)
# print(type(dic))
# # print(dic['boy'])      ' dicread'
# # print(dic['girl'])
# print(dic.get('boy')) 
# print(type(dic.get('boy')))
# print(dic.get('girl','사전에 존재하지 않는 단어입니다.')) ## None이 아니라 사전에 ~ 반환

# print(dic.keys())
# print(dic.values())
# print(type(dic.items()))
# for item in dic.items():
#     print(item) # tuple 형태의 데이터 출력 ('boy','소년'). # ==> sorting, index 등 사용가능
#     print(item[0], item[1])
#     print(item[0], item[1][0], item[1][1])

# dic2 = {'student':['학생','공부하는 사람'],
#         'teacher':['선생님', '가르치는 사람'],
#         'book':['교과서','공부하기 위한 도구']}

# dic.update(dic2)    ## 결과값 : {'boy': ['소년', '남자아이'], 'school': ['학교', '공부하는 곳'], 'book': ['교과서', '공부하기 위한 도구'], 'student': ['학생', '공부하는 사람'], 'teacher': ['선생님', '가르치는 사람']}
# print(dic)          ## update함수: 기존의 없는 내용은 추가. 있는 내용은 바꾼다.

# myList = [['boy','남자아이'],
#             ['school','공부하는 곳'],
#             ['book','공부하기 위한 도구'],
#             [123,'숫자입니다']]

#             # [[1,2], 'tests']]  ==> 오류 발생. key는 단일 형태의 데이터이어야함. value는 여러 값이 와도 key에 대한 단일 value로 인식됨.

# dic = dict(myList)   ## dict : dictionary 형태로 변환
# print(type(dic))
# print(dic)

# print(type(myList))
# print(myList[2][1])

# asiaList = ['korea','china','japan','korea']
# asiaSet = {'korea','china','japan','korea'}
# asiaSet.add('usa')
# asiaSet.add('china')
# asiaSet.remove('japan')
# asiaSet.update({'singapore','hongkong', 'korea'}) ## 중복된 데이터는 덮어쓰고, 나머지 추가
# print(asiaSet)
# print(asiaList)
# print(type(asiaList))
# print(asiaSet)
# print(type(asiaSet))
# print(set("sangyongPark"))  ## {'s', 'n', 'P', 'o', 'g', 'k', 'y', 'r', 'a'} : 겹치는 것 제거 후 들어감.
# print(set([12,34,56,78,90])) ## {34, 12, 78, 56, 90}
# print(set(('python', 'Django', 'Blockchain'))) ## {'Blockchain', 'python', 'Django'}
# print(set({'boy':'소년','girl':'소녀','male':'남성','female':'여성'})) # {'female', 'boy', 'male', 'girl'} key값만 저장됨
# print(set()) # set()

## set은 입력 순서와 상관없이 표현됨.

# score = [88, 95, 70, 100, 99]
# for no, s in enumerate(score,1): ## enumerate(대상, 어디서부터 시작할 것인지)
#     print(str(no) + "번 학생 점수:", s)

# days = ['월','화','수','목','금','토','일']
# foods = ['갈비탕','설농탕','순대국','칼국수']
# menu = zip(days, foods)
# print(type(menu))

# for d, f in menu:
#         print(d, ' 메뉴:', f) ## 개수가 같은 곳까지만 결합.

# # 월  메뉴: 갈비탕
# # 화  메뉴: 설농탕
# # 수  메뉴: 순대국
# # 목  메뉴: 칼국수

# score = [45, 98, 72, 50, 94] 
# for s in score:
#         if s < 60:
#                 print(s)

# def multiply(a): ## 0보다 크면 전부 True로 됨. 결과값은 원본 그대로.
#         return a * 2

# for s in filter(lambda a:(a<60),score): ## multiply 함수를 한 뒤 출력. lambda 매개변수:매개변수에 대한 반환값
#         print(s)

# score = [45, 90, 72, 50, 85]
# bonus = [5, 5, 10, 7, 8]

# # def total(s, b):
# #         return s + b

# for s in map(lambda a,b:a+b, score, bonus):
#         print(s)

# for s in map(lambda a:a*2,score):
#         print(s)

# import copy

# list0 = ['a','b']
# list1 = [list0, 1, 2]
# # list2 = list1.copy()
# # list2[0][1] = 'c'
# # print(list1)
# # print(list2)

# list2 = copy.deepcopy(list1)
# list2[0][1]='c'
# print(list1)
# print(list2)

# index = 5 # user input data

# list_a = [1, 2, 3, 4, 5]
# print(list_a[1])
# if index >= len(list_a):
#         print("ERROR!")
# else:
#         print(list_a[index])


# while True:
#         inputData = input("반지름을 입력하세요->")

#         try:
#                 num = int(inputData)

#         except Exception as ex : # Exception as 원하는 이름 : 오류 객체 선언
#                 print("type(ex):" + type(ex))
#                 print("exception:", ex)
#                 # print("입력값이 잘못 되었다!")
#                 continue
#         else:
#                 print("반지름", num)
#                 print("원 둘레", (3.14 * 2 * num))
#                 print("원 넓이", (3.14 * num * num))
        
#         finally:
#                 print("## 항상실행")
#         print("#####BYE")

# myList = ['100', '90', '80', '70', 'TEST', '60', '50']
# newList = []

# for item in myList:
#         # if item.isdigit() == True:
#         #         newList.append(item)
#         # else:
#         #         print(item, "은(는) 숫자가 아닙니다.")
#         try:
#                 int(item)
                
#         except:
#                 pass ## pass는 이 구문을 실행하지 않는다. 오류는 그냥 넘어감.
#         else: ## 에러 발생하지 않은 부분은 else에 가서 실행 - 파이썬에만 있는 문법.
#                 newList.append(item)
#         finally: ## try or except 상관없이 무조건 실행되는 문장
#                 print("항상 실행")
# print(newList) # try ~ exception

# score = [85, 80, 60, 100, 70]

# while True: 
#         userData = input("index를 입력하세요 (0-4)->")
#         try:
#                 num = int(userData)
#                 if num < 0 or num > 4:
#                         raise IndexError  ## 로직 상 문제없지만 input 값 제한

#                 print("{}째 점수는: {}".format(num, score[num]))

#         except ValueError as ex:
#                 print("Type(exception):", type(ex))
#                 print("Exception message:",ex)
#                 print("######### 정수만 입력해 주세요.")
#                 continue

#         except IndexError as ex:
#                 print("Type(exception):", type(ex))
#                 print("Exception message:",ex)
#                 print("######### 입력 가능한 범위는 0-4입니다.")
#                 continue

#         except Exception as ex:  ## 모든 에러를 다 정의해놓기 어렵기 때문에 다른 예외 발생시 이 구문이 실행.
#                 print("예기치 못한 에러가 발생했습니다")

# def calcsum(n):
#         # n이 음수인지 확인하는 작업?
#         if n < 0:
#                 raise ValueError("양의정수 사용")
#                 return -1
#         sum = 0
#         for i in range(1,n+1):
#                 sum += i
#         return sum

# # print("1~10=", calcsum(10))
# try:
#         result1 = calcsum(-5)
# # if result1 == -1:
# #         print("양의 정수를 사용해주세요")
# # else:
# #         print("1~5:",result1)
#  # return value -> 정수, valueError 총 2가지 가능
# except ValueError as ex:
#         print("양의 정수를 사용해주세요")

# try:
#         print("네트워크 접속")
#         a = 2 / 0
#         print("....네트워킹 관련 작업...")
#         print("....네트워크 통신 수행...")
# except:
#         print("!! 에러 발생!!")
# finally:
#         print("접속 해제")

# print("작업 완료")

# dic = {'boy':['소년','남자아이'], 
# 'school':['학교','공부하는 곳'], 
# 'book' : ['책', '정보를 얻을 수 있는 것']}


# # print(dic.get('girl'))  ## Error 없이 None 받아오게
# try:
#         print(dic['boy'])
#         print(dic['girl'])
# except KeyError as ex:
#         print("type(ex):",type(ex))
#         print("찾는 단어가 없습니다")

score = 120
try:
        assert score <= 100, "점수는 100 이하여야 합니다." ## assert 조건, 에러메시지 : 조건을 거짓으로 만드는 값은 뒤의 에러메시지 출력 
                                                 ## 테스트용으로 사용.
except AssertionError as ex:
        print(ex)
else: 
        print(score)