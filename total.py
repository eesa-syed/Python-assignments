n=int(input())
if n>=0:
    tot=sum(range(0,n+1))
    avg=(n+1)/2
    print('total: %d \n average: %f'%(tot,avg))
else: print('try again')