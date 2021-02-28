n=int(input("enter limit:"))
d={}
for i in range(0,n):
    k=input("enter keys:")
    v=int(input("enter values:"))
    d[k]=v 
    v=d.values()
r=sorted(list(set(v)))[1]
r1=[]
for k,v in d.items():
    while r==v:
        r1.append(k)
        break
#r1.sort()
for n in r1:
    print(n)
        
