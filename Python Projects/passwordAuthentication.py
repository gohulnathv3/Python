import getpass

from click import password_option
database = {"Gohul": "170398", "Priya": "170398",
            "Sujatha": "12345", "Vadivelu": "12345"}
username = input("Enter username: ")
password = getpass.getpass("Enter your password: ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass(
                "Please try again with correct password: ")
        break

print(f"You logged in!, Welcome {username}")
