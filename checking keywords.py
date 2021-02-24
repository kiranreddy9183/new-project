import keyword
g=input()
k=keyword.kwlist
#print(k) [If we want to print all keywods in python we have to remove '#']
if(g in k):
    print(g,"is present")
else:
    print(g,"is not present")
