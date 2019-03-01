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
