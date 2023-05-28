n=int(input())
lst=list(map(int,input().split()))
count=0
for i in range(n):
    if lst[i]==1 or lst[i]==0:
        count+=1
    else:
        count-=1
if count==n:
    print(True)
else:
    print(False)