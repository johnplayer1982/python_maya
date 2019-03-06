# ------------------------------
# import duplicate as dp
# reload(dp)
# new = dp.duplicateTool()
# ------------------------------

from maya import cmds
import random

class duplicateTool(object):

    def __init__(self):

        print 'Tool initialized'

    def dupAndTransform(self,
                        objects=10,
                        transformaxis='y',
                        transformstep=1,
                        transformscale=0.1,
                        height=1,
                        randomscale=True):

        step = 0
        obj_list = []
        multiplier = 0
        startScale = 0

        while step < objects:
            cube = cmds.polyCube(height=height)
            obj_list.append(cube)
            step += 1

        for obj in obj_list:
            objshape = obj[0]
            cmds.setAttr(objshape+'.t%s' % transformaxis, transformstep + multiplier)

            if randomscale:
                cmds.scale(random.randint(1, 20), random.randint(1, 20),  random.randint(1, 20), objshape, pivot=(0, 0, 0), relative=True)
            else:
                cmds.scale(startScale, startScale, startScale, objshape, pivot=(0, 0, 0), relative=True)

            startScale += transformscale
            multiplier += transformstep

        print startScale