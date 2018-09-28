# filedemo_05.py
import os, glob

dir = "C:\work\day01\Day5"
os.chdir(dir)
filter_list = glob.glob('*.txt')
for file in filter_list:
    print(file)
print(glob.glob('*.py'))  ## 확장자가 py인 애들 불러옴
# files = os.listdir(dir)
# for file in files:
#     if file.  ## file sorting하는 방법.
#     print(file)