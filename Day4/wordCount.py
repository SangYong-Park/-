# 단어 검출 개수 출력 => 공백 파싱
# 포함하지 않는 문자 : 숫자, 특수문자 제외. 단 's는 한 단어로 허용.
# 많이 사용된 문자 순으로 sort.

import sys
import time

start = time.time()
f = open('C:\work\day01\Day4\\novel.txt') ## open("읽어올 파일명")
text = f.read()
print(len(text))
end = time.time()
print("Elapsed time:", str((end-start)))

test = "my Name's sangyong! 'nong' 'sangyong!' 7마리 Names' " # 특수문자는 맨 처음이나 뒤에만 온다는 것.
words = test.split(' ')


    



"""
1. 단어를 쪼갠다
2. 딕셔너리에 key-value 값으로 넣는다.
"""