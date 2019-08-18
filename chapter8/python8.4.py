def greet_users(names):
    for name in names:
        print ("hello : " + name)
    
#python中不用main方法也可以运行方法也，这样不同于java
usernames = ["yang","li","he"]
greet_users(usernames)


unprinted_designs = ["iphone_case","robot_pendant","yyy"]
completed_models = []
def print_mode(unprinted_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("current_design:" + current_design)
        completed_models.append(current_design)

#参数的传递，由于方法里对参数变量做了操作导致列表数据为空
print_mode(unprinted_designs)
print(unprinted_designs)

unprinted_designs2 = ["zzz","xxx","ccc"]
completed_models2 = []
#传递的是列表的副本,不改变列表本身的值，是改变的副本的值
print_mode(unprinted_designs2[:])
print(unprinted_designs2)


