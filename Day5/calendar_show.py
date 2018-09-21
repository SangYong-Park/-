
# 1. 사용자로부터 (1~12) 사이의 숫자를 입력
#   - 월로 인식해서 달력 출력
#   ex) 확인하려는 월을 입력하세요 (1~12) -> 9
#   ** 9월 **
#   S   M   T   W   T   F   S
#                           1
#   2   3   4   5   6   7   8 
#   9  10  11  12  13  14  15
#  16  17  18  19  20  21  22
#  23  24  25  26  27  28  29
#  30  31

# 2. 
#   S   M   T   W   T   F   S
#  26  27  28  29  30  31   1
#   2   3   4   5   6   7   8 
#   9  10  11  12  13  14  15
#  16  17  18  19  20  21  22
#  23  24  25  26  27  28  29
#  30  31

# 7개 데이터마다 개행
# 1일의 시작 요일    
# 매달의 마지막 날짜 파악
import statistics
import time, datetime
import calendar

# d = datetime.date.today()
# print(d)
# print(datetime.date(2018, 10, 1))
# print(d.weekday())  ## weekday는 0 - 월요일.
# print(datetime.date(2018, 10, 1).weekday())
# print(calendar.month(2018,10))
         

# print(time.localtime())
# print(time.ctime())

# 9.21일은 wday=4(금요일)  wday=[0월,1화,2수,3목,4금,5토,6일]
# 9.20일은 wday=3(목요일)  각 달의 마지막 날.
# localtime 

string_weekday = ['월','화','수','목','금','토','일']
day = calendar.weekday(2019, 2, 28)
print(day)
print(string_weekday[day])