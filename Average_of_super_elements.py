n=int(input())
lst=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    h=0
    for j in range(n):
        if lst[i]==lst[j]:
            h+=1
    if h==lst[i]:
        s+=lst[i]
        c+=1
        lst[i]=0
if c==0:
    print("-1")
else:
    avg=s/c
    print("%.2f"%avg)