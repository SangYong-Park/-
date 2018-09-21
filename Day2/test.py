"""import random
conNum = random.randrange(1, 100)"""

# num = 1
# print(conNum, " \n")
#while(num<=100):
#    if conNum % num == 0:
#        print(num, end=" ")
#    num+=1

#userNum = int(input("input number?"))
#for m in range(userNum / 2):
#    if m == 0:
#        continue
#
#    if userNum % m == 0:
#        print(m)

""" for dan in range(1,10):
    print(dan, " 단", end="             \n")
    for gugu in range(1,10):
        for gugu2 in range(1,10):
            print("%d * %d = %d " % (gugu, gugu2, (gugu * gugu2)), end="")

for i in reversed(5):"""

""" list_a = [52, 100, 90, 80, 43]

\"""min_value = min(list_a)
max_value = max(list_a)
print("MIN=", min_value)
print("MAX=", max_value)\"""

length = len(list_a) - 1
for i in range(length):
    for j in range(length - i):
        if list_a[j] > list_a[j+1]:
            #temp = list_a[j]
            #list_a[j] = list_a[j+1]
            #list_a[j+1] = temp
            list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
print(list_a[0])
print(list_a[len(list_a)-1])

"""

"""a = [10, 20, 30]
b = len(a)
print(b)

def len(array):
    return ..."""

#def print_times(count):
#    for i in range(count):
#        print("hello")

# print_times(10)
def print_sth(str_user,count):
    for i in range(count):
        print(str_user)

print_sth("졸려", 5)     

def add(a, *b): #가변 매개변수는 맨 뒤에 1개만 선언해야함. 그렇지 않으면 고정 매개변수의 위치를 알 수 없는 상황도 발생.
    print("")

add(100,200,300,400,500) ### 100은 a로. 나머지는 b로 감. 