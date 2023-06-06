s=input().split()
b=0
for i in s:
    if i[0] in "aeiouAEIOU":
        if i[-1] not in "aeiou":
            b+=1
print(b)
    