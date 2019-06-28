k=int(int(input())
l=list(map(str,input().split()))
m=list(input())
b=0
for i in range(K):
  x=(list(l[i])
  for j in range(0,len(x)-len(m)+1):
    if m==x[j:len(m)]:
      b=b+1
      break
print(b)
