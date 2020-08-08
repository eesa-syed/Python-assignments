def divisiblity(lb,ub):
    for i in range(lb,ub):
        if(i%6==0 and not(i%100==0)):
            print(i)
lb=int(input("input lower bound number :"))
ub=int(input("input upper bound number :"))
divisiblity(lb,ub)
