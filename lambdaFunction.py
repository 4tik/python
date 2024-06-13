# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# can take n number of arguments at a time. But it returns only one argument at a time
# anonymous functions, implying they don't have a name

# Syntax : lambda arguments : expression
add = lambda num : num+4
print(f"output : {add(4)}")

# filter
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]      
# squared_list = list(map( lambda num: num ** 2 , numbers_list ))  
mapping_list = list(
    map(
        lambda num: (num % 2 != 0), numbers_list
    )
)

filter_list = list(
    filter(
        lambda num:(num>5), numbers_list
    )
)

print("map lambda : ", mapping_list)
print("filter lambda  ", filter_list)
# print( 'Square of each number in the given list:' ,squared_list ) 