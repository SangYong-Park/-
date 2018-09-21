import random

comNum = random.randrange(1, 100)
cnt = 0
grade = 0
while True:   ## while은 조건이 충족되기 전까지 계속 반복. 
    userNum = int(input("숫자를 입력하세요(1~100)->"))
    cnt += 1
    if userNum < 1  or userNum > 100:
        print("1~100 사이의 숫자를 입력해주세요")
    else:
        if comNum > userNum:
            print("보다 큰 숫자를 입력해주세요")
        elif comNum < userNum:
            print("보다 작은 숫자를 입력해주세요")
        else:
            print("맞췄습니다")
            break ## break와 가장 근접해 있는 반복문(Loop)을 강제로 종료함.

if cnt <= 5:
    grade+=10
elif cnt <= 10:
    grade+=5
else:
    grade=0

print("========================")
print("COMNUM=",comNum)
print("축하합니다.총 ", cnt, "번만에 맞추었습니다")
print("점수는",grade,"입니다")


