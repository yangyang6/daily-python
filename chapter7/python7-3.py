if __name__ == "__main__":
    pisas = ['liulain','zhishi','dangao']
    copy_pisas = []

    #确定列表不为空,如果不为空则为True
    while pisas:
        current = pisas.pop()
        print("current:" + current)
        copy_pisas.append(current)

    print(copy_pisas)