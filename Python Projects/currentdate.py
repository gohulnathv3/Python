import datetime
from datetime import date, datetime

today = date.today()
print("Today date is:", today)

todaywithtime = datetime.now()
print("Today with current time: ", todaywithtime)

# Python3 code to demonstrate
# attributes of now()

# importing datetime module for now()

# using now() to get current time
current_time = datetime.now()

# Printing attributes of now().
print("The attributes of now() are : ")

print("Year : ", end="")
print(current_time.year)

print("Month : ", end="")
print(current_time.month)

print("Day : ", end="")
print(current_time.day)

print("Time: ", end="")
print(current_time.hour)

print("Minutes ", end="")
print(current_time.minute)

print("Seconds ", end="")
print(current_time.second)
