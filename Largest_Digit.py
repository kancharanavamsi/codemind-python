n=int(input())
l=0
while n:
    d=n%10
    n=n//10
    if l<d:
        l=d
print(l)