#完整删除整个列表元素  实现
foods = ["egg","beaf","dock"]


# 第一种方式
# print(foods)
# del foods[len(foods):]
# print(foods)

# 第二种方式(最简单的方式)
# foods = []
# print(foods)

#第三种方式
#创建两个列表解决循环删除列表中多个元素的问题
# del_foods = ["egg","beaf","dock"]
# for i in del_foods:
#     foods.remove(i)
# print(foods)

#第四种方式
for i in foods:
    print(foods[:])
    del foods[:]
print(foods)

        