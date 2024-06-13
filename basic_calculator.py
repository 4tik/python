# basic calculator programm for two numbers

def addition(first_number=0, second_number=0):
    return first_number+second_number;

def subtraction(first_number=0, second_number=0):
    return first_number-second_number;

def multiplication(first_number=1, second_number=1):
    return first_number*second_number;

def division(first_number=1, second_number=1):
    return "Invalid" if second_number==0 else first_number/second_number;


first_number = 13
second_number = 0

print(f"Addition : {addition(first_number, second_number)}");
print(f"Subtraction : {subtraction(first_number, second_number)}");
print(f"Multiplication : {multiplication(first_number, second_number)}");
print(f"Division : {division(first_number, second_number)}");
