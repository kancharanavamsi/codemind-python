n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in range(n):
    if lst[i]%2==0:
        a.append(lst[i])
for j in range(n):
    if lst[j]%2!=0:
        a.append(lst[j])
print(*a)