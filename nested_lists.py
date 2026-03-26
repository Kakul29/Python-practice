#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


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
#print(ls)
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
#print(ls3)
second_lowest=ls4[1]  
ls2=[]
for i,j in ls:
        if j ==second_lowest:
                ls2.append(i)
ls2.sort()
print(ls2)
for i in ls2:
        print(i)                
                     
