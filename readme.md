# Python Maya

## Purpose

This repo stores all of my python scripts for use in Maya.  For help setting up your environment:

- [Setting up your build environment](http://help.autodesk.com/view/MAYAUL/2018/ENU/?guid=__files_Setting_up_your_build_environment_htm)

## Example scripts

Example scripts are prefixed with "ex_" and show small examples of methods and functions.

## Complete Scripts

*objectRenamer.py*

Adds a suffix to objects based on type and returns a list of all of the renamed objects.
Camera's are bypassed.

Will rename a selected object, or all objects if no object is selected.  It will also check for the suffix before
applying to prevent duplicates (eg. polyCube1_geo_geo_geo).

```
import objectRenamer as obr
obr.rename()
```

*gearCreator.py*

Allows you to easily create a gear shape.

Default values are specified in the script (teeth=10, length=0.3)

```
import gearCreator as gc
gc.createGear()
```

Or specify override values in the function call

```
import gearCreator as gc
gc.createGear(teeth=20, length=0.3)
```

You can then modify the gear within Maya using the command:

```
import gearCreator as gc
reload(gc)
gc.createGear(teeth=20, length=0.3)
gc.changeTeeth(constructor, extrude, teeth=10, length=0.2)
```

as we return transform, constructor, extrude from the createGear() function.
