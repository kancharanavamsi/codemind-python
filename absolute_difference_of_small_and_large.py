n=input().split()
k=[]
for i in n:
    a=ord(min(i))
    b=ord(max(i))
    k.append(abs(a-b))
print(*k)