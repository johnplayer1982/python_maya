# Conditional statements

# if...

def conditional_if():

    text = "Hello if statement"

    if text.endswith('statement'):
        print text

# if and else

def conditional_elif():

    value = 14

    if value < 14:
        print "The value is less than 14"

    elif value > 14:
        print "The value is more than 14"

    else:
        print "The value is exactly 14"

# for

def conditional_for():

    mylist = [10, 12, 11, 3, 'string']

    for obj in mylist:
        print obj

# while

def conditional_while():

    myvalue = 1

    while myvalue < 7:
        myvalue = myvalue + 1
        print myvalue

# breaking a loop

def conditional_break():

    breakvalue = 0

    while breakvalue < 10:
        breakvalue = breakvalue + 1
        if breakvalue == 6:
            print "The value reached 6 so we stopped the loop"
            break
