# 단어 검출 개수 출력 => 공백 파싱
# 포함하지 않는 문자 : 숫자, 특수문자 제외. 
# 많이 사용된 문자 순으로 sort.
# 



import sys
import time

start = time.time()
f = open('C:\work\day01\Day4\\novel.txt') ## open("읽어올 파일명")
text = f.read()
print(len(text))

test = "my Name's sangyong! 'nong' 'Sangyong!' 7마리 Names nas!xsa " # 특수문자는 맨 처음이나 뒤에만 온다는 것.
words = test.split(' ')

def wordInDic (word, wordDic):
    if word.isalpha()==False:
        return
    if word in wordDic.keys():
        wordDic[word] = wordDic[word]+1
    else:
        wordDic[word] = 1

wordDic = {}
wordOnlyAlpha = ""

for word in words:
    if(word.isalpha()==False):
        for spell in word:
            if(spell.isalpha()==True):
                wordOnlyAlpha = wordOnlyAlpha + spell
            else:
                continue
        wordInDic(wordOnlyAlpha.capitalize(), wordDic)
        wordOnlyAlpha = ""
    else:
        wordInDic(word.capitalize(), wordDic)

wordTuple = list(wordDic.items())
wordTuple.sort(key=lambda element:element[1],reverse=True)
for wordNum in wordTuple:
    print(wordNum,end="")

end = time.time()
print("Elapsed time:", str((end-start)))

    



"""
1. 단어를 쪼갠다
2. 딕셔너리에 key-value 값으로 넣는다.
"""