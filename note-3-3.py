if __name__ == "__main__":
    cars = ['bmw','audi','toyota','subaru']
    #按首字母排序
    cars.sort()
    print(cars)

    #反序操作
    cars.sort(reverse=True)
    print(cars)


    orgin_cars = ['bmw','audi','toyota','subaru']
    #对列表进行临时排序
    sorted_cards = sorted(orgin_cars)
    reverse_cards = sorted(orgin_cars,reverse=True)
    print(orgin_cars)
    print(sorted_cards)
    print(reverse_cards)

    #反转列表
    orgin_cars.reverse()
    print(orgin_cars)

    null_list = []
    #空列表下的-1索引值会报错
    #print(null_list[-1])
