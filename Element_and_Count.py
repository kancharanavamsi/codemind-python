n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if i not in c:
        print(i,'',end='')
        print(a.count(i),'',end='')
        c.append(i)