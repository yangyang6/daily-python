if __name__ == "__main__":
    #input 用于接收用户的输入
    message = input("tell me,you say:")
    print(message)

    age = input("how old are you :")
    print(age)

    #会报错,接收的是一个字符串
    #print(age > 19)
    
    #转一下就ok
    print(int(age))

    #while的使用
    current_number = 1
    while current_number < 5:
        print("current_number:" + str(current_number))
        current_number += 1

        if current_number == 2:
            continue
        
        if current_number == 3:
            break