num = int(input())
n = len(str(num))
sqr = num**2
l = sqr%pow(10,n)
if l == num:
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")