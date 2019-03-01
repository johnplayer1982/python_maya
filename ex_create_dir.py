# To call from Maya
# ----------------------------------------
# import ex_create_dir as exd
# reload(exd)
# exd.createDirectory()
# ----------------------------------------

# Import the Maya commands library
from maya import cmds

# os module to interact with our operating system
import os

# Query the users Maya application directory
USERAPPDIR = cmds.internalVar(userAppDir=True)
print 'Maya application directory:', USERAPPDIR

# Construct the name of the directory
# Using the application directory and the name of our package
# os.path.join() explained:
# os: operating system
# path: OS specific path seperator (Win = /, mac = \)
# join(): Use the os specific separator to join these 2 things together
DIRECTORY = os.path.join(USERAPPDIR, 'newDirectory')

# Create a function which creates a directory
# Use our constructed path as the default value
def createDirectory(directory=DIRECTORY):

    """
    Creates a given directory if it doesnt already exist
    Args:
        directory(str): The directory to create
    """

    # If the path does not already exist
    if not os.path.exists(directory):

        # We will make the directory
        os.mkdir(directory)
