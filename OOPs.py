# oops(object oriented programming)
# Syntax

class Person:
    def __init__(my, name) -> None:
        print("__init__ calling........")
        my.my_name = name
        print(my.my_name)
        # print(self)

    def display(my): #class method
        print("display() calling.......")
        print("Hi person!!!")


person = Person("atik"); #create object
person.display()

