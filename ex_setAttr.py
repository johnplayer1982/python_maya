# Set object attributes

# Import maya commands library
from maya import cmds

# Create a cube object
cube = cmds.polyCube()

# This will output a list [u'pCube1', u'polyCube1']
print cube

# Get the cube shape from the cube object
cubeshape = cube[0]

# This will output pCube1
print cubeshape

# Lock the translate attrubute
cmds.setAttr(cubeshape+".translate", lock=True)

# Select the cube shape
cmds.select(cubeshape)
