n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=0
for i in range(len(arr)):
        s=s+arr[i]
        if(i==k-1):
            break
print(s)    