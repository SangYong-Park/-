list_a = [1,2,3,4,5,6]
value = list_a.pop()

list_b = [1,2,3,4,5,6]
del list_b[:2]
print(list_b)

list_c = [1,2,3,4,5,6]
del list_c[3:]
print(list_c)

# del --> index 값으로 삭제
# remove --> 실제 값으로 삭제
list_a.remove(2)
print(list_a)

list_a.clear()
print(list_a)

