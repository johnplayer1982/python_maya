# List the attributes of an obkect which can be animated on
# ---------------------------------------------------------
# Create an object and select it
# ---------------------------------------------------------
# import ex_listattr as ex
# reload(ex)
# ex.listattributes()
# ---------------------------------------------------------

from maya import cmds

def listattributes(obj=None, attrs=None, selection=True):

    if not obj:
        obj = cmds.ls(selection=True)[0]

    if not attrs:

        # Get the attributes that are available for our object
        # and only show the keyable attributes (Attributes we can animate on)
        attrs = cmds.listAttr(obj, keyable=True)

    # Lets get back the selected object and its animate-able attributes:
    print obj, attrs

    # Output:
    # The obj = pCube1
    # The attrs we can animate on = [u'visibility', u'translateX', u'translateY', u'translateZ', u'rotateX', u'rotateY', u'rotateZ', u'scaleX', u'scaleY', u'scaleZ']
