
n = int(input())
a = list(map(int, input().split()))[:n]
m=max(a)
while(max(a)==m):
    a.remove(max(a))
print(max(a))
    
