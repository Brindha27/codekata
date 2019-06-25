bri=str(input())
k=0
l=0
m=len(bri)
for i in range(0,m):
  if(bri[i].isalpha()):
    k=k+1
  if(bri[i].isnumeric()):
    l=l+1
if((k==0)or(l==0)):
  print("No")
else:
  print("Yes")
