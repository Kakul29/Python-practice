# calculator using python
a=float(input("enter first value"))
b=float(input("enter second value"))
print("consider the following instructions : \nto perform addition type 1 \nto perform subtraction type 2 \nto perform multiplication type 3 \nto perform division type 4")
c=int(input("operation to be performed"))
if c== 1 : 
   print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b) 
else:
    print("invalid")
print("done")
