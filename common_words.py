s=input().split()
l=input().split()
for i in l:
    for j in s:
        if(i.lower()==j.lower()):
            print(j.lower(),end=" ")
            