import pprint

class prettyPrint(object):

    stuff = ['chicken', 'eggs', 'orange', 'spoon', 'toast']

    print 'Normal:', stuff

    stuff.insert(0, stuff[:])
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)
