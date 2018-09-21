""" 성적관리 어플리케이션
[입력, 전체출력, 검색]
입력
 1. 사용자로부터 [이름, 국어, 영어, 수학] 성적 입력
    - 3명 사용자 입력
    - dictionrary로 관리
       ex) 
           sungjuk = {
               '홍길동' : [100, 100, 90],
               '박민지' : [100, 100, 90],
               '김유신' : [100, 100, 90]
           }

           sungjuk = {}
           sungjuk['name'] = [---]
전체출력
    1. 전체 데이터를 성적순으로 출력
검색 
    1. 사용자 이름 입력해서 조회
"""    

sungjuk = {}
listup = []
listup2 = []

sungjuk['HONG'] = [100 ,90 ,80]
sungjuk['KANG'] = [70 ,85 ,99]
sungjuk['KIM'] = [45 ,86 ,90]
sungjuk['LEE'] = [80, 85 ,81]

# def displaySungjuk():
#     for student in sungjuk:
#         # print(student, '\t', sungjuk[student]) # 국어, 영어, 수학, 총점, 평균, 석차
#         temp = sungjuk[student] # [100, 90, 80] -> list -> append(A), insert(B), extend([총점,평균])
#         sum = temp[0] + temp[1] + temp[2]
#         avg = sum/3
#         if len(temp) < 5:
#             temp.extend([sum, avg]) # [100, 90, 80, 270, 90] -> list, Tuple => sort 함수 사용
#         # print(student, '\t', sungjuk[student])

#     items = sungjuk.items()
#     # items[1][3] # 총점
#     newList = sorted(sungjuk.items(), key=lambda element:element[1][3],reverse=True) # 결과 정렬값에 대해서 새로운 리스트를 반환
#     for student in newList:
#         print(student[0],'\t', student[1])

# for key in sungjuk.keys():
#     i = 0
#     listup.append(key)
#     listup.append(sungjuk[key][0]+sungjuk[key][1]+sungjuk[key][2])
#     listup.append((sungjuk[key][0]+sungjuk[key][1]+sungjuk[key][2]) / 3)
#     # print(listup)
#     listup2.append(listup)
#     print(listup2)
#     listup = []
# print()

# listup2.sort(key=lambda element:element[1], reverse=True)
# print(listup2)

while True:
    print("##현재 등록자 수:", len(sungjuk))
    cmd = int(input("1) 성적입력 2) 성적출력 3) 성적조회 (1~3) 4) 종료 -> "))
    if cmd == 1:
            userData = input('성적을 입력하세요. (이름, 국어, 영어, 수학) ->')
            print(userData) # '홍길동,100,90,78'
            print(userData.split())
            data = userData.split(',')  # split은 문자열을 쪼개는 함수. 인자는 ','를 받아서 이것 단위로 쪼갬
            print(data) #['홍길동','100','90','70']
            # sungjuk['name'] = ['100','75','70']
            sungjuk[data[0]] = [int(data[1]), int(data[2]), int(data[3])]
    elif cmd == 2:
        # 정보 출력 sungjuk(3)
        print('##################################')
        print('이름\t총점\t평균\t등수')
        print('##################################')
        # displaySungjuk()

        # 내가 짠 코드 - work
        for key in sungjuk.keys():
            listup.append(key)
            listup.append(sungjuk[key][0]+sungjuk[key][1]+sungjuk[key][2])
            listup.append((sungjuk[key][0]+sungjuk[key][1]+sungjuk[key][2]) / 3)
            listup2.append(listup)
            listup = []
            listup2.sort(key=lambda element:element[1], reverse=True)
        
        for i in range(len(listup2)):
            print(listup2[i][0],end="\t")
            print(listup2[i][1],end="\t")
            print("{:.2f}".format(listup2[i][2]),end="\t")
            print(i+1,"등")
        
        listup2=[]
        
    elif cmd == 3:
        # 정보 조회 -> 출력
        searchUser = input("검색할 학생이름을 입력하세요->")
        print(sungjuk[searchUser])
    elif cmd == 4:
        quit()
    else:
        print("잘못된 명령어입니다. 다시 입력해 주세요.")
        continue
    #sungjuk (3)


""" 내가 한 것
sungjuk = {}
score = []

for i in range(1,4):
    name = input("본인의 이름을 입력해주세요. \n")
    a = input("국어 점수를 입력해주세요")
    score.append(a)
    b = input("수학 점수를 입력해주세요")
    score.append(b)
    c = input("영어 점수를 입력해주세요")
    score.append(c)
    d = (a + b + c / 3)
    score.append(d)
    sungjuk[name]=score

# 전체출력


    
# 검색
"""






