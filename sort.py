n=int(input())
ls=list(map(int,input().split()))
ls.sort()
for i in range(0,n):
  print(ls[i],end=" ")
