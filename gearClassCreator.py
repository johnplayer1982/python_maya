# wip
# Import the maya commands library
from maya import cmds

# Create class and inherit from the Python object
class Gear(object):

    """
    This function will create a gear object with the given parameters,
    To run this from within Maya:

        import gearClassCreator as gearCreator
        reload(gearCreator)
        gear = gearCreator.Gear()
        gear.createGear()

    Then modify the object using the changeTeeth function:

        gear.changeTeeth(teeth=12, length=0.4)

    :param teeth: The number of teeth to create
    :param length: The length of the teeth
    :return: A tuple of the transform, constructor and extrude node
    """

    # The __init__ method allows us to create default values
    # When we first 'initialise' a new gear
    # We can confirm these values in the Maya script editor when we create a new gear object:
    # ------------------------------------------
    #   import gearClassCreator as gearCreator
    #   reload(gearCreator)
    #   gear = gearCreator.Gear()
    #   print gear.extrude
    #
    #   Output = None
    # ------------------------------------------

    def __init__(self):

        print 'Running the init method'
        self.transform = None
        self.extrude = None
        self.constructor = None

    # Once we have created the gear:
    # ------------------------------------------
    #    gear.createGear()
    #    print gear.extrude
    #
    #    Output = polyExtrudeFace1
    # ------------------------------------------
    # We get back the extrude object, as we have defined self.extrude on line 119 in the createGear()
    # method that we have executed

    # Add a create gear method
    # PyCharm automatically adds the self keyword
    # Add the gear parameters
    def createGear(self, teeth=10, length=0.2):

        # The number of teeth is the subdivisions multiplied by 2
        # In other words if we want 10 teeth and we are extruding every other face then we need 20 faces in total
        spans = teeth * 2

        # Now lets create the pipe object
        # We want to hold on to the transform and the constructor of this object
        # We are storing these variables inside the class instance itself using 'self',
        # they will be accessible from outside this method

        self.transform, self.constructor = cmds.polyPipe(
            # We set the subdivisions axis to the number of spans we defined (teeth * 2)
            subdivisionsAxis=spans
        )

        # Lets find the faces we want to extrude
        # This variable exists only inside of this function, as it is not prefixed with self.
        sideFaces = range(

            # If we select every other face on the pipe and type ls -sl in the command line we get:
            # Result: pPipe1.f[40] pPipe1.f[42] pPipe1.f[44] pPipe1.f[46] pPipe1.f[48] pPipe1.f[50] pPipe1.f[52]...
            # pPipe1.f[54] pPipe1.f[56] pPipe1.f[58]
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

        # We have identified the faces, we now want to select them
        # first lets clear anything we may already have selected

        cmds.select(clear=True)

        # Now lets loop through the range in the sideFaces variable and select each

        for face in sideFaces:

            # We are going to use string substitution to build the string that maya
            # will use to identify the faces:
            cmds.select('%s.f[%s]' % (self.transform, face), add=True)
            print('Selected face: %s.f[%s]' % (self.transform, face))

            # add=True adds the selection, without this maya would deselect the previous selection
            # and select the new one

        # Nice, we have selected every other face
        # We now want to extrude them by the default length we specified in the function definition

        # Define self.extrude
        self.extrude = cmds.polyExtrudeFacet(
            # And we'll give it a localTranslate value of length along the Z axis
            localTranslateZ=length
        )

    def changeTeeth(self, teeth=10, length=0.2):

        """
        Change the number of teeth on a gear with a given number of teeth and a given length for the teeth.
        This will create a new extrude node.
        Args:
            constructor (str): the constructor node
            extrude (str): the extrude node
            teeth (int): the number of teeth to create
            length (float): the length of the teeth to create
        """

        # Lets change the number of faces on the polyPipe object

        # Again we define the spans (faces)
        spans = teeth * 2

        cmds.polyPipe(
            # Constructor is the polypipe that we have
            self.constructor,
            # We are editing an existing object, this tells maya not to create a new object
            edit=True,
            subdivisionsAxis=spans
        )

        # Lets tell Maya which faces to extrude:
        # To get the face values, in maya:
        # import the maya commands library:
        # from maya import cmds
        # print cmds.getAttr('polyExtrudeFace1.inputComponents')
        # This will give us the list of faces

        # Lets define the face range

        sideFaces = range(
            # Starting point
            spans*2,
            # End point
            spans*3,
            # Step up value
            2
        )

        # And create an empty variable to store our faces:

        faceNames = []

        # Cycle through each face, using string substitution to construct the correct identifier for each face

        for face in sideFaces:
            faceName = 'f[%s]' % (face)

            # Add the identifier string to the faceNames list
            faceNames.append(faceName)

        # Now to set the new attributes:
        # cmds.setAttr('extrudeNode.inputComponents', numberOfItems, item1, item2, item3, type='componentList')

        cmds.setAttr(
            # Set the extrude node
            # We have extrude[0] as extrude alone returns:
            # [u'polyExtrudeFace1'].inputComponents and we want 'polyExtrudeFace1.inputComponents'
            '%s.inputComponents' % self.extrude[0],
            # Get the length of the nodes (the number of)
            # This will be given to the setAttr function
            len(faceNames),
            # We now also need the list of faces that we will be using
            # This will expand the faceNames list so that each will be a parameter
            # This is the same as giving 'f[160], f[162], etc'
            *faceNames,
            # Finally lets describe what type of attribute we are changing
            type="componentList"
        )

        cmds.polyExtrudeFacet(
            self.extrude,
            edit=True,
            # ltz is short-form for localTranslateZ (see line 91)
            ltz=length
        )
