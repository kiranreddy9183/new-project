n=int(input())
c=0
t=n
while(t>0):
    d=t%10
    c=c+(d**3)
    t=t//10
print(c)
if c==n:
    print("yes")
else:
    print("no")
