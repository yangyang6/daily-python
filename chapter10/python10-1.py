#注意这里是mac或者linux环境，windows是反斜杠
dirPath = "/Users/yangli/Project/python/basePython/daily-python/chapter10/data1.txt"
with open(dirPath) as file_object:
    '一次性读取'
    #contents = file_object.read()
    '该输出会多一个空行，要去掉空行可以使用下面的方法'
    #print(contents)
    #print(contents.rstrip())

    for line in file_object:
        print(line.rstrip())