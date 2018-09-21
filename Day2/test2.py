""" def print_n_times(n,*values):
    print("LEN=", len(values))
    for i in range(n):
        for value in values:
            print(value, end="")
        print()

print_n_times(1, "A") """

""" def print_n_times(value, cnt=5):
    for i in range(cnt):
        print(value, end="")

print_n_times("A", 3)
print_n_times("B")""" 

""" def test(a, b=10, c=100):
    print("before")
    return a + b + c
    print("after")

def test2():
    userData = int(input("숫자를 입력하세요(1-9)"))
    if userData < 1 or userData > 9:
        print("숫자를 잘못 입력했습니다....")
        return

    if userData == 1:
        print("A")

print(test(200,c=1))
print(test2()) """

""" def sum_all(startNum=1, lastNum=100): # parameter 지정?
    # pass  # 현재 여기를 임시로 비워둔다. pass
    sum = 0
    for i in range(startNum, lastNum+1):
        sum += i
    return sum

print("1 to 100", sum_all()) # 1 to 100-5050  """

file = "20171224-104830.jpg"
print("촬영날짜 : " + file[4:6] + "월" + file [6:8] + "일")
print("촬영시간 : " + file[9:11] + "시" + file [11:13] + "분")
print("확장자: " + file[16:])