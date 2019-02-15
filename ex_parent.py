# Create parent / child relationships

# Import maya commands library
from maya import cmds

# Create a cube object
cube = cmds.polyCube()
cubeshape = cube[0]

# Create a circle object
circle = cmds.circle()
circleshape = circle[0]

# Make the cubeshape a child of the circleshape
cmds.parent(cubeshape, circleshape)

# Check the outliner to see the new hierarchy
