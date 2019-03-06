# -----------------------
# import ex_nodes as ex
# reload(ex)
# newInst = ex.getNodes()
# -----------------------

# Import the Maya commands library
from maya import cmds

# Function to get the nodes
# Nodes = None by defaullt
def getNodes(nodes=None):

    # Create a couple of objects
    cube = cmds.polyCube()
    sphere = cmds.polySphere()

    # Get the names of both objects
    cubeShape = cube[0]
    sphereShape = sphere[0]

    # Select both shapes
    cmds.select(cubeShape, sphereShape)

    # Add the selected objects to the nodes variable
    nodes = cmds.ls(selection=True)

    # Print the nodes type and list:

    # <type 'list'>
    print type(nodes)

    # [u'pCube1', u'pSphere1']
    print nodes

# ------------------------------
# import ex_nodes as ex
# reload(ex)
# newInst = ex.noNodesSelected()
# ------------------------------

def noNodesSelected(nodes=None):

    if not nodes:
        cmds.error('No objects selected')


