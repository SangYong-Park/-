dic = {
    "a": 100,
    "b": 200,
    "c": 300,
    "d": 400,
    "sum" : [10,20,30,40,50]
}

#print(dic)
#print(dic["a"])
#print(dic["d"])
#print(dic['sum'])

for key in dic.keys(): # keys라는 함수를 사용하면 dictionary 안의 모든 데이터를 읽어옴.
    print(key, "=", dic[key])

del dic['sum']
print(dic)

if 'sum' in dic:
    print("'sum' 키가 존재")
else:
    print("'sum' 키가 존재 x")

for d in dic:
    