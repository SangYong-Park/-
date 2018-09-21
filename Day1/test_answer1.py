# 컴퓨터가 임의의 숫자를 하나 발생.(Random, 1-100)
# 컴퓨터가 발생한 숫자를 맞추기
# 5번 이하로 맞추면 10
# 10번 이하로 맞추면 5
# 10번 이상이면 0
# 총 몇 번의 시도로 몇 점인지 출력

import random

a = random.randrange(100)
time = 0
grade = 0
print(a)

while 1:
    answer = int(input("1에서 100까지의 정수를 입력해주세요 \n"))
    if(answer < 1 or answer > 100):
        print("범위 밖의 숫자 입력은 횟수로 인정되지 않습니다")
        continue
    time += 1
    if (answer == a):
        if(time <= 5):
            grade = 10
            print(time,"번 시도로",grade,"점입니다") 
            break
        elif(time <= 10):
            grade = 5
            print(time,"번 시도로",grade,"점입니다")
            break
        else:
            grade = 0
            print(time,"번 시도로",grade,"점입니다")
            break
    else:
        continue