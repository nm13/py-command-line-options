import sys
import cmdopt

## print cmdopt.options

# print sys.argv
# print cmdopt.options.count()     


def get_option( dic, key, default = None ) :     
        """ check for "--key" and '-key[0]' """     

        ret = dic[key]
        if ret is None : ret = dic[ key[0] ]     

        if ret is None : ret = default     

        return ret     
        

cmdopt.options.__class__.get_option  =  get_option     
## options = cmdopt.options     
options = cmdopt.string_options     

print "raw values:", options

# if cmdopt.options['o'] is None and options['option'] is None:
if options.get_option('option') is None:

    print " neither '-o' nor '--option' keys were specified ! "     
    


#
# testing the convert() method:
#

conv_table = {    "i,int"    : int
             ,    "f,float"  : float
                  # custom stuff
             ,    "custom"   : lambda x: int(x[2:],16) if x.startswith('0x') else int(x)
             }


print "converted values:", options.convert( conv_table )  

