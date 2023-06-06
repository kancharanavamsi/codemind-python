n=input()
s=[]
for i in n:
    if i in "AEIOUaeiou" and i not in s:
        s.append(i)
if len(s)==0:
    print(-1)
else:
    print(*s)