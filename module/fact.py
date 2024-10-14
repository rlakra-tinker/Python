#
# Author: Rohtash Lakra
#

# Modules are often designed with the capability to run as a standalone script for purposes of testing the
# functionality that is contained within the module. This is referred to as unit testing.
# For example, suppose you have created a module fact.py containing a factorial function, as follows:
def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


# When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module.
# However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'.
# Using this fact, you can discern which is the case at run-time and alter behavior accordingly:
if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))


# But it can also be run as a standalone by passing an integer argument on the command-line for testing:
# python fact.py 6
