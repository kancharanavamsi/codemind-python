n=int(input())
a=list(map(int,input().split()))
k=sorted(a)
if(a==k[::-1]):
    print("yes")
else:
    print("no")