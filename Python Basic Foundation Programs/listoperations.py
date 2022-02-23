a=[1,2,3,4,5,6,7,8,9]

print(a[1:3])
print(a[:6])
print(a[:3])
print(a[:-6])
print(a[:])

b=[1,3,5,7,9]

print(b[2])

b[2] = 10
print(b[:])

b[1:3] = [20,30]
print(b[:])