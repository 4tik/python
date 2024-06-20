# Python String Interpolation or Format
from string import Template

# f-strings
name = 'World'
program = 'Python'
print("####### F-strings ##########")
print(f'Hello {name}! This is {program}')

# %-formatting
print("\n####### %-formatting ##########")
print("%s %s" %('Hello','World'))

print('Hello %s! This is %s.'%(name,program))

# Str.format()
print("\n####### Str.format() ##########")

print('Hello, {name}'.format(name=name))

# Template Strings
print("\n####### Template Strings ##########")
new = Template('Hello $name! This is $program.')
print(new.substitute(name=name,program=program))

