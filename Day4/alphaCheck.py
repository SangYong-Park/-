# With the anniversary of the Bitcoin whitepaper looming on October 31, it is remarkable how far and fast this industry has come since it was anonymously launched on a crypto bulletin board just ten years ago. Ethereum, which gave us smart contracts and ICOs, was only started in 2015. The Consensus conference, only in its fourth year, packed over 8500 attendees into the New York midtown Hilton with representatives from most major corporations and industries being present.
# Blockchain is quickly becoming mainstream. The industry is entering the phase of industrial competition — and this is happening on a global scale.
# Consensus is the centerpiece of Blockchain Week in New York City, and the main global industry conference for cryptocurrency and blockchain technology. It is also increasingly a platform for major industry announcements. Two clusters of announcements in particular are propitious markers of where we’re up to in the development of the industry.

news = """With the anniversary of the Bitcoin whitepaper looming on October 31, it is remarkable how far and fast this industry has come since it was anonymously launched on a crypto bulletin board just ten years ago. Ethereum, which gave us smart contracts and ICOs, was only started in 2015. The Consensus conference, only in its fourth year, packed over 8500 attendees into the New York midtown Hilton with representatives from most major corporations and industries being present.
Blockchain is quickly becoming mainstream. The industry is entering the phase of industrial competition — and this is happening on a global scale.
Consensus is the centerpiece of Blockchain Week in New York City, and the main global industry conference for cryptocurrency and blockchain technology. It is also increasingly a platform for major industry announcements. Two clusters of announcements in particular are propitious markers of where we’re up to in the development of the industry.
"""

# {'a':2, 'b':3, 'c':1, 'e':10, ...}
# alphabet = {}
# for char in news:
#     if char.isalpha() == False:
#         continue
#     char = char.lower() # A -> a
#     if char not in alphabet: # True, False
#         alphabet[char] = 1 # {'e':1, 'y':1}
#     else:
#         alphabet[char] += 1
        
# print(alphabet)

# 오름차순 정렬 (A -> Z)

# keyList = list(alphabet.keys())
# keyList.sort()
# for key in keyList:
#     num = alphabet[key]
#     print(key, '=', num)

# print()
# key = list(alphabet.items())
# key.sort(key=lambda e:e[0])
# for pair in key:
#     print(pair)

## 1. 검색 x --> 표시

# alphabet = {}
# for char in news:
#     if char.isalpha() == False:
#         continue
#     char = char.lower() # A -> a
#     if char not in alphabet: # True, False
#         alphabet[char] = 1 # {'e':1, 'y':1}
#     else:
#         alphabet[char] += 1

# for c in range(ord('a'), ord('z') + 1):
#     print(chr(c), '=', alphabet.get(chr(c),0)) ## 없으면 0을 가져옴

## 내가 한 것

# keyList = list(alphabet.keys())

# for ascNum in range(ord('a'),(ord('z')+1)):
#     if chr(ascNum) not in keyList:
#         alphabet[chr(ascNum)] = 0
#         keyList.append(chr(ascNum))

# keyList.sort()
# print(keyList)

# for key in keyList:
#     num = alphabet[key]
#     print(key, '=', num)

## 2. 단어 검출 출력 ==> 공백으로 데이터 파싱
      # 단어 사용 횟수
      # 포함하지 않는 문자 - 숫자, (, ), ',', . , ...
      # 포함하는 문자 - '
        # China's (o) china(o) china.(x)

test = "aaaa,bbbb cccc AAAA BBBB CCCC"
wordDic = {} 
words = test.split(' ')
print(words)

for word in words:
    if word.isalpha()==False:
        continue
    if word not in wordDic:
        wordDic[word] = 1
    else:
        wordDic[word] += 1

keyList = list(wordDic.keys())
keyList.sort()

for key in keyList:
    print(key,"=",wordDic[key])


## 내가 한 것
# def checkAlpha(alphabet,sentences):
#     count = 0
#     for word in sentences:
#         if char.isalpha() == False:
#             continue     // 예외 처리 놓침.
#         if(word == alphabet.upper() or word == alphabet.lower()):
#             count+=1
#     return count

# print(checkAlpha("A",news))
# print(checkAlpha("a",news))
# print(checkAlpha("b",news))
# print(checkAlpha("c",news))

