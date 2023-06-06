n=input()
b=[]
for i in n:
    if i in "abcdefghijklmnopqrstuvwxyz":
        b.append(i)
print(len(b))