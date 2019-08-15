#元组：python将不能修改的值称为不可变的，而不可变的列表被称为元组
if __name__ == "__main__":
    #元组的定义 和集合列表的定义一样
    dimension = (200,50)
    print(dimension[0])
    print(dimension[1])

    #python不允许给元组里面的列表某个字段赋值
    #dimension[0] = 250

    #给元组对象赋值是可以的
    dimension = (250,100)
    


    
