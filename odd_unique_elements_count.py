n=int(input())
lst=list(map(int,input().split()))
count=0
set11=set(lst)
set1=list(set11)
leng=len(set1)
for i in range(0,leng):
    if set1[i]%2!=0:
        count+=1
print(abs(count))