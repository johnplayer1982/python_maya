# Apply a suffix to an object name
# Check if a string ends with a thing
# -----------------------------------
# import ex_endswith as exr
# reload(exr)
# exr.renameObj(suffix='_new')
# -----------------------------------

# Import Maya commands library
from maya import cmds

def renameObj(suffix=None):

    if suffix == None:
        raise ValueError('No suffix specified')

    # Create a cube object
    cube = cmds.polyCube()
    print cube
    # output = [u'pCube1', u'polyCube1']

    # Get the object name
    cubeshape = cube[0]
    print cubeshape
    # output = pCube1

    # Add the suffix to the object
    cmds.rename(cubeshape, cubeshape + suffix)
    # Update the variable name
    cubeshape = cubeshape + suffix

    # Check if the new suffix has been applied
    if cubeshape.endswith(suffix):
        print 'Yep!'
