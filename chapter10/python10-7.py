# try:
#     print(4/0)
# except ZeroDivisionError:
#     print("has error")



#一声不吭
try:
    print(4/0)
except ZeroDivisionError:
    pass
else:
    #不会输出
    print("else")