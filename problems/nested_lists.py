ls=[]
n=int(input("enter number of students"))
for _ in range(n):
        name = input("enter name")
        score = float(input("enter score"))
        ls2=[]
        ls2.append(name)
        ls2.append(score)
        ls.append(ls2)
print(ls)

ls3=[]
for i,j in ls:
        ls3.append(j)
print(ls3)        
ls4=[]
for i in ls3:
        if i not in ls4:
                ls4.append(i)
ls4.sort()  
print(ls4)             

second_lowest=ls4[1]  
ls2=[]
for i,j in ls:
        if j ==second_lowest:
                ls2.append(i)
ls2.sort()
print(ls2)
for i in ls2:
        print(i)  
