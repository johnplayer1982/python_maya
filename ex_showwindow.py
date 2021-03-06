# Example for creating a simple UI window in Maya
# ---------------------------
# import ex_showwindow as sw
# reload(sw)
# sw.showWindow().buildUI()
# ---------------------------

# Import the Maya commands library
from maya import cmds
import random

class showWindow(object):

    windowName = 'WindowName'

    def __init__(self):

        print 'Initialized'

    def buildUI(self):

        # Create a window using the cmds.window command
        # give it a title, icon and dimensions

        window = cmds.window( title="Long Name", iconName='Short Name', widthHeight=(300, 300) )

        # As we add contents to the window, align them vertically
        cmds.columnLayout(adjustableColumn=True)

        # Add some intro text
        cmds.text(label="Some intro text here")

        # For column Layout use:
        # cmds.columnLayout()
        # And define the column numbers using:
        # cmds.rowLayout(numberOfColumns=4)

        # Add a number slider (integer)
        # Set min and max values
        # value = default value
        # step = increment
        # dragCommand = function to run on each step

        self.slider = cmds.intSlider(min=2, max=30, value=5, step=1, dragCommand=self.updateLabel)

        # Label for the slider
        # We want to update this when the slider is moved

        self.label = cmds.text(label="5")

        # A button that does nothing

        cmds.button(label='Do Nothing')

        # A button that triggers a function

        cmds.button(label='Create cubes', command=self.createCubes)

        # Close button with a command to delete the UI

        cmds.button(label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)'))

        # Set its parent to the Maya window (denoted by '..')

        cmds.setParent( '..' )

        # Show the window that we created (window)

        cmds.showWindow( window )

    # The value is passed from the dragCommand attribute on line 43:

    def updateLabel(self, value):

        # Update the label on the slider

        cmds.text(self.label, edit=True, label=value)
        print value

    def createCubes(self, *args):

        # Give us something to increment
        count = 0

        # Query the slider to see how many cubes to make
        cubes = cmds.intSlider(self.slider, query=True, value=True)

        # Create some cubes!
        while count < cubes:

            # Create the cube
            cube = cmds.polyCube()
            cubeshape = cube[0]

            # Place the cube at random
            cmds.setAttr(cubeshape+".translateX", random.randrange(-10, 10))
            cmds.setAttr(cubeshape+".translateY", random.randrange(-10, 10))
            cmds.setAttr(cubeshape+".translateZ", random.randrange(-10, 10))

            # Increment the count
            count += 1



