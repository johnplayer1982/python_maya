from maya import cmds
import random

# Give us something to increment
count = 0

# Query the slider to see how many cubes to make
cubes = 10

# Create some cubes!
while count < cubes:

    # Create the cube
    cube = cmds.polyCube()
    cubeshape = cube[0]

    # Place the cube at random
    cmds.setAttr(cubeshape+".translateX", random.randrange(-10, 10))
    cmds.setAttr(cubeshape+".translateY", random.randrange(-10, 10))
    cmds.setAttr(cubeshape+".translateZ", random.randrange(-10, 10))

    # Increment the count
    count += 1
