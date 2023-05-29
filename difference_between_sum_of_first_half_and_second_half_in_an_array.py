n=int(input())
arr=list(map(int,input().split()))
first=arr[:n//2]
second=arr[n//2:]
print(abs(sum(first)-sum(second)))
