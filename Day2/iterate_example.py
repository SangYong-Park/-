student = 1
while  student <= 5:
    print(student, " 번 학생의 성적 처리")
    student += 1  # <--> for는 범위가 존재. 언젠가는 범위가 끝나면 종료됨.

num = 1
sum = 0


while num<=100:
    #홀수의 합
    if num % 2 == 0:
        num+=1
        continue
    elif num % 2 == 1:
        sum = sum + num # sum += num 
        num = num + 1 # num += 1
        continue
print("1~100까지의 합 ", sum)

# 인수출력(1~100)
# 사용자로부터 숫자 입력(1~100)
# 입력받은 숫자의 소인수를 출력
# ex) 10 -> 1, 2, 5
# ex) 12 -> 1, 2, 3, 4, 6
