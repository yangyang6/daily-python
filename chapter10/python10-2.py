filename = "/Users/yangli/Project/python/basePython/daily-python/chapter10/data1.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.strip())

    