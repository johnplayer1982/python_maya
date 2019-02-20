# Exploring the self

class Animal(object):

    species = None
    name = None

    # Logging this is pretty pointless, we know its only going to get us that
    # object is an object <type 'object'>
    print 'Object =', object

    def speak(self):

        print 'Hi my name is', self.name, "and I am a", self.species

        # If we print 'self' we get the animal object and its address in memory:
        # Output: <ex_self.Animal object at 0x100f6ae50>
        print 'Self =', self

        # If we print the type of 'self' we get the fact that self is a class and is 'ex_self.Animal'
        # Output: <class 'ex_self.Animal'>
        print 'Self Type =', type(self)

# Create a new class instance for a tiger
# Define the name (tiger.name) and species (tiger.species)
# run this in the python console with:
# ---------------------
# import ex_self as exs
# reload(exs)
# exs.tiger.speak()
# ---------------------
# Output: Hi my name is Keith and I am a big cat

tiger = Animal()
tiger.name = 'Keith'
tiger.species = 'big cat'
