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

