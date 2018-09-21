# import math as m   ## module 이름이 길 경우 as를 통해 별명 부여 가능. from도 마찬가지.
# print(m.sqrt(2))
# print(m.sin(m.radians(45)))
# print(m.factorial(5))

# # from math import sqrt as sq ## 다만 줄이게 되면 다른 사람들이 일반적으로 알아보기 힘들 수도 있음. 비추천 
# # print(sq(2))    ## math.sqrt로 실행하면 오류남 + math.sqrt가 되지 않으면 어느 모듈에서 불러왔는지 파악하기 힘듬.

# import statistics

# score = {30, 40, 60, 70, 80, 90}
# print(statistics.mean(score)) ## 평균
# print(statistics.median_high(score)) ## 70
# print(statistics.median_low(score)) ## 60

# import time

# t = time.time()
# print(t)  ## 1970.1.1 기준 몇 초 지났는지 => 유닉스 타임
# print(time.ctime(t)) ## 우리가 쓰는 형태의 포멧
# print(time.localtime(t)) ## localtime의 year 등등 나옴. 포매팅은 따로 해줘야함
# now = time.localtime(t)
# print("%d년 %d월 %d일" % (now.tm_year,now.tm_mon,now.tm_mday))
# print("{0}:{1}:{2}".format(now.tm_hour,now.tm_min,now.tm_sec))

# start = time.time()
# str = ""
# for a in range(10000):
#     time.sleep(0.5) ## 1초에 1번씩 실행이 멈추게 한다.
#     str += "*"
#     print(str)

# # print(str)
# end = time.time()
# print("Elapsed Time:{0}".format(end - start))

# for dan in range(1,10):
#     print(dan,"단")
#     for hang in range(2,10):
#         print(dan,"*", hang, "=", (dan*hang))
#         time.sleep(0.2)
#     print()
#     time.sleep(1)

# import random

# # for i in range(5):
# #     print(random.random(), end='')

# # for i in range(5):    
# #     print(random.randint(1, 6))

# lang = ['Python', 'Java', 'C', 'JavaScript', 'Golang']

# print(random.sample(lang, 2))
# print(random.sample(range(1, 46), 6))  ## 복권 번호 뽑기

# print(lang)
# random.shuffle(lang)
# print(lang)
# for i in range(5):
#     print(random.choice(lang))
    

# game = ['KAWI', 'BAWI', 'BO']
# print(random.choice(game))

import sys, time

# print("Version:",sys.version)   
# print("Platform:",sys.platform)
# if sys.platform == 'win32':
#     print(sys.getwindowsversion)  ## 현재 윈도우 버전
#     # file -> Linux 계열은 '/'로 구분. Window 계열은 '\'로 구분.
#     # file list -> linux -> li / windows -> dir
# print("Module path:", sys.path)  ## path 경로

if (len(sys.argv)) != 2: # "python 파일명.py 파라미터" 형식이 아니라면 오류
    print("시작 날짜를 yyyymmdd로 입력하세요")
    sys.exit(0) ## 시스템이 정상종료된 것처럼 표현

birth = sys.argv[1] # 파라미터 (날짜)
if (len(birth)!=8 or birth.isnumeric()==False):
    print("날짜 형식이 잘못 되었다.")
    sys.exit(0)

tm = (int(birth[:4]), int(birth[4:6]), int(birth[6:8]), 0, 0, 0 ,0 ,0 ,0)


ellapse1 = int((time.time() - time.mktime(tm)) / (24 * 60 * 60)) ## mktime(maketime) -> 튜플 형태의 데이터를 Time 객체를 만들어주는 함수
print(ellapse1)
