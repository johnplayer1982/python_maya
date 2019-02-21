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

    # If selection is False (Nothing selected in Maya) and the obj is None we'll get an error
    # So lets catch this in our code:

    # If object is none, and selection is False
    if not obj and not selection:

        # Throw the error
        raise ValueError("No object given to tween")

    # If obj is False (None is 'Falsey')
    if not obj:

        # Object is assigned the first object in the selection
        obj = cmds.ls(selection=True)[0]

    # If attrs is false
    if not attrs:

        # Get the attributes that are available for our object
        # and only show the keyable attributes (Attributes we can animate on)
        attrs = cmds.listAttr(obj, keyable=True)

    # Confirm that we are getting the object and attributes:
    print obj, attrs

    # Output:
    # The obj = pCube1
    # The attrs we can animate on:
    # u'visibility',
    # u'translateX', u'translateY', u'translateZ',
    # u'rotateX', u'rotateY', u'rotateZ',
    # u'scaleX', u'scaleY', u'scaleZ']
