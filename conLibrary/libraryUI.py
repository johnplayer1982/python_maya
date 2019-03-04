# The UI for our controller library

# from the controllerLibrary module import the ControllerLibrary Class
import pprint
from maya import cmds

import controllerLibrary
reload(controllerLibrary)

# Import the QT modules we need
# Widgets, core and GUI
from PySide2 import QtWidgets, QtCore, QtGui

# Create a class for our library UI
# We inhert from ... because we cant our controller library UI to be a dialogue
class ControllerLibraryUI(QtWidgets.QDialog):

    """
    The ControllerLibraryUI is a dialog that lets us save and import controllers
    """

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
        # The library variable points to an instance of our controller library
        self.library = controllerLibrary.ControllerLibrary()

        # Build and populate the controller library UI each time a new instance of this class (ControllerLibraryUI) is
        # created:

        # Call the build UI method
        # Build the UI
        self.buildUI()

        # Call the populate method
        # Populate the UI
        self.populate()

    def buildUI(self):

        """
        This method builds the UI
        """

        print 'Building UI'

        # Create a vertical layout
        # This is the master layout
        # QVBoxLayout = Vertical Box Layout
        # We tell the layout to 'apply' to self (Our ControllerLibraryUI class)
        layout = QtWidgets.QVBoxLayout(self)

        # A child of the master layout
        # Add a horizontal line for our text field (To allow users to search controllers)
        saveWidget = QtWidgets.QWidget()
        # Will layout out any of its children horizontally from left to right
        # Apply this to the 'saveWidget'
        saveLayout = QtWidgets.QHBoxLayout(saveWidget)
        # Add the widget to the layout
        layout.addWidget(saveWidget)

        # Create the items that will be inside this layout (saveLayout)
        # Prefixing with 'self' means that we can access this varible from outside of this method
        # But inside the class
        self.saveNameField = QtWidgets.QLineEdit()
        # And Add it to the layout
        saveLayout.addWidget(self.saveNameField)

        # Create the save button
        saveBtn = QtWidgets.QPushButton('Save')
        # Connect the button to a save method
        saveBtn.clicked.connect(self.save)
        # And Add it to the layout
        saveLayout.addWidget(saveBtn)

        # Define the size of the icons in the library UI as an int
        size = 64
        # Define buffer (margin between icons in lib list)
        buffer = 10

        # Create the thumbnail view
        # A list of widgets
        self.listWidget = QtWidgets.QListWidget()
        # Set the view mode it 'IconMode', displaying the controllers as icons + text, not a list
        self.listWidget.setViewMode(QtWidgets.QListWidget.IconMode)
        # Set the size of the icons (See size variable above)
        self.listWidget.setIconSize(QtCore.QSize(size, size))
        # Set our list so that the icons move adjust to fit the window
        self.listWidget.setResizeMode(QtWidgets.QListWidget.Adjust)
        # Add the spacing between icons
        self.listWidget.setGridSize(QtCore.QSize(size+buffer, size+buffer))
        # And Add it to the layout
        layout.addWidget(self.listWidget)

        # Add buttons to the bottom of the UI
        # We'll create a new widget within the UI to hold these
        btnWidget = QtWidgets.QWidget()
        # Add the button layout, and assign it to the button widget (above)
        btnLayout = QtWidgets.QHBoxLayout(btnWidget)

        # Add to the master layout
        layout.addWidget(btnWidget)

        # Create an import button
        importBtn = QtWidgets.QPushButton('Import')
        # Connect the button to the self.load method
        importBtn.clicked.connect(self.load)
        # Add it to our btnLayout
        btnLayout.addWidget(importBtn)

        # Add a refresh button
        refreshBtn = QtWidgets.QPushButton('Refresh')
        # On click connect to the populate method (see def populate(self):)
        # We didnt include the brackets on the method ('populate()')
        # Because we dont want to trigger the method, just establish a connection between the refresh button and the method
        refreshBtn.clicked.connect(self.populate)
        # Add it to our btnLayout
        btnLayout.addWidget(refreshBtn)

        # Add a close button
        closeBtn = QtWidgets.QPushButton('Close')
        # When the close button is clicked
        # Connect the event to the method self.close
        closeBtn.clicked.connect(self.close)
        # Add the close button to the button layout
        btnLayout.addWidget(closeBtn)

    def populate(self):

        """
        This method clears and then populates the UI with the controller library
        """

        print 'Populating UI'

        # Clear out the list first
        # So that when we trigger this method by clicking the 'Refresh' button, our controllers arent duplicated
        self.listWidget.clear()

        # Find our existing controllers
        self.library.find()

        # Loop through each controller that we find and add it to the UI
        for name, info in self.library.items():

            # self.library.items returns 2 items for every for loop
            # The name and the info:
            print name, info

            # Create a new list widget to add our item to
            # Give it 'name', as this is the string that we want displayed in the list
            item = QtWidgets.QListWidgetItem(name)

            # Add the item to the list widget:
            self.listWidget.addItem(item)

            # Add the screenshot
            screenshot = info.get('screenshot')

            # Check if a screenshot exists
            if screenshot:

                # Create an icon variable
                # The icon class is in the QtQui module
                # screenshot is the path to the screenshot that we stored in the variable
                icon = QtGui.QIcon(screenshot)

                # Tell the list item to use this icon
                item.setIcon(icon)

            # Create a tooltip
            # Sets the tooltip for each item in this loop
            # Uses the 'info' as the tooltip content
            item.setToolTip(pprint.pformat(info))

    def load(self):

        """
        This loads the currently selected controller
        """

        # Get the current item in our list widget
        # This is what we are loading into our scene?
        currentItem = self.listWidget.currentItem()

        # If there is not an item in our selection
        if not currentItem:

            # Do nothing
            return

        # Store the name of the current selected item
        name = currentItem.text()

        # Load the object into the scene, from the library based on its name
        self.library.load(name)

    def save(self):

        """
        This saves the controller with the given filename
        """

        # Save the name in the text field to a variable
        name = self.saveNameField.text()
        print 'Saving', name

        # Add some validation, we want to make sure we're entered a name
        # If after stripping out whitespaces the name does not exist
        if not name.strip():

            # Issue a warning
            cmds.warning("No name entered")
            return

        # Save the name to the library
        self.library.save(name)

        # Refresh/re-populate the library UI
        self.populate()

        # Reset the text field (to empty)
        self.saveNameField.setText('')

# Function to show the UI
# This is a convenience function to display our UI
def showUI():

    """
    Shows and returns a handle to the UI
    :return: QDialog
    """

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


