class MyClass:
    my_number:int
    def __init__(self, number) -> None:
        self.number = number
        self.my_number = number*10
        print("in __init__[self.my_number]     : ", self.my_number)
        self.my_number = number*20
        print("in __init__[self.my_number]     : ", self.my_number)
        MyClass.count = MyClass.my_func(30)

    count = 0
    def my_func(num):
        MyClass.my_number=num*12
        print("in function [MyClass.my_number] : ", MyClass.my_number)
        # print("in function [self.my_number] : ", self.my_number)
        return num*10
    def display_fun(self):
        self.my_number=1210

my_object = MyClass(1)
# print("passing number : ",my_object.number)
print("my_number [my_object.my_number] : ",my_object.my_number)
print("counter : ",my_object.count)
print(my_object.my_number)
my_object.display_fun()
print(my_object.my_number)
my_object.my_number=420
print(my_object.my_number)
print(type(my_object))