age = 16;
print("My age is :", age)
print("----------------------------")

#different kinds of variables
emp_id = 11
name = 'Atikur Rahman'
salary = 2000.40

print("Employee ID : ", emp_id)
print("Name : ", name)
print ("Salary : ", salary)

print("---------------------------")

#type() used to check the data type of the variables.
print("Employee ID Type : ", type(emp_id))
print("Name Type : ", type(name))
print ("Salary Type : ", type(salary))

print("-------------------------------")

#Built-in data types

print("** Numeric Data Type **")
myValue = 193874
print(myValue);
print(type(myValue))

print("-------------------------------")
print("** Float Data Type **")
myValue = 193874.876
print(myValue);
print(type(myValue))


print("-------------------------------")
print("** Complex Data Type **")
a = 3+5j
b = 2-5.5j
c = 3+10.5j
print(a)
print(b)
print(c)
print()
print(a+b)
print(b+c)
print(c+a)


print("-------------------------------")
print("** Bool Data Type **")
a = True
b = False
print(a)
print(b)
print(a+a)
print(a+b)


print("-------------------------------")
print("** None Data Type **")
a=None
print(a)
print(type(a))

print("-------------------------------")
print("** Bytes Data Type **")
x = [10, 20, 100, 40, 15]
y = bytes(x)
print(y[0])
print(type(y))

for a in y:
    print(a)


print("-------------------------------")
print("** Range Data Type **")
a = range(5)
print(a)
print(type(a))
for value in a:
    print(value)

