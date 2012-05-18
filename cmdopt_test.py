import sys
import cmdopt

print "options as strings:", cmdopt.string_options

print "options as Python values:", cmdopt.options

print "positional arguments:", cmdopt.options.args

# print sys.argv
# print cmdopt.options.count()     


"""

# get the first positional ("non-option") argument, if any :     
posarg = cmdopt.options.count() + 1
if posarg < len( sys.argv ):     
    print sys.argv[ posarg ]     

"""

if cmdopt.options['O'] is None and cmdopt.options['option'] is None:

    print
    print " neither '-O' nor '--option' keys were specified ! "     
    

