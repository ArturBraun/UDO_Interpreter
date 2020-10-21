"""@package Exceptions
Exception module for this project. Contain custom exception classes.
"""

#--------------------------------------------
# INCLUDED MODULES:
#--------------------------------------------
# Built-in:

# Written:

#--------------------------------------------
#CLASSES AND FUNCTIONS
#--------------------------------------------

class NestedParsingFileNotFoundError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None 

    def __str__(self):
        if self.message:
            return 'NestedParsingFileNotFoundError, {0}.'.format(self.message)
        else:
            return 'NestedParsingFileNotFoundError, cannot find the file for nested parsing!'

