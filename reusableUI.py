from maya import cmds
from tweenerUI import tween
from gearClassCreator import Gear

# -------------------------
# import reusableUI as rui
# reload(rui)
# rui.BaseWindow().show()
# -------------------------

class BaseWindow(object):

    windowName = "BaseWindow"

    def show(self):
        if cmds.window(self.windowName, query=True, exists=True):
            cmds.deleteUI(self.windowName)

        cmds.window(self.windowName)
        self.buildUI()
        cmds.showWindow()

    def buildUI(self):

        pass

    def reset(self, *args):

        pass

    def close(self, *args):
        cmds.deleteUI(self.windowName)

# -------------------------
# import reusableUI as rui
# reload(rui)
# rui.TweenerUI().show()
# -------------------------

class TweenerUI(BaseWindow):

    windowName = "TweenerWindow"

    def buildUI(self):
        # To start with we create a layout to hold our UI objects
        # A layout is a UI object that lays out its children, in this case in a column
        column = cmds.columnLayout()

        # Now we create a text label to tell a user how to use our UI
        cmds.text(label="Use this slider to set the tween amount")

        # We want to put our slider and a button side by side. This is not possible in a columnLayout, so we use a row
        row = cmds.rowLayout(numberOfColumns=2)

        # We create a slider, set its minimum, maximum and default value.
        # The changeCommand needs to be given a function to call, so we give it our tween function
        # We need to hold on to our slider's name so we can edit it later, so we hold it in a variable
        self.slider = cmds.floatSlider(min=0, max=100, value=50, step=1, changeCommand=tween)

        # Now we make a button to reset our UI, and it calls our reset method
        cmds.button(label="Reset", command=self.reset)

        # Finally we don't want to add anymore to our row layout but want to add it to our column again
        # So we must change the active parent layout
        cmds.setParent(column)

        # We add a button to close our UI
        cmds.button(label="Close", command=self.close)

    # *args will be a new concept for you
    # It basically means I do not know how many arguments I will get, so please put them all inside this one list (tuple) called args
    def reset(self, *args):
        # This resets the slider to its default value
        cmds.floatSlider(self.slider, edit=True, value=50)

# -------------------------
# import reusableUI as rui
# reload(rui)
# rui.GearUI().show()
# -------------------------

class GearUI(BaseWindow):

    windowName = 'GearWindow'

    def __init__(self):

        self.gear = None

    def buildUI(self):

        column = cmds.columnLayout()

        cmds.text(label="use te slider to modify the gear")

        cmds.rowLayout(numberOfColumns=4)

        # Define as self. variable as we want to access it later
        self.label = cmds.text(label="10")

        # intSlider = Integer sliders
        # default value=10
        # step is the increment value = 1 (Goes up by 1 each time)
        # dragCommand=self.modifyGear = will execute the modifyGear function on drag
        self.slider = cmds.intSlider(min=4, max=30, value=10, step=1, dragCommand=self.modifyGear)

        # Create some buttons
        cmds.button(label="Make Gear", command=self.makeGear)
        cmds.button(label="Reset", command=self.reset)
        cmds.setParent(column)

        # Self.close is already defined in the baseWindow above
        cmds.button(label="Close", command=self.close)


    # Throw away any values the command= gives us in the *args variable
    def makeGear(self, *args):

        print 'Making gear'

        # We are going to query the value to use for our key (query=True, value=True)
        teeth = cmds.intSlider(self.slider, query=True, value=True)

        # Gear() is imported on line 3
        self.gear = Gear()

        # Call the createGear function
        # Use the teeth number specified in the slider (line 122)
        self.gear.createGear(teeth=teeth)

    # The drag command will send us the value of the slider
    # We'll store this value in a variable called teeth,  defined in the function call below
    def modifyGear(self, teeth):

        print teeth

        if self.gear:
            self.gear.changeTeeth(teeth=teeth)

        # For self.label see line 98 above
        cmds.text(self.label, edit=True, label=teeth)

    def reset(self, *args):

        print 'Resetting'

        # We dont want to hold on to the gear anymore
        self.gear = None

        # Reset the slider
        cmds.intSlider(self.slider, edit=True, value=10)

        # Reset the slider label to 10
        cmds.text(self.label, edit=True, label=10)
