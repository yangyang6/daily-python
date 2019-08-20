#函数的导入
def make_pizza(size,*toppings):
    print("marking size:" + str(size))

    for topping in toppings:
        print("topping:" + topping)