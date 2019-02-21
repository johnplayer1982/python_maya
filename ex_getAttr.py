# Import the Maya command library

from maya import cmds

# Create a function for this, give it a None shape

def createObject(shape='None'):

    # Whack in an if statement just for the craic
    if shape == 'Cube':

        # Create a cube object
        ourCube = cmds.polyCube()

        # And get the shape
        ourCubeShape = ourCube[0]

        # And move it about a bit!
        cmds.setAttr(ourCubeShape+'.translateX', 2)
        cmds.setAttr(ourCubeShape+'.rotateY', 45)
        cmds.setAttr(ourCubeShape+'.scaleZ', 3)

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
# Run from Maya:
# -----------------------------------------------------------------
# import ex_getAttr as ga
# reload(ga)
# ga.createObject(shape='Cube')
# -----------------------------------------------------------------
