n=int(input("how many numbers")) # read number of values to read
arr=[]
for i in range(1,n+1):
    ele=int(input("add eliments")) # read each value in arrey
    arr.append(ele)
    stor=arr #store values of arr into stor
    stor.sort() #sort function
print(stor)
