# ** 개미수열

# 1
# 11                : len=2, duplicate = yes
# 12                : len=2, duplicate = no 
# 1121              : len=4, duplicate = yes, No,
# 122111            : len=6, duplicate = no, yes, yes
# 112213            : len=6, duplicate = yes, yes, no, no
# 12221131          : len=8, duplicate = no, yes, yes, no, no
# 123123111         

# rowData -> 데이터 생성원
# output -> 만들어질 데이터
# current -> 현 상태를 나타낼 개별적 데이터
# index -> current를 나타내기 위한 index

rowData = "1"
print(rowData)

for i in range(10):
    output = ""
    index = 0
    while index < len(rowData):
        current = rowData[index]   # 1
        count = 1
        # 현재하고 다음숫자가 같은지 비교
        while index+1 < len(rowData) and current == rowData[index+1]:
            count+= 1    # 2
            index+= 1


        output += current + str(count)   # 11
        index += 1
    print(output)    
    rowData = output
    



