s1=input().lower()
s2=input().lower()
s=""
for i in s2:
    if i not in s1 and i!=" " and i not in s:
        s+=i
for j in s1:
    if j not in s2 and j not in s and j!=" ":
        s+=j
print(len(s)-1)