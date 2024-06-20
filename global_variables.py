# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

def my_func():
    global_var = "in function"
    print(f"inside function : {global_var}")

global_var = "Global Variable"
print(f"assign value : {global_var}")

my_func()

print(f"after function calling : {global_var}")

# The global Keyword
# To create a global variable inside a function, you can use the global keyword.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)