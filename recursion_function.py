#recursion factorial  function
def factorial(number=1):
  return number*(factorial(number-1)) if(number>1) else  1

print(factorial(5))