n=int(input())
fib,x=0,1
print(x,end=" ")
for i in range(1,n):
  y=fib+x
  print(y,end=" ")
  fib,x=x,y
