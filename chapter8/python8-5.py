#传可变参的
def make_pizza(*topping):
    print(topping)

#观察输出的是一个元组，形参名*topping中的星号让python创建了一个名为topping的空元组，并将受到的参数值存放在元组中
make_pizza("soga")
make_pizza("solt","noddle","vegatable")

#将实参和可变参混合使用的时候，可变参要放在方法参数最后 —— 这个仿佛是和java一样


#接受任意数量的实参