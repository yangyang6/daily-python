if __name__ == "__main__":
    #练习题
    pisas = ['liulain','zhishi','dangao']
    for pisa in pisas:
        print("I like " + pisa + " pisa")
    print("I really love pisa")

    #生成数字
    for value in range(1,5):
        print(value)

    #从1开始,不断的加2,直到11
    even_number = list(range(1,11,2))
    print(even_number)

    #列表解析,将for循环和创建新元素的代码合并成一行，并自动附加新元素
    squares = [value ** 2 for value in range(1,11)]
    print(squares)

    #python中的切片,输出前三个
    print(squares[0:3])
    #如果没有开始索引,则从最头部开始
    print(squares[:4])
    #如果没有指定结束索引,则一直到最后
    print(squares[1:])

    #打印末尾最后三个值
    print(squares[-3:])

    #复制列表
    my_foods = ['egg','chiken','dark']
    friend_foods = my_foods[:]
    my_foods.append('fish')
    friend_foods.append('ice cream')
    print("my foods:")
    print(my_foods)
    print("friend foods:")
    print(friend_foods)
    