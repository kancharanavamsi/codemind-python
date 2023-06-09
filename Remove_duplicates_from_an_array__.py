n=int(input())
l=list(map(int,input().split()))
l=list(dict.fromkeys(l))
for i in l:
    print(i,end=" ")
