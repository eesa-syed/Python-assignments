def reverse(x):
    if(x%2==1):
        for i in range(x,0,-2):
            print(i)
    else:
        x-=1
        for i in range(x,0,-2):
            print(i)
y=int(input("input a number "))
reverse(y)