#定义一个类
class Dog():

    #初始化
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print("sit dog")
    
    def roll_over(self):
        print("roll over")

my_dog = Dog("white",10)
print("my_dog name:" + my_dog.name + "===age:" + str(my_dog.age))
#直接修改对象值
my_dog.name = "hexiao white"
print("my_dog name2:" + my_dog.name + "===age2:" + str(my_dog.age))