# Import maya commands library
from maya import cmds

# Print ALL objects, none of which we care about
print cmds.ls()

# Lets create an object
cube = cmds.polyCube()

# And select it
cmds.select(cube)

# Then list the selected object(s)
selection = cmds.ls(selection=True)
print selection
