k=input()
m=input().split()
x=0
y=input()
for i in m:
  if y==i[:len(y)]:
    x+=1
print(x)
    
