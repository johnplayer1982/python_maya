# Get the bounding box of objects
# -------------------------------
# import ex_bounding_box as ex
# reload(ex)
# newInst = ex.boundingBox()
# -------------------------------

from maya import cmds
import pprint

def boundingBox():

     # Create a couple of objects
    cube = cmds.polyCube()
    sphere = cmds.polySphere()

    # Get the shapes of both objects
    cubeShape = cube[0]
    sphereShape = sphere[0]

    # Select both shapes
    cmds.select(cubeShape, sphereShape)

    # Add the selected objects to the nodes variable
    nodes = cmds.ls(selection=True)

    # Create an empty list to store the bounding boxes
    bboxes = {}

    # For loop to loop through the nodes (objects)
    for node in nodes:

        # Store the bounding box in a bbox variable
        # Give it the node the query
        bbox = cmds.exactWorldBoundingBox(node)

        # Add the bounding box for this node to the bboxes list
        bboxes[node] = bbox

        print node, bbox
        # We'll get back a list of 6 float (0.00) values for each object:
        # They are in order of XYZ XYZ
        # X min, Y min, Z min, X max, Y max, Z max
        # These values define the bounds of the bounding box
        # [-0.5, -0.5, -0.5, 0.5, 0.5, 0.5]
        # [-1.000000238418579, -1.0, -1.0000004768371582, 1.0, 1.0, 1.0000001192092896]

    print pprint.pprint(bboxes)
