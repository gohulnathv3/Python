str = "moam"

str=str.casefold()
#for case sensitive string

str1=reversed(str)
#reversed the string

if list(str)==list(str1):
    print("it is palindrome string")
else:
    print("It is not palindrome String")