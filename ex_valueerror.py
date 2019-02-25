# Example of a value error
# --------------------------------
# import ex_valueerror as exval
# reload(exval)
# exval.example(selection=False)
# --------------------------------

# Define a simple function:
def example(obj=None, selection=True):

    # If object is none and selection is false:
    if not obj and not selection:

        # Output a value error:
        raise ValueError('There is no object or selection')

