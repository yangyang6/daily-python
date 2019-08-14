#第三章阅读笔记
if __name__ == "__main__":
    #集合类型用[]标识
    color = ['yellow','red','green']
    print(color)

    print(color[0])

    #访问最后一个元素,快捷方法
    print(color[-1])

    #添加元素,从元素末尾添加
    color.append('pink')
    print(color)

    #从指定区域插入
    color.insert(0,'gray')
    print(color)

    #使用del删除数据，可以任意删除
    del color[0]
    print(color)

    #pop 类似于栈的弹出，并可以得到它的值
    pinkColor = color.pop()
    print(color)
    print("pinkColor:" + pinkColor)

    #还可以具体弹出某个索引下的值
    yellowColor = color.pop(0)
    print("yellowColor:" + yellowColor)

    print(color)
    #根据值删除
    color.remove('red')
    print(color)