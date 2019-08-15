#集合与集合之间的赋值
#注意与python4-1.py中的[:]这种方式的复制的区别
if __name__ == "__main__":
    my_foods = ['pizza','falafel','carrot cake']
    friends_foods = my_foods
    print(my_foods)
    print(friends_foods)

    my_foods.append('canoli')
    print(my_foods)
    print(friends_foods)

    friends_foods.append('ice cream')
    print(my_foods)
    print(friends_foods)

   