#python中的函数
def describe_pet(animal_type,pet_name):
    print("animal_type:" + animal_type + " === pet_name:" + pet_name)

#方法中的默认值
def describe_pet2(pet_name,animal_type="dog"):
    print("animal_type:" + animal_type + " === pet_name:" + pet_name)

#带返回值的函数
def return_function():
    return 1

#返回字典
def return_dict():
    return {"lastname":"yang","firstname":"li"}

if __name__ == "__main__":
    #python中调用方法很有趣的地方
    #这个叫关键字实参 是传递给函数的名称 —— 键值对
    describe_pet(animal_type="hamster",pet_name="harry")
    describe_pet(pet_name="harry",animal_type="hamster")

    describe_pet2("white")

    print(return_function())
    print(return_dict())

    