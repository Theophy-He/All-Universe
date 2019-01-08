def hanoi_tower(n,x,y,z):
    if n==1:
        print(x,"->",z)
    else:
        #将n-1个盘子从x->y
        hanoi_tower(n-1,x,z,y)
        #将剩余的最后一个盘子从x->z
        print(x,"->",z)
        #将剩余的n-1个盘子从y->z
        hanoi_tower(n-1,y,x,z)

n = int(input("Please input number of Tower's floor:"))

hanoi_tower(n,"A","B","C")