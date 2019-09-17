#装饰器模式
import time
# def display_time(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print((t2-t1))
#     return wrapper

# def display_time(func):
#     def wrapper():
#         t1 = time.time()
#         result = func()
#         t2 = time.time()
#         print("Total time: {:4}s".format(t2-t1))
#         return result
#     return wrapper

#带参数的装饰器模式
def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("Total time: {:4}s".format(t2-t1))
        return result
    return wrapper

#判断是否是素数

def is_prime(num):
    if(num <2):
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

# 最原始的
# @display_time
# def print_prime():
#     for i in range(2,10000):
#         if is_prime(i):
#             print(i)

# 中间
# @display_time
# def print_prime():
#     count = 0
#     for i in range(2,10000):
#         if is_prime(i):
#             count = count + 1
#     return count


@display_time
def print_prime(maxNum):
    count = 0
    for i in range(2,maxNum):
        if is_prime(i):
            count = count + 1
    return count

# print_prime();
#不带参数调用方法
# count = print_prime()
#带参数调用方法
count = print_prime(5000)
print(count)
