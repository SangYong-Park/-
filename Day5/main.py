# python/Day05/main.py
import sub ## main 안에서 sub를 불러들임. import하는 모든 것들이 메모리에 올라옴
           ## import 모듈의 코드가 많을수록 많이 가져옴. from 사용해서 최대한 줄이는 것 권장.

print("beginning of sub by")
print("name:{0}".format(__name__))
print("end of sub day")  

# 결과 
# beginning of sub by
# name:sub
# end of sub day
# beginning of sub by
# name:__main__
# end of sub day