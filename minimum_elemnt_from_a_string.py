n=input()
n=n[::-1]
n.lower()
for i in n.split():
    k=min(i)
    if k in i and k.lower() in i:
        print(k.lower())
        break
    else:
        print(k)

