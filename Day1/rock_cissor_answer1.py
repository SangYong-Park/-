# 가위바위보 (1,2,3) randrange(1,3)
# 지면 게임 종료
# 비기면 다시 입력
# 이기면
 # 게임 계속 or 종료
 # 계속하는 경우 : 상금 x 2
 # 종료하는 경우 : 상금만 받도록
 # 지면 상금 몰수
 # 기본 상금 : 100000원

import random

# comNum = random.randrange(1, 3)
cnt = 0
time = 0
reward = 100000
 
 # test용
while True:
    comNum = random.randrange(1, 3)
    print(comNum)
    userNum = int(input("가위(1) 바위(2) 보(3)->"))
    if userNum < 1 or userNum > 3:
        print("다시 입력하세요")
        continue # 가장 인접한 Loop의 조건식으로 이동
    else:
        #게임룰 계산
        if comNum == 1:
            if userNum == 2:
                print("사용자가 이겼습니다")
                answer = input("게임을 계속 진행하시겠습니까?(Y/N)")
                if(answer=="Y"):
                    time += 1
                    reward = reward * (2 ** time)
                    continue
                elif(answer=="N"):
                    print("상금은", reward, "입니다")
                    break
                else:
                    print("Y/N으로만 입력해주세요")
                    while answer != "Y" or answer != "N":
                        answer = input("게임을 계속 진행하시겠습니까?(Y/N)으로만 입력 \n")
                        if(answer == "Y" or answer == "N"):
                            break
                    if(answer=="Y"):
                        time += 1
                        reward = reward * (2 ** time)                        
                        continue
                    else:
                        break
                        print("상금은", reward, "입니다")
            elif userNum == 3:
                print("컴퓨터가 이겼습니다")
                reward=0
                print("상금은", reward, "입니다")
                break
            else:
                print("비겼습니다")
                print("게임을 다시합니다")
                continue
        elif comNum == 2:
            if userNum == 3:
                print("사용자가 이겼습니다")
                answer = input("게임을 계속 진행하시겠습니까?(Y/N)")
                if(answer=="Y"):
                    time += 1
                    reward = reward * (2 ** time)
                    continue
                elif(answer=="N"):
                    print("상금은", reward, "입니다")
                    break
                else:
                    print("Y/N으로만 입력해주세요")
                    while answer != "Y" or answer != "N":
                        answer = input("게임을 계속 진행하시겠습니까?(Y/N)으로만 입력 \n")
                        if(answer == "Y" or answer == "N"):
                            break
                    if(answer=="Y"):
                        time += 1
                        reward = reward * (2 ** time)
                        continue
                    else:
                        break
                        print("상금은", reward, "입니다")              
            elif userNum == 1:
                print("컴퓨터가 이겼습니다")
                reward=0
                print("상금은", reward, "입니다")
                break
            else:
                print("비겼습니다")
                print("게임을 다시합니다")
                continue            
        elif comNum == 3:
            if userNum == 1:
                print("사용자가 이겼습니다")
                answer = input("게임을 계속 진행하시겠습니까?(Y/N)")
                if(answer=="Y"):
                    time += 1
                    reward = reward * (2 ** time)
                    continue
                elif(answer=="N"):
                    print("상금은", reward, "입니다")
                    break
                else:
                    print("Y/N으로만 입력해주세요")
                    while answer != "Y" or answer != "N":
                        answer = input("게임을 계속 진행하시겠습니까?(Y/N)으로만 입력 \n")
                        if(answer == "Y" or answer == "N"):
                            break
                    if(answer=="Y"):
                        time += 1
                        reward = reward * (2 ** time)                        
                        continue
                    else:
                        break
                        print("상금은", reward, "입니다")
            elif userNum == 2:
                print("컴퓨터가 이겼습니다")
                reward=0
                print("상금은", reward, "입니다")
                break
            else:
                print("비겼습니다")
                print("게임을 다시합니다")
                continue 