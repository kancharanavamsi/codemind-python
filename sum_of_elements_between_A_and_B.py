n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(len(arr)):
    if(arr[i]>=a and arr[i]<=b):
        c.append(arr[i])
print(sum(c))        