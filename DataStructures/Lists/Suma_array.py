n = int(input())  
a = list(map(int, input().split()))
if len(a) == n:
    g = sum(a)
    
print(g)