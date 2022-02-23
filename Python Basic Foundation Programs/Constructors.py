
#it is like methods
#two types... default constructor, parameterized constructor
#default constructor
class geek:
    def __init__(self):  #constructor
        self.geek="geeks"

    def print_geek(self): #method
        print((self.geek))

obj=geek()
obj.print_geek()

#parameterized constructor
class add:
    first=0
    second=0
    addition=0

    def __init__(self,f,s):
        self.first=f
        self.second17=s

    def display(self):
        print("First number is ",self.first)
        print("second number is :",self.second)
        print("Additio"vjharis

    def calculate(self):
        self.addition = self.first+self.second

object=add(100,200)
object.calculate()
object.display()
