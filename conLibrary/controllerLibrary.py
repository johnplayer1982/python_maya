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
# Inherits from dict, dictionaries are a good way to save
# information about something, as we can include a name, details and screenshots of a single item
class ControllerLibrary(dict):

    # Create the save method
    # We add the 2 parameters that are required for us to save our file
    # The name and the directory, we'll default the directory to what we defined
    # earlier (see line 31)
    # **info allows us to save any additional arguments passed into this function
    # **info allows for extra user flexibility to save any information, useful for our .json feed
    # Any arguments which aren't defined in our function below (name, directory) will be stored in the **info variable
    # **info is a dictionary by default
    # screenshot=True : We want to save a screenshot of our controller
    def save(self, name, directory=DIRECTORY, screenshot=True, **info):

        # If we pass not additional arguments to the function:
        # -------------------------------------------
        # from conLibrary import controllerLibrary
        # reload(controllerLibrary)
        # lib = controllerLibrary.ControllerLibrary()
        #
        # lib.save('test2')
        # -------------------------------------------
        # info will return an empty dictionary: {}
        # However if we pass any random args:
        # -------------------------------------------
        # from conLibrary import controllerLibrary
        # reload(controllerLibrary)
        # lib = controllerLibrary.ControllerLibrary()
        #
        # lib.save('test2', chicken=True, rice='nice')
        # -------------------------------------------
        # Then info will contain the additional arguments:
        # {'chicken': True, 'rice': 'nice'}
        print 'Info, see line 63:', info

        # Lets call the createDirectory() function to create the directory if we havent already
        # We tell is to use the value in the class variable 'directory' (see 59)
        createDirectory(directory)

        # Create the path that we will be saving to
        # Use string substitution to construct the filename
        # directory = Either the default directory or one we provide in the function call
        # '%s.ma' =  We substitute %s with our 'name' and .ma is the maya file extension
        path = os.path.join(directory, '%s.ma' % name)

        # Create a path for the json file
        # This is similar to the .ma file above, this is our info file
        infoFile = os.path.join(directory, '%s.json' % name)

        # Because we know that **info is a dictionary by default
        # we should add some more information to it, like a name and path
        info['name'] = name
        info['path'] = path

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

        # Save a screenshot of the controller to be displayed in the UI library
        # If screenshot is set to True (default)
        if screenshot:

            # Run the saveScreenshot method
            info['screenshot'] = self.saveScreenshot(name, directory=directory)



        # Break this down:
        # With an open file (infoFile is the path name to this file)
        # We'll open it in 'write' mode ('w')
        # And we store this open file in a temporary variable called 'f'
        with open(infoFile, 'w') as f:

            # With this variable 'f', use json to dump the 'info' dictionary see line 63
            # into 'f', which is the file stream we have just opened
            # and we are going to indent everything by 4 spaces
            json.dump(info, f, indent=4)

        # Test the writing of the json file by running the following:
        # -------------------------------------------------------
        # from conLibrary import controllerLibrary
        # reload(controllerLibrary)
        # lib = controllerLibrary.ControllerLibrary()
        # lib.find()
        # lib.save('infoTest', chicken=True, rice='nice')
        # -------------------------------------------------------
        # A new .json file will be created called infoTest.json
        # And it will contain the chicken and rice values, indented by 4 spaces

        # To prevent us having to run lib.find() each time we save a new file to refresh our library
        # We can update the dictionary (self) with the info dictionary each time we save
        # As the info dictionary contains all the information we need
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

            # Find the json file, which will be called the same as our .ma maya file
            # Se we can use string substitution to construct the .json filename
            infoFile =  '%s.json' % name

            # Check if the infoFile (json) is in the files we listed (line 166)
            if infoFile in files:

                # If it is, then we can construct the full path
                # We already know the directory from earlier
                # And we have just defined the infoFile based on the file name (line 200)
                infoFile = os.path.join(directory, infoFile)

                # We can now read the file
                # 'r' refers to 'read' mode, as apposed to 'w' write mode
                with open(infoFile, 'r') as f:

                    # Store the json data in a new variable
                    info = json.load(f)
                    pprint.pprint(info)

            # Otherwise if there is no infofile already
            else:
                print 'No info found'

                # Define that info is an empty dictionary
                # We do this so that 'info' is always a dictionary
                info = {}

            # Check if a screenshot exists
            screenshot = '%s.jpg' % name
            if screenshot in files:
                info['screenshot'] = os.path.join(directory, name)

            info['name'] = name
            info['path'] = path

            print 'Path:', path

            # Remember that this is a dictionary, and we defined this class as
            # one on line 53 (class ControllerLibrary(dict)
            # Assign the dictionary key 'name' to the path we have just constructed using the .join command

            self[name] = info

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

        # Get the path from the self dictionary
        path = self[name]['path']

        # import the file
        # i=True : Import = True
        # usingNamespaces = False : Our controller wont be imported into a secondary namespace
        cmds.file(path, i=True, usingNamespaces=False)

        # We can now import our test controller using:
        # --------------------------------------------
        # from conLibrary import controllerLibrary
        # reload(controllerLibrary)
        # lib = controllerLibrary.ControllerLibrary()
        # lib.find()
        # lib.load('test')
        # --------------------------------------------

    def saveScreenshot(self, name, directory=DIRECTORY):

        # Create the path, which is our directory + the file name
        path = os.path.join(directory, '%s.jpg' % name)

        # Make sure the maya view fits exactly around our controller
        cmds.viewFit()

        # Tell maya how to save out the image (.jpeg, png?, width, height etc)
        # Set the file type to JPEG (8 is the value in the maya render settings interface, makes little sense)
        cmds.setAttr('defaultRenderGlobals.imageFormat', 8)

        # Render this out using the playblast command
        # The complete filename is our path (where this is saved to)
        # forceOverwrite=True : Write over an existing one, so we dont get a dialog
        # showOrnaments : ornaments are parts of the viewport which arent in our scene
        # startTime = 1, endTime = 1 : We only want 1 image
        # viewer : We dont want this to open up in an image viewer once saved
        cmds.playblast(completeFilename=path, forceOverwrite=True, format='image', width=200, height=200,
                       showOrnaments=False, startTime=1, endTime=1, viewer=False)

        return path
