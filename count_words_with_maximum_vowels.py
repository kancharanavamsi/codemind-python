def vowel(n):
    v=0
    for i in n:
        if i in "AEIOUaeiou":
            v+=1
    return v
n=list(input().split())
x=[]
for i in n:
    x.append(vowel(i))
a=max(x)
print(x.count(a))