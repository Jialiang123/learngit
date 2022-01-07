def bubbleSort(alist):
    exchange = True #是否有交换
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False #刚开始设置成无交换
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1
    print(alist)

