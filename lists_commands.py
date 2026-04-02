N = int(input())
ls=[]
for i in range(N):
        command,*line=input().split()
        line=list(map(int,line))
        if command=='insert':
            ls.insert(line[0], line[1])
        elif command=='print':
            print(ls)
        elif command=='remove':
            ls.remove(line[0])
        elif command=='append':
            ls.append(line[0])
        elif command=='sort':
            ls.sort()
        elif command=='pop':
            ls.pop()
        elif command=='reverse':
            ls.reverse()