import sys
import cmdopt

print "'bare' options:"
print cmdopt.string_options

    


#
# testing the convert() method:
#

def myeval( expr ):
    
    ret =  expr
    try:
        ret = eval( expr, {} )
    except:
        pass
        
    return ret


conv_table = {    "i,int"    : int
             ,    "f,float"  : float
                  # custom stuff
             ,    "custom"   : lambda x: int(x[2:],16) if x.startswith('0x') else int(x) # translate both integers base 10 and base 16 
             # "default" :
             ,    '*'        : myeval 
             }


options = cmdopt.string_options

print "converted options:"
print options.convert( conv_table )  
