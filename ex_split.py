# Split a string into a list

# Create a new string
string = "Hello my name is John"

# <type 'str'>
print type(string)

# Output = Hello my name is John
print string

# Split the string into a list
list = string.split()

# <type 'list'>
print type(list)

# Output = ['Hello', 'my', 'name', 'is', 'John']
print list

# Select specific items in the list
print list[0]   # Hello
print list[1]   # my
print list[2]   # name
print list[3]   # is
print list[4]   # John
print list[-1]  # John
