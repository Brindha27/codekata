n=input()
x=0
for i in range(len(n)):
  if(n[i].isdigit() or n[i].isalpha() or n[i]==(' ')):
    continue
  else:
    x+=1
print(x)
