def factorial(k):
    if k==1:
        return 1
    else:
        return (k*factorial(k-1))
#above one is recursive funciton
k=int(input("Enter the number to find factorial: "))
print("Factorial of given number is",factorial(k))