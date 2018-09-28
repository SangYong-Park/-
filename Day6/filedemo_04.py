# filedemo_04.py

import os
import time, datetime
import glob

# 사용자로부터 디렉토리(폴더)명을 입력받은 후 파일목록(폴더목록 포함) 출력.

# files = os.listdir("C:\\") ## C:\ 디렉토리의 모든 파일, 디렉토리가 보임
# for f in files:
#     print(f)

def listDir(dir):
    files = os.listdir(dir)
    print('\t\t{0} 디렉토리 내용입니다.'.format(dir))
    print("-" * 50)
    fileList = []
    dirList = []
    os.chdir(dir)
    
    for file in files:
        # 파일? 디렉토리? -> os.path.isfile(), isdir()
        # 디렉토리 출력, 파일 출력 (이름순)
        # 1. 디렉토리와 파일을 구분하여 출력
        # 2. 생성시간, 파일 크기 등의 정보 출력
        # 3. tree라는 명렁어처럼 만들고 싶음
        if os.path.isfile(file) == True:
            fileList.append(file)
        else:
            dirList.append(file)

    for dirName in dirList:
        print("{0}\t<DIR>\t-\t{1}".format(
            time.ctime(os.path.getmtime(dirName)),
            dirName)
        )
    print("-------------------------")

    sumSize = 0 

    for fileName in fileList:
        sumSize += os.path.getsize(fileName)
        print("{0}\t-\t{1}\t{2}".format(
            time.ctime(os.path.getmtime(fileName)),
            os.path.getsize(fileName),
            fileName
        ))
    print("-" * 50)
    print("전체 디렉토리 개수:", len(dirList))
    print("전체 파일 개수:", len(fileList))
    print("전체 파일 용량:", sumSize/1024,"byte")


    # 내가 한 것
    # for dirName in dirList:
    #     ModiTime = time.ctime(os.path.getmtime(dirName))
    #     print(ModiTime, "<dir>", " " * 10, dirName)
    # print("-------------------------")
    # sumSize = 0 
    # for fileName in fileList:
    #     size = os.path.getsize(fileName) / 1024
    #     sumSize = sumSize + size
    #     ModiTime = time.ctime(os.path.getmtime(fileName))
    #     print(ModiTime, " " * 5, "%0.2f" % (size)," byte", fileName)
    
    # print("-------------------------")
    # print("전체 파일크기","%0.2f" % (sumSize)," byte")
    # print("전체 파일개수",len(fileList))
    # print("전체 디렉토리 개수",len(dirList))
    # for dirs in dirList:
    #     size = os.path.getsize(dirs)
    #     time = os.path.getctime(file)
    #     time = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    #     print("<dir>",dirs, size, time)
    # for file in fileList:
    #     size = os.path.getsize(file)
    #     time = os.path.getctime(file)
    #     time = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    #     print("<file>",file, size, time)

def traverse(path, max_depth = 999, depth = 0):
    for obj in glob.glob(path + '/*'):
        if depth == 0:
            prefix = '|--'
        else:
            prefix = '|' + '  ' * depth + '+--'
        
        if depth < max_depth:
            if os.path.isdir(obj):
                print(prefix + os.path.basename(obj))
                traverse(obj, max_depth, depth + 1)
            elif os.path.isfile(obj):
                print(prefix + os.path.basename(obj))
            else:
                print(prefix + 'unknown object:',obj)

def main():
    user_input = input("디렉토리명->")
    # listDir(user_input)
    traverse(user_input)
    
    # f = open(user_input)  ## 입력받은 데이터가 파일인지 디렉토리인지 알 수 있음.
    # file = "C:\work\day01\Day6\\filedemo_03.py"
    # dir = "C:\work\day01\Day6"
    # print(os.path.isfile(file))  ## False
    # print(os.path.isdir(file))   ## True
    # print('파일여부:', os.path.isfile(file))
    # print('파일크기:', os.path.getsize(file))
    # print("파일마지막수정일:", os.path.getmtime(file))
    # print("파일만든날짜:", os.path.getctime(file))
    # print("파일마지막접근일:", time.ctime(os.path.getatime(file)))  ## time.ctime()으로 유닉스 시간을 가독성 있는 시간으로 변환

main()
