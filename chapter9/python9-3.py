#继承
class Car():
    def __init__(self,name):
        self.name = name
    
    def run(self):
        print("Im running！")

class ElatricCar(Car):
    def __init__(self,name):
        #初始化父类属性
        super().__init__(name)
        #self.name = name

    #重写父类的方法
    # def run(self):
    #     print("my elatic car running!")

my_teala = ElatricCar("iii")
print("my tesla name:" + my_teala.name)
my_teala.run()