class Dog():
    'python构造函数有两个下滑线‘
    '李景龙错误的把init方法写成只有一个下滑线的方法_init_'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + "is now sitting")

my_dog = Dog("white",6)
my_dog.sit()