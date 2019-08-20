#直接导入的方法
#import pizza 
#调用模块的话 声明前缀pizza
#如果导入了整个模块，使用其中的函数 module_name.function_name()
#pizza.make_pizza(10,"cheese","tosi")

#导入文件和方法名,给方法别名
from pizza import make_pizza as mp

#下面是四种常见的导入方式
import pizza
from pizza import make_pizza
import pizza as pi
from pizza import *
mp(10,"cheese","tosi")

