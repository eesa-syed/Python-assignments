x=input("input a character ")
if (len(x)>1):
    print("Error, please enter only one character")
elif (65<=ord(x)<=90 or 97<=ord(x)<=122):
    print("its a Alphabit")
elif (48<=ord(x)<=57):
    print("its a Number")
else: print("it is a special character")