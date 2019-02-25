# Get the current time on the animation slider within maya
# --------------------------------------------------------
# import ex_currenttime as extime
# reload(extime)
# extime.getTime()
# --------------------------------------------------------

# Import the maya commands library
from maya import cmds

def getTime():

    currentTime = cmds.currentTime(query=True)

    print currentTime
