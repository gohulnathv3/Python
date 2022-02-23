#labmda does not use return statement
#lambda we only use single expression these are all the difference between lambda and funciton

mul=lambda x: x*x

print(mul(5))

l=[1,2,3,4,5,6,7,8,9,0]

newlist= list(filter(lambda x:(x%2==0),l))
newlist1= list(filter(lambda x:(x%2!=0),l))

print(newlist)
print(newlist1)