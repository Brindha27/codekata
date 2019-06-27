k=[int(i) for i in input().split()]
m=k[0]
n=k[1]
k=[int(i) for i in input().split()]
x=0
for i in k:
  if(i==n):
    x=x+1
if(x==0):
  print("no")
else:
  print("yes")
