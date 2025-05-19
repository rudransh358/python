a,b=[int(x) for x in input("enter any two number:").split()]
opt=input("The type of operation:")
if(opt=="sum"):
    result=a+b
    print(result)
    print("the sum of the two number",)
elif(opt=="mul"):
    result=a*b
    print(result)
    print("the product of the number ")
elif(opt=="div"):
    result=a/b
    print(result)
    print("the division of the number")
elif(opt=="sub"):
     result=a-b
     print(result)
     print("the sub of the number")
else:
    print("no operation")
