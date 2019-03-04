# The UI for our controller library

# from the controllerLibrary module import the ControllerLibrary Class
from controllerLibrary import ControllerLibrary

# Import the QT modules we need
# Widgets, core and GUI
from PySide2 import QtWidgets, QtCore, QtGui

# Create a class for our library UI
# We inhert from ... because we cant our controller library UI to be a dialogue
class ControllerLibraryUI(QtWidgets.QDialog):

    # Init function, called whenever you create a new instance of the class, eg:
    # newInst = ControllerLibrary()
    def __init__(self):

        # Lets find the 'super' class of the ControllerLibraryUI class
        # Which is the class its inheriting from (QtWidgets.QDialog)
        # Means we dont have to change all of our code occurences if we change QtWidgets.QDialog to something else
        super(ControllerLibraryUI, self).__init__()

        # Set a window title:
        self.setWindowTitle('Controller Library UI')

        # Store an instance of the library inside our UI
        self.library = ControllerLibrary()

        # Build and populate the controller library UI each time a new instance of this class (ControllerLibraryUI) is
        # created:

        # Call the build UI method
        self.buildUI()

        # Call the populate method
        self.populate()

    def buildUI(self):
        print 'Building UI'

    def populate(self):
        print 'Populating UI'

# Function to show the UI
# This is a convenience function to display our UI
def showUI():

    # Create an instance of our UI
    ui = ControllerLibraryUI()

    # Show the UI
    ui.show()

    # Return the ui instance so people using this function can hold on to it
    return ui

    # Test in maya:
    # --------------------------------
    # from conLibrary import libraryUI
    # reload(libraryUI)
    # ui = libraryUI.showUI()
    # --------------------------------


