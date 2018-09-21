#주사위 게임
# 1~6개의 눈을 가진 3개의 주사위를 던져서, 다음 규칙에 따라 상금을 받는 게임
# 1) 같은 눈이 3개가 나오면 10,000원 + (같은 눈) * 1,000원
# 2) 같은 눈이 2개가 나오면 1,000원 + (같은 눈) * 100원
# 3) 모두 다른 눈이 나오면 (그 중 가장 큰 눈) * 100원
# 4) 게임을 계속하면 상금은 누적

# ex)
# 게임을 시작 하시겠습니까?(y/n)  -> y
# 당신의 주사위는 (3, 3, 6) 입니다. 상금은 1300원 입니다. 누적 상금 1,300원
# 게임을 시작 하시겠습니까?(y/n) -> y
# 당신의 주사위는 (2, 2, 2) 입니다. 상금은 12,000원 입니다. 누적 상금은 13,300원
# 게임을 시작 하시겠습니까?(y/n) -> y
# 당신의 주사위는 (6, 2, 5) 입니다. 상금은 600원 입니다. 누적 상금은 13,900원

import random
import math
money = 0
reward = 0
dic = {}

while True:
    answer = input("게임을 시작 하시겠습니까?(y/n)")
    if(answer == "Y" or answer == "y"):
        output = []
        for i in range(3):
            output.append(random.choice(range(1,7)))

        for i in range(1,7):
              dic[7-i] = output.count(7-i)

        item = list(dic.items())
        item.sort(key=lambda element:element[1],reverse=True)

        for final in item:
            if(final[1]==3):
                reward = (10000+ final[0] * 1000)
                money += reward
                break
            elif(final[1]==2):
                reward = (1000 + final[0] * 100)
                money += reward
                break
            elif(final[1]==1):
                reward += (final[0] * 100)
                money += reward
                break
        print("당신의 주사위는 {}입니다. 상금은 {}원입니다. 누적 상금은 {}원입니다.".format(output,reward,money))
        reward = 0

    elif answer =="N" or answer == "n":
        print("최종 상금은 %d입니다" % money)
        break
    else:
        print("다시 입력해주세요(y/n)")