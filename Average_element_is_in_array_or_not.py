n=int(input())
lst=list(map(int,input().split()))
x=[lst[i] for i in range(n)]
p=sum(x)//n
print(p in lst)