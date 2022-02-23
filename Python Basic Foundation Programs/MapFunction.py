l=[1,2,3,4,5,6,7,8,9]
l1=[10,11,13,14,12,15]
result=list(map(lambda x,y: x+y,l,l1))
print(result)
result1=list(map(lambda x,y: x*y,l,l1))
print(result1)

nl=[1,2,3,4,5,6,7,8,9,0]
n2=list(map(lambda x:x+5,nl))
print(n2)