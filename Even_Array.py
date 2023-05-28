n=int(input())
lst=list(map(int,input().split()))
count=0
for i in range(n):
    if lst[i]%2==0:
        count+=1
if count==n:
    print(True)
else:
    print(False)
