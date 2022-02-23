# this project is all about working with inputs and strings

# generally madlib is like a word filling game in a paragraph. Here we're making word filling game by using string formats.
# let see how it gonna works.

# a = " Hi, how are you"
# b = "I'm very good!"
# c = f"{a}.\
#     \n Yep! we're all fine. And what about you.\
#     \n {b}"

# print(c)

# # other ways to declare variables.

# print("Hello"+a)
# print("Hello {}".format(a))
# print(f"Hello {a}")

# a = 1

# do you want to uncomment above. First select the text/code and press ctrl+k+u (uncomment) and ctrl+k+c (comment)

# inputs
adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous person: ")

# logic
madlib = f"Python programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}, Stay hyderated and {verb2} like you are {famous_person}!"

# output
print(madlib)
