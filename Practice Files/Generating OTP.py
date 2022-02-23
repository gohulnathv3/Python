import random #it is one builtin modeule from python.
numbers='1234567890'
print("Enter 1 if you want 4 digit OTP for user login")
print("Enter 2 if you want 6 digit OTP for user login")

i = 0
while i<3:
    digits = int(input("Enter 1 or 2: "))
    if digits==1:
        otp=random.randint(1000,9999)
        print(otp)
    elif digits == 2:
        otp=random.randint(100000,999999)
        print(otp)
    else:
        print("Enter 1 or 2 otherwise it's invalid")
    i+=1
#for visuals: www.pytutor.com
#randint method

