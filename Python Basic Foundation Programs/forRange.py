#range funciton is used to create a range.
print(range(10))
print(list(range(10)))

print(range(3,8))
print(list(range(3,8)))

print(list(range(2,20,5)))
#range(start,end,stepsize)
#in general it takes stepsize of 10
print(list(range(3,25,2)))

# range(1,8) various ways to set range
# range(2,20,3)
# range(10)
l=['sun','moon','earth','a']

for i in range(len(l)-1):
    print(l[i])

