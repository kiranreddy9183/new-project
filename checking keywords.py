import keyword
g=input()
k=keyword.kwlist
#print(k)
if(g in k):
    print(g,"is present")
else:
    print(g,"is not present")
