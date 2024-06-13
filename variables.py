# about python variables
# print(2+2);
number_1 = 5
number_2 = 7
my_name = "atikur rahman"

# print(number_1+number_2)
# print(number_1*number_2)

number_2="new namwe"
# print(number_2)
# print(type(number_2))


# find variabls data types
# print(type(number_1))
# print(type(my_name))

# Object Identity 
# to find this python using id(variabler_name)
print("=================================================================================")
number1 = 10;
number2 = number1;
print("Object Identity->number1 : ", id(number1))
print("Object Identity->number2 : ", id(number2))

# variable value assign
a=10
a,b,c = 10,12,20
a=b=c=10

numbers = [1,2,3]
# a=numbers[0]
# b=numbers[1]
# c=numbers[2]

a,b,c = numbers # unpack collection

# print(a,b,c)

# variables are two types 1. Global and 2.local
global_value = 10

# if True:
#     print("start if condition")
#     in_value = 54 #local variale
#     print(in_value)
#     print(global_value)
#     print("end if condition")

# print(in_value)

# delete variable
delete_variable = "delete data"
print (delete_variable)
del delete_variable
print(delete_variable)

# variable case type 
#  1. Camel Case ->   nameOfStudent
#  2. Pascal Case ->  NameOfStudent
#  3. Snake Case ->   name_of_student