if __name__ == "__main__":
    #python使用 and  or 来结合条件判断 
    #in 表示是否在集合中; not in表示不在集合之中
    #布尔表达式 True False
    age = 10

    #if else
    if age > 9:
        print("age more than 9")

    if age > 10:
        print("age more then 10")
    else:
        print("age less then or equals 10")

    
    #if elif else
    age = 5
    if age > 5:
        print("age more than 10")
    elif age == 5:
        print("age equals 5")
    else:
        print("age more than 5")

    #if的作用：确定列表不为空,如果不为空则为True
    request_topping = []
    if request_topping:
        print("request_topping is at last one")
    else:
        print("request_topping is null")