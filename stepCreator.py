# Simple Maya steps script
# Create simple staircases
# John Player - www.john-player.com

# Import the maya commands library
from maya import cmds

# Create a new class

class stepCreator(object):

    # Create initialize class
    def __init__(self):

        # Print confirmation
        print 'Class initialized'

    # Define steps class
    def makesteps(self, steps=5, width=5):

        count   = 0
        start_y = 0
        start_z = 0

        while count < steps:

            thisCube = cmds.polyCube(w=width)
            thisCubeShape = thisCube[0]

            cmds.setAttr(thisCubeShape + '.ty', start_y)
            cmds.setAttr(thisCubeShape + '.tz', start_z)

            start_y += 1
            start_z += 1

            print thisCubeShape

            count += 1

        # [WIP - Adds bannister]
        if count == steps:

            print 'Stairs done, Adding bannister'

            leftbannister = cmds.polyCube()
            leftbannisterShape = leftbannister[0]

            cmds.setAttr(leftbannisterShape+'.tx', width/2)
