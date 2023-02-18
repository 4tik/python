#Strings

print("Strings\n---------")
name = "Balayya"
emp_id = 20
print("Name of the employee: ", name)
print("employee id is :", emp_id)

#triple single and triple-double quotes
print("If you want to create multiple lines of string, then triple single or triple-double quotes are the best to use.")
print()
loc1 = """XYZ company
While Field
Bangalore"""
loc2 = """XYZ company
Banglore
Human tech park"""
print(loc1)
print()
print(loc2)
print()

#single and double quotes inside a string

s1 = "Welcome to 'python' learning"
s2 = 'Welcome to "python" learning'
s3 = """Welcome to 'python' learning"""
print(s1)
print(s2)
print(s3)

print()

#Slicing 
wish = "Hello World"
print(wish[::])
print(wish[:])
print(wish[0:9:1])
print(wish[0:9:2])
print(wish[2:4:1])
print(wish[::2])
print(wish[2::])
print(wish[:4:])
print(wish[-4:-1])
print()

#in operator
print('p' in 'python')
print('z' in 'python')
print('on' in 'python')
print('pa' in 'python')

#find substring in the main string
print()
print("find substring in the main string\n--------------------")

mainString = "find substring in the main string"
subString = "main"
if subString in mainString:
    print(subString, " => Found")
else:
    print("Not Found")

print("\n## Predefined methods to remove spaces in Python ##\n")

stringValue = "remove spacess  "
print("Befor remove space : ", len(stringValue))
print("After remove space : ", len(stringValue.rstrip()))

course = "python programming language"
print(course.find('p'));
print(course.find('p',1,20))
print("Find Index : ", course.index("language"))

















