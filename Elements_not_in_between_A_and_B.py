n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
mi=0
c=0
for i in range(n):
    if lst[i]<a or lst[i]>b:
        print(lst[i],end=' ')
        c+=1
if c==0:
    print("-1")
