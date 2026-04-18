A = {1,2,3,4}
B = {0,1,2}

A ^= B
print(A)

print(B.issubset(A))
print(A.issuperset(B))
print(A.isdisjoint(B))