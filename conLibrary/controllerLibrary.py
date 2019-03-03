# To call from Maya
# ----------------------------------------
# from conLibrary import controllerLibrary
# reload(controllerLibrary)
# controllerLibrary.createDirectory()
# ----------------------------------------

# Import our modules:
# Import the Maya commands library
from maya import cmds

# os module to interact with our operating system
import os

# json module to write out data
import json

# pprint allows us to pretty up our data to make it more readable
import pprint

# Query the users Maya application directory
USERAPPDIR = cmds.internalVar(userAppDir=True)
print 'Maya application directory:', USERAPPDIR

# Construct the name of the directory
# Using the application directory and the name of our package
# os.path.join() explained:
# os: operating system
# path: OS specific path seperator (Win = /, mac = \)
# join(): Use the os specific separator to join these 2 things together
DIRECTORY = os.path.join(USERAPPDIR, 'controllerLibrary')
print 'Controller Library directory:', DIRECTORY

# Create a function which creates a directory
# Use our constructed path as the default value
def createDirectory(directory=DIRECTORY):

    """
    Creates a given directory if it doesnt already exist
    Args:
        directory(str): The directory to create
    """

    # If something went wrong and a path does not already exist
    if not os.path.exists(directory):

        # We will make the director
        os.mkdir(directory)

# Create a class to manage our controllers
# Inherits from dict, dictionarys are a good way to save
# information about something, as we can include a name, details and screenshots of a single item
class ControllerLibrary(dict):

    # Create the save method
    # We add the 2 parameters that are required for us to save our file
    # The name and the directory, we'll default the directory to what we deined
    # earlier (see line 31)
    def save(self, name, directory=DIRECTORY):

        # Lets call the createDirectory() function to create the directory if we havent already
        # We tell is to use the value in the class variable 'directory' (see 59)
        createDirectory(directory)

        # Create the path that we will be saving to
        # Use string substitution to construct the filename
        # directory = Either the default directory or one we provide in the function call
        # '%s.ma' =  We substitute %s with our 'name' and .ma is the maya file extension
        path = os.path.join(directory, '%s.ma' % name)

        # Rename the file to what we specified in 'path', above on line 69
        cmds.file(rename=path)

        # If we only want to save the selection and not all objects to the new maya file
        if cmds.ls(selection=True):
            cmds.file(type='mayaAscii', force=True, exportSelected=True)
        else:
            # If no objects are selected save the file, and define the file type
            # force=True = if the file already exists we want to save over it (by force)
            cmds.file(save=True, type='mayaAscii', force=True)

        # To test we can create a new instance of our library class in the Maya script editor
        # -------------------------------------------------------
        # from conLibrary import controllerLibrary
        # reload(controllerLibrary)
        # lib = controllerLibrary.ControllerLibrary()
        # lib.save('test')
        # -------------------------------------------------------
        # Go to the maya application folder to confirm the new maya file has been created

        # To prevent us having to run lib.find() each time we save a new file to refresh our library
        # We can update the dictionary (self) with the path each time we save
        self[name] = path

    # Create a find method to find our files
    # Define the directory, We'll use the directory we have already defined (line 31)
    def find(self, directory=DIRECTORY):

        # Create an if statement to catch if the directory path doesn't exist (DIRECTORY)
        # os.path.exists = Check for the existence of the directory we pass as an argument
        if not os.path.exists(directory):

            # return = We wont continue, halt this method here!
            return

        # Therefore if the directory does exist we need to list the files
        # Create a new variable to store the file list in:
        # os.listdir = list the files in the directory given as an argument
        files = os.listdir(directory)

        # Our files variable will contain a list of ALL files
        # We only want .ma maya files in our library
        # Lets exclude all other files
        # We'll use list comprehension
        mayaFiles = [f for f in files if f.endswith('.ma')]

        # This is the same as doing the following, but more efficient:
        # --------------------------
        # mayaFiles = []
        # for f in files:
        #    if f.endswith('.ma'):
        #        mayaFiles.append(f)
        # --------------------------

        print 'Maya files in directory:', mayaFiles

        # Now we have found our maya files, we can loop through them
        # and add them to our dictionary:
        for ma in mayaFiles:

            # We just need the name, not including the extension (.ma)
            # This will split the extension (ma) and the filename
            # It returns the name and the extension
            name, ext = os.path.splitext(ma)

            # Now we have the names we need to store this in our dicitonary along with the path to the file
            # Construct the path to the directory based on the file we are on in the list (ma in mayaFiles)
            # os.path.join(path, path) = Accepts 2 argument, 2 paths to join
            path = os.path.join(directory, ma)

            print 'Path:', path

            # Remember that this is a dictionary, and we defined this class as
            # one on line 53 (class ControllerLibrary(dict)
            # Assign the dictionary key 'name' to the path we have just constructed using the .join command

            self[name] = path

            # If we now run the following in Maya
            # print lib
            # We get back a dictionary with a key (the file name) and a value (the path to the file)
            # {u 'key' , u '/path/to/file', u 'key' , u '/path/to/file', u 'key' , u '/path/to/file'}

        # We can make the output of the dictionary easier to read using the pprint module:
        # pprint = Use the pretty print module
        # pprint.pprint = to pretty print
        # pprint.pprint(self) = self, which is our dictionary
        pprint.pprint(self)

        # This will print each dictionary entry to a single line, improving readbility
        # {u 'key', u '/path/to/file',
        #  u 'key', u '/path/to/file',
        #  u 'key', u '/path/to/file',
        # }

    # Load the files back in to Maya
    # Create a load method
    # Pass it the 'name' to load
    def load(self, name):

        # Get the path
        path = self[name]

        # import the file
        # i=True : Import = True
        # usingNamespaces = False : Our controller wont be imported into a secondary namespace
        #
        cmds.file(path, i=True, usingNamespaces=False)

        # We can now import our test controller using:
        # --------------------------------------------
        # from conLibrary import controllerLibrary
        # reload(controllerLibrary)
        # lib = controllerLibrary.ControllerLibrary()
        # lib.find()
        # lib.load('test')
        # --------------------------------------------

