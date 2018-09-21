# file_practice2.py
f = None
try:
    # f = open('my_test.txt', encoding="utf-8")  # 내가 해본 것
    f = open('my_text.txt', 'rb')
    text = f.read().decode('utf-8')
    print(text)
except FileNotFoundError:
    print("해당 파일이 존재하지 않습니다.")
finally:
    if not (f is None):
        f.close()


# try:
#     f = open('live.txt')
# except FileNotFoundError:
#     print("해당 파일이 존재하지 않습니다.")
# else:
#     text = f.read()
#     print(text)
# finally:
#     f.close()