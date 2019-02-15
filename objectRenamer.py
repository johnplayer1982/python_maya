
# Load the maya commands library

from maya import cmds

# Create a library of suffixes
SUFFIXES = {
    'mesh': "geo",
    'joint': "jnt",
    'camera': None,
    'ambientLight': 'lgt'
}

# Create a default suffix as a fallback
DEFAULT_SUFFIX = "grp"

# Create the rename() function
def rename():

    # Create a new variable 'selection'
    # Store in it the currently selected objects

    selection = cmds.ls(selection=True)

    # If the selection contains 0 lists

    if len(selection) == 0:

        # Then get all objects in the outliner and assign to 'selection'
        # long=True : Gives us the full path to the object, so we can determine any parents.
        # dag=True : We will only get objects which are listed in the outliner, and none of the hidden objects inside of Maya.

        selection = cmds.ls(dag=True, long=True)

    # Sort the list now stored in 'selection'
    # Sort by length
    # In reverse, giving us the longest path first

    selection.sort(key=len, reverse=True)

    # For each object now in the 'selection' variable

    for obj in selection:

        # Split the path by "|" (pipe)
        # Store in a new variable 'shortName'

        shortName = obj.split("|")[-1]

        # Lets create a new variable to store the relatives
        # We want to list the relatives, we only want the children, and we want the full path
        # If there are no relative, return an empty list (or []), so that we always get a consistent object type output

        children = cmds.listRelatives(obj, children=True, fullPath=True) or []

        # If the length of the children is exactly 1 (remember this is in a for loop)

        if len(children) == 1:

            # Then put the object at position 0 in the chidren list into a new variable 'child'
            child = children[0]

            # Place the objecttype of the child variable in the variable 'objtype'
            objType = cmds.objectType(child)
        else:

            # Otherwise if the length of children is NOT 1 (so basically 0)
            # Put the object type of the object in the objtype variable
            objType = cmds.objectType(obj)

        # print the objtype variable
        print objType

        suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX)

        # If the suffix if false then do nothing
        # Because we set the camera to 'None' in the library this if will run as None is equal to false
        if not suffix:
            continue

        # If the object name already contains the _ suffix, continue and do not apply the new name
        if obj.endswith(suffix):
            continue

        # Lets now create a string which contains the new amended object name, based on our code:
        newName = shortName + "_" + suffix

        # Lets now rename the objects
        cmds.rename(obj, newName)
