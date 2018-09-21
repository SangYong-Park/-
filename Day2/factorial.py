# factorial 구하기
#  ex) 1x2x3 = 6

""" def factorial(n):
    multiNum = 1
    for i in range(1, n + 1):
        multiNum *= i
    return multiNum

print(factorial(5)) """

# 재귀함수

# def factorial(n):
#     if (n==1):
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial(n-1)

print(factorial(1))
print(factorial(3))
print(factorial(5))