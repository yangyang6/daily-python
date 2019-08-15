#python中字典的概念
#比如实体的意思是一个外星人对象
if __name__ == "__main__":
    alien0 = {"color":"green","points":"5"}
    print(alien0["color"])
    print(alien0["points"])

    #字典里面的值的添加
    alien0["x_position"] = 0
    alien0["y_position"] = 20
    print(alien0)

    #空字典对象
    alien1 = {}

    #修改字典中的值
    alien0["x_position"] = 20
    print(alien0)

    #删除字典中的键值
    del alien0["x_position"]
    del alien0["y_position"]
    print(alien0)

    #对字典的遍历
    #!!! 注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系
    #上面这种情况还真没遇到过额
    for key,value in alien0.items():
            print("key:" + key)
            print("value:" + value)

    favorite_language = {
        "jen":"python",
        "sarah":"c",
        "eder":"ruby",
        "joy":"java",
        "phil":"python",
        "yang":"java"
    }
    for key,value in favorite_language.items():
        print("key:" + key + " === value:"+ value)

    #遍历keys值
    for key in favorite_language.keys():
        print("=====key:"+key)

    for value in favorite_language.values():
        print("=====value:"+value)

    if "long" not in favorite_language.keys():
        print("long is not in keys")

    if "java" in set(favorite_language.values()):
        print("java in favorite_lang values set")