# Import the maya commands library
from maya import cmds


# Create gear function
# teeth = Number of teeth the gear will have
# length = How long the teeth will be

def createGear(teeth=10, length=0.3):

    """
    This function will create a gear object with the given parameters
    :param teeth: The number of teeth to create
    :param length: The length of the teeth
    :return: A tuple of the transform, constructor and extrude node
    """
    # Get help in maya console with 'help(gearCreator.createGear)'

    print "Creating gear with", teeth, "teeth which are", length, "long"
    # Run this function in Maya with:
    # import gearCreator as gc
    # gc.gearCreator()
    # output = Creating gear 10 0.3

    # changing default value:
    # gc.gearCreator(teeth=20)
    # output = Creating gear 20 0.3

    # The number of teeth is the subdivisions multiplied by 2
    # In other words if we want 10 teeth and we are extruding every other face then we need 20 faces in total
    spans = teeth * 2
    print "Spans:", spans
    # Confirm that we get the number we are expecting

    # Now lets create the pipe object
    # We want to hold on to the transform and the constructor of this object
    transform, constructor = cmds.polyPipe(
        # We set the subdivisions axis to the number of spans we defined (teeth * 2)
        subdivisionsAxis=spans
    )

    # Lets find the faces we want to extrude
    sideFaces = range(

        # If we select every other face on the pipe and type ls -sl in the command line we get:
        # Result: pPipe1.f[40] pPipe1.f[42] pPipe1.f[44] pPipe1.f[46] pPipe1.f[48] pPipe1.f[50] pPipe1.f[52] pPipe1.f[54] pPipe1.f[56] pPipe1.f[58]
        # (pPipe1.f[40] = face 40) is our starting point for the range
        # teeth = 10, spans = teeth * 2 (20), here is it spans * 2 = 40
        spans * 2,

        # This is the END point for the range, we can see from the output of the ls -sl command
        # that the shape has 60 faces, so spans * 3 = 60
        # you cant see face 60 because we selected every other face
        spans * 3,

        # What we really want here is to select every second face
        # remember we are creating a gear here
        # the range method also accepts a "step" argument:
        2

    )

    # Now that we have added the step argument, printing the sideFaces
    # variable should give us every other face
    print "Side faces of object:", sideFaces
    # Side faces of object: [40, 42, 44, 46, 48, 50, 52, 54, 56, 58]

    # We have identified the faces, we now want to select them
    # first lets clear anything we may already have selected

    cmds.select(clear=True)

    # Now lets loop through the range in the sideFaces variable and select each

    for face in sideFaces:

        # We are going to use string substitution to build the string that maya
        # will use to identify the faces:
        cmds.select('%s.f[%s]' % (transform, face), add=True)
        print('Selected face: %s.f[%s]' % (transform, face))

        # add=True adds the selection, without this maya would deselect the previous selection
        # and select the new one

    # Nice, we have selected every other face
    # We now want to extrude them by the default length we specified in the function definition

    # Create a variable to hold the extrude command
    extrude = cmds.polyExtrudeFacet(
        # And we'll give it a localTranslate value of length along the Z axis
        localTranslateZ=length
    )

    # Lets print the new extrude object we have just created
    # extrude alone will give us back a list (of 1), for readability we'll only return the 1st item in the list
    print "Your new extrude object is:", extrude[0]

    # Finally lets return 3 important nodes that we can make use of later
    return transform, constructor, extrude

    # This returns a tuple with 3 nodes:
    # (u,'pPipe1', u'polyPipe1', u'polyExtrudeFace1')
