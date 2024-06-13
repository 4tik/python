import random

#This is Basic program in python
print("Welcome to python program")
a = 50  
b = a  
print(id(a))  
print(id(b))  
# Reassigned variable a  
a = 500  
print(id(a))
output = f'random number : {random.randrange(1, 5)}'
print(output)

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "Hello, World!"
i=-1
while i!=-len(txt)-1:
    print(txt[i], f'index-> {i}')
    i-=1

print(txt[-1:5])

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    pass
  print(x)

for x in range(2, 30, 3):
   print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)