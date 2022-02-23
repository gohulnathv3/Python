# this project is all about working with inputs and strings

# generally madlib is like a word filling game in a paragraph. Here we're making word filling game by using string formats.
# let see how it gonna works.

a = " Hi, how are you"
b = "I'm very good!"
c = f"{a}.\
    \n Yep! we're all fine. And what about you.\
    \n {b}"

print(c)

# other ways to declare variables.

print("Hello"+a)
print("Hello {}".format(a))
print(f"Hello {a}")

a = 1
