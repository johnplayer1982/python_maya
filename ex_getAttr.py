# Import the Maya command library

from maya import cmds

# Create a function for this, give it a None shape

def createObject(shape=None, tx=1, ry=1, sz=1):

    # Whack in an if statement just for the craic
    if shape == 'Cube':

        # Create a cube object
        ourCube = cmds.polyCube()

        # And get the shape
        ourCubeShape = ourCube[0]

        # And move it about a bit!
        cmds.setAttr(ourCubeShape+'.translateX', tx)
        cmds.setAttr(ourCubeShape+'.rotateY', ry)
        cmds.setAttr(ourCubeShape+'.scaleZ', sz)

        # Lets get the translateX attribute
        ourCubeTX = cmds.getAttr(ourCubeShape+'.translateX')
        print 'Translate X Attribute:', ourCubeTX

        # Lets get the rotateX attribute
        ourCubeRY = cmds.getAttr(ourCubeShape + '.rotateY')
        print 'Rotate Y Attribute:', ourCubeRY

        # Lets get the scaleZ attribute
        ourCubeSZ = cmds.getAttr(ourCubeShape + '.scaleZ')
        print 'Scale Z Attribute:', ourCubeSZ

# -----------------------------------------------------------------
# Run from Maya (Default values):
# -----------------------------------------------------------------
#
# import ex_getAttr as ga
# reload(ga)
# ga.createObject()
#
# -----------------------------------------------------------------
# Run from Maya (Specify translate, rotate and scale):
# -----------------------------------------------------------------
#
# import ex_getAttr as ga
# reload(ga)
# ga.createObject(shape='Cube', tx=2, ry=33, sz=4)
#
# -----------------------------------------------------------------
