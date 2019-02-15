# Check if a string ends with a thing

# Import Maya commands library
from maya import cmds

# Create a cube object
cube = cmds.polyCube()
print cube
# output = [u'pCube1', u'polyCube1']

# Get the object name
cubeshape = cube[0]
print cubeshape
# output = pCube1

# Define the suffix
suffix = "_new"

# Add the suffix to the object
cmds.rename(cubeshape, cubeshape + suffix)
# Update the variable name
cubeshape = cubeshape + suffix

# Check if the new suffix has been applied
if cubeshape.endswith('new'):
    print 'Yep!'
