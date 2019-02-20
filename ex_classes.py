# Define the class:
# Class    = We're defining a class
# Animal   = We are naming our class
# (object) =  We are telling the class what to inherit from, in this case we are inheriting from the Python 'object',
# object is the lowest level type inside of python.

class Animal(object):

    # Lets create 2 variables and assign them with None
    name = None
    type = None

    # Define a 'speak' method
    # Print a string which contains both the name and type variables
    def speak(self):
        print "Hi my name is", self.name, "and I am a", self.type

    def walk(self):
        print "I can walk, but not fly!"

# Create a new instance of the Animal() class
tiger = Animal()

# Assign the name variable
tiger.name = 'John'

# Assign the type variable
tiger.type = 'Big cat'

# Evoke the speak method
tiger.speak()

# Output:
# Hi my name is John and I am a Big cat

# Lets create a new class which inherits from the Animal() class: class Dog(Animal)
# We'll assume this new animal cant speak, and can only Woof

class Dog(Animal):

    # Redefine the 'speak' method when called from within the Dog() scope
    def speak(self):
        print "Woof!!"

# Create a new instance of the Dog() class
trevor = Dog()

# Call the speak() method
trevor.speak()
# Output: Woof!!
# We redefined the speak() method in the Dog() class, which will override the method in the Animal() base class with
# the same name

# If we call a method which only exists in the Animal() class
trevor.walk()
# Output: I can walk, but not fly!
# This is because our Dog() class inherits every method from the Animal() base class, and we can access its methods
