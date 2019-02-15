
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
def rename(selection=False):

    # Help text
    """
    This function will rename any objects to have the correct suffix
    :param selection: Whether or not we use the current selection
    :return: A list of all the objects we operated on
    """
    # Trigger in Maya by typing:
    # import objectRenamer as rn
    # reload(rn)
    # print help(rn.rename)

    # Create a new variable 'selection'
    # Store in it the currently selected objects

    object = cmds.ls(selection=selection, dag=True, long=True)

    # if the objects in empty and there is no selection
    if selection and not object:
        # Raise a runtime error
        raise RuntimeError("You don't have anything selected")

    # Sort the list now stored in 'selection'
    # Sort by length
    # In reverse, giving us the longest path first

    object.sort(key=len, reverse=True)

    # For each object now in the 'selection' variable

    for obj in object:

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
        if obj.endswith("_"+suffix):
            continue

        # Lets now create a string which contains the new amended object name, based on our code:
        new_name = "%s_%s" % (shortName, suffix)

        # Lets now rename the objects
        cmds.rename(obj, new_name)

        index = object.index(obj)
        object[index] = obj.replace(shortName, new_name)

    return object

