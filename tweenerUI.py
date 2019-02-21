# Import the Maya commands library
from maya import cmds

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

    # If selection is False (Nothing selected in Maya) and the obj is None we'll get an error
    # So lets catch this in our code:

    # If object is none, and selection is False
    if not obj and not selection:

        # Throw the error
        raise ValueError("No object given to tween")

    # If obj is False (None is 'Falsey')
    if not obj:

        # Object is assigned the first object in the selection
        obj = cmds.ls(Selection=True)[0]

    # If attrs is false
    if not attrs:

        # List the attributes that are available
        attrs = cmds.listAttr(
            # List attributes of the object
            obj,
            # Which are key-able
            keyable=True
        )

    # Confirm that we are getting the object and attributes:
    print obj, attrs
