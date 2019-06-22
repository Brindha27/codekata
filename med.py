n=int(input())
ls=list(map(int,input().split()))
ls.sort()
a=ls[int(n/2)]
print(a)
