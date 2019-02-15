# Split a string into a list

# Import maya commands library
from maya import cmds

# Create a new string
string = "Hello my name is John"
print string
# Output = Hello my name is John

# Split the string into a list
list = string.split()
print list
# Output = ['Hello', 'my', 'name', 'is', 'John']

# Select specific items in the list
print list[0]   # Hello
print list[1]   # my
print list[2]   # name
print list[3]   # is
print list[4]   # John
print list[-1]  # John
