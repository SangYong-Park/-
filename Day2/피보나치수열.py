dic = {
    1: 1,
    2: 1
}

count = 0
def pivo(n):   ## 피보나치 수열
    """ 이 함수는 피보나치 수열을 구하기 위한 함수입니다."""
    if n in dic:
        return dic[n]
    else:
        global count 
        count += 1 # count = count + 1
        output = pivo(n-1) + pivo(n-2) # f(5)
        dic[n] = output
        return output

print("fivonacchi({})={}".format(10, pivo(10)),count)

help(pivo)
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211
# 개수 + 해당 글자






                