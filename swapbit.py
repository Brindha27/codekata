a,bp=map(int,input().split())
a=a^bp
bp=a^bp
a=a^bp
print(a,bp)
