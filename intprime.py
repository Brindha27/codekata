low=int(input())
up=int(input())
low,up<=10000
for num in range(low,up+1):
  if(num>1):
    for i in range(2,num):
      if(num%i==0):
        break
      else:
        print(num)
