r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
lst=[]
for i in range(c):
    s=0
    for j in range(r):
        s+=mat[j][i]
    lst.append(s)
print(max(lst))