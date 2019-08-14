#练习题
if __name__ == "__main__":
    mingdan = ['yang','he','wang','yangsuiqun','yanghua']
    print(mingdan)

    print(mingdan[3] + "无法共进晚餐")

    mingdan[3] = "yangchunhai"

    print(mingdan)

    #插入到开头
    mingdan.insert(0,'jianchuluo')
    print(mingdan)

    #插入到中间
    mingdan.insert((len(mingdan) // 2),'yangyongyong')
    print(mingdan)

    #插入到末尾
    mingdan.append("yangyonggang")
    print(mingdan)

    #删除第一位嘉宾
    mingdan.pop(0)
    print(mingdan)


