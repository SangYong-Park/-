# 단어 검출 개수 출력 => 공백 파싱
# 포함하지 않는 문자 : 숫자, 특수문자 제외. 
# 많이 사용된 문자 순으로 sort.



import sys
import time

start = time.time()
f = open('C:\work\day01\Day4\\novel.txt') ## open("읽어올 파일명")
text = f.read()
print(len(text))

words = text.split(' ')

def wordInDic (word, dictionary):
    if word.isalpha()==False:
        return
    if word in dictionary.keys():
        dictionary[word] = dictionary[word]+1
    else:
        dictionary[word] = 1

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
    print(wordNum)

end = time.time()
print("Elapsed time:", str((end-start)))

    


