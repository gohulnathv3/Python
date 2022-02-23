import time 

#we need to set some default fake login details without using db.

username = "user1"
password = "123"

#we need to cross check above credentials by entering manually.

enterUsername = input("User Name: ")
enterPassword = input("Password: ")

#we need to check these credentials using condtional functions. 

if username == enterUsername and password == enterPassword:
    print("Wait, you're credentials are being submitted")
    time.sleep(5)
    print("Please wait")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print("Welcome to this login, now you're eligible to move further with codings!")
elif username != enterUsername and password == enterPassword:
    print("Enter the correct user name please, username is not found or mispelled")
elif username == enterUsername and password != enterPassword:
    print("Entered password is wrong, Please try again with correct password")
else:
    print("Please check you credentials, both username and password are wrong")
