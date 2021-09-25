x=int(input())
y=int(input())
n=int(input())
c=0
t=n
if(x<=100 and y>=200):#if the number is in limit of x,y ,proceed and chech for logic
    #while(t>0):
        d=t%10
        c=c+(d**3)
        t=t//10
    print(c)
    if c==n:
        print("yes")
    else:
        print("no")
else: #if the number is not in between x and y
    print("error")
