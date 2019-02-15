# Select an object

# Import maya commands library
from maya import cmds

# Create a few objects
cube = cmds.polyCube()
circle = cmds.circle()
cylinder = cmds.polyCylinder()

# Select the circle object
cmds.select(circle)
