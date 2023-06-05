n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
for i in b:
    if i not in c:
        d.append(i)
if len(d)!=0:
    print(*d)
else:
    print(-1)