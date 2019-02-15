from maya import cmds

name = "John"
newname = "James"

cmds.rename(name, newname)
print name
