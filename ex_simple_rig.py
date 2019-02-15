# Create a simple rig

# Import maya commands library
from maya import cmds

# Create a cube object
cube = cmds.polyCube()
cubeshape = cube[0]

# Create a circle object
circle = cmds.circle()
circleshape = circle[0]

# Make the cube a child of the circle
cmds.parent(cubeshape, circleshape)

# Lock the cubes attributes so it cant be moved independently of its parent
targetshape = cubeshape
attr = [".translate", ".rotate", ".scale"]

for obj in attr:
    cmds.setAttr(targetshape+obj, lock=True)

# Rotate the parent just so we can see that the child will also rotate
cmds.setAttr(circleshape + '.rx', 45)
