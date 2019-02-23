# Simple Maya steps script
# Create simple staircases
# John Player - www.john-player.com

# Import the maya commands library
from maya import cmds

class stepCreator(object):

    """
    This class will create a set of steps with the given parameters,
    To run this from within Maya:

        import stepCreator as sc
        reload(sc)
        makesteps = sc.stepCreator()
        makesteps.makesteps()

    Example of arguments:

        makesteps.makesteps(steps=50, width=8)

    :param steps: The number of steps
    :param width: The width of the steps
    """

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

            print 'Step ' + thisCubeShape + ' Added'

            count += 1

# To enhance:
# - bannisters
# - angle: for spiralled, curved stairs
