# def fn(name,msg="hello"):
#     print("my name is ",name+','+msg)
#
# fn("Gohul")
# fn("Gohul","I'm a data scientist")

def stu_name(*name):
    for names in name:
        print("My name is ",names)
stu_name("Gohul")
stu_name("Abi")
stu_name("Akash","Ajay")
