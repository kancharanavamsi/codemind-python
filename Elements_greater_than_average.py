n=int(input())
lst=list(map(int,input().split()))
count=0
avg=sum(lst)//n
for i in range(n):
    if lst[i]>=avg:
        count+=1
print(count)