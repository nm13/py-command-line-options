import sys
import cmdopt

print cmdopt.options

# print sys.argv
# print cmdopt.options.count()     


"""

# get the first positional ("non-option") argument, if any :     
posarg = cmdopt.options.count() + 1
if posarg < len( sys.argv ):     
    print sys.argv[ posarg ]     

"""

if cmdopt.options['O'] is None and cmdopt.options['option'] is None:

    print " neither '-o' nor '--option' keys were specified ! "     
    
