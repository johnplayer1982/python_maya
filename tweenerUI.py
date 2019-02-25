# Import the Maya commands library
from maya import cmds

# ------------------------------------------------
# Firstly create an object (cube, whatever..)
# ------------------------------------------------
# import tweenerUI as tui
# reload(tui)
# tui.tween(50)
# ------------------------------------------------

# Lets define our tween function
# We need to know the percentage to tween and also the object
# We'll set the object to None so that it isn't undefined
# Define the attributes, and set that to None
# And finally selection=True

def tween(percentage, obj=None, attrs=None, selection=True):

    # Raise an error if obj is not given and selection is False
    if not obj and not selection:
        raise ValueError('No object selected to tween')

    # To see the above value error run:
    # ---------------------------------
    # tween(12, selection=False)
    # ---------------------------------

    # If no object is specified, get it from the first selection
    if not obj:

        # Get the first object in the selection
        obj = cmds.ls(selection=True)[0]

    if not attrs:

        # Query the object that we got from the selection
        # List all of the attributes on it that are keyable (we can animate)
        attrs = cmds.listAttr(obj, keyable=True)

        # This will give is all the attributes that can be animated on
        print 'Nice! we can animate on:', obj, 'with the following attributes: ', attrs

    # Get the current time (Maya timeline)
    # query=True means that we just want to get the time, not change it
    currentTime = cmds.currentTime(query=True)

    # Confirm we are getting the current time
    print currentTime
