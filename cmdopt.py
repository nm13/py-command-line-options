#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-  

import sys     

# class _Structure: pass # convenient syntax to pass arguments     
class _KeyData :     
        
        def __init__( self ) :     
                
                self.key = None     
                self.value = None     



def _get_key( arg ) :     
        """ returns None or Structure ; special cases: for '--' key is None, for '-' it is ''  """     
        
        if arg is None : return None     
        # else ...             
        
        # ret = None  
        ret = _KeyData()   # most frequent case _in the code_ )
        
        # data = _KeyData()     
        
        
        #
        # the checks order makes them a bit ineffective -- but the code is easier to understand :  
        #
        
        
        # a special case
        if arg == '-' : 
            
            ret.key = ''
            # ret.value = None     
            
        # another one
        elif arg == '--' : 
            
            ret.key = None
            # ret.value = None     
            
        # "--option " and "--option=value"
        elif arg.startswith( '--' ) :     
                
                short = arg[2:]     
                
                # "--option=value"
                valstart = short.find('=')     
                if valstart >= 0 :     
                
                        ret.key = short[:valstart]
                        ret.value = short[(valstart+1):]
                
                # "--option"
                else : # no '=' in the argument string     
                        
                        ret.key = short
                        # ret.value = None     
                        
        # "-o ", "-oValue"
        elif arg.startswith( '-' ) :   # we have checked for '--' above -- so it is a single '-' 
                
                short = arg[1:]     
                
                ret.key = short[0]
                
                if len( short ) > 1 :     
                        
                        ret.value = short[1:]     
                    
        else :  # just an argument
            
            # may be we'd better put this as a first "if" check -- but at the moment I think this order reads better )  
            ret = None 
        
        return ret     


# 
# want to do things like "if opts['k'] is None and opts[keys] is not None : ... "     
# 
class _Dict(dict):     

    def __getitem__(self, key) :     
    
        return self.get(key)     


class _OptionsDict(_Dict) :  

    """ a _Dict( dict ) with some additional fields -- e.g. 'args' (a list of all "ordered / non-named" arguments) """

    ## pass # todo: add a "convert()" method
    # for "__init__", see _get_keys() below 
    
    def convert( self, table ) :  
        """ the "conversion table" is a dict of a form:
        
            {
                "k,key" : lambda arg : int(arg) # or just 'int'
                ...
            }
        
            i.e. the table 'key' is a string containing a comma-separated list of arguments (may be just one: "key" or "k" ) ,
            and the table 'value' is a conversion function that need to be applied .  
            
            on exception there is a warning message printed to stderr, and then the exception is re-raised .  
            
        """
        
        # the internal lookup table  
        # functions = {}
        functions = _Dict() # __getitem__ = get 
        
        # fill it  
        for key, value in table.iteritems() :  
            
            keys = key.split(',') 
            
            for k in keys :  
                
                functions[ k.strip() ] = value  
                
            
        # now apply it  
        for key, value in self.iteritems() :  
            
            func = functions[key] 
            if func : 
                try:
                    self[ key ] = func( value )  
                # except Exception as e :
                # want to be backward-compatible with 2.5 :
                except:
                    print >>sys.stderr, "failed to convert the value '%s' for the key '%s' "     %     ( value, key )  
                    
                    # too wordy  
                    """
                    print >>sys.stderr, "| failed to convert the value '%s' for the key '%s' "     %     ( value, key )  
                    
                    etype, evalue = sys.exc_info()[0:2]
                    exception_string = "%s: %s" % ( etype, evalue ) 
                    
                    print >>sys.stderr, "| exception:\n|\t", exception_string
                    
                    if isinstance(  func, type(lambda x:x)  ) :  
                        func_name = "%s function from %s:%d" % ( func.func_name, func.func_code.co_filename, func.func_code.co_firstlineno )
                    else :  
                        func_name = "function: %s" % (func, )
                    
                    print >>sys.stderr, "| caused by:\n|\t", func_name
                    """
                    
                    # better, but still in doubt if we need it )  
                    """
                    if isinstance(  func, type(lambda x:x)  ) :  
                        func_name = "function %s from %s:%d" % ( func.func_name, func.func_code.co_filename, func.func_code.co_firstlineno )
                    else :  
                        func_name = "function: %s" % (func, )
                    
                    print >>sys.stderr, "caused by", func_name
                    """
                    
                    # re-raise finally  
                    raise  
                    
                
            
        # for convenience :  
        return self     
    


def _get_keys( argv ) :  
    
    """ the actual constructor for the _OptionsDict class """
        
    # ret = {}     
    # ret = _Dict()          
    ret = _OptionsDict()          
    
    i, N = 0, len( argv )     
    
    ret.args = []
    # a synonym
    args = ret.args
    
    # for re-evaluation, if we'll need it :  
    ret._argv = argv
    
    while i < N :     
            
            arg = argv[i]     
            i += 1
            
            keydata = _get_key( arg )     
            
            # "if not an option: "
            if keydata is None : 
                
                    args.append( arg )
                    continue     
            
            # special case : '--'     
            elif keydata.key is None :     

                    # stop parsing options 
                    args.extend(  argv[ i : ]  )
                    break     
                    
            # special case : '-'     
            elif keydata.key == '' :     

                    ret[ '-' ] = True     
                    continue     
                    
            # simple option : "--option=value" or "-oValue"
            elif keydata.value is not None :     
                    
                    ret[ keydata.key ] = keydata.value     
                    continue     
                    
            # got a boolean option, "-o --other-option" , or a key/value pair, "-o Value" or "--option value"
            else :     
                    
                    nextarg = None
                    if i < N:     
                            
                            nextarg = argv[ i ]     
                            if nextarg.startswith( '-' ) :  
                                nextarg = None  
                            else: # skip this next argument on the next iteration  
                                i += 1     
                            
                    if nextarg is None :  
                        
                        ret[ keydata.key ] = True  
                        
                    else : 
                        
                        ret[ keydata.key ] = nextarg  
                                    
                    continue  # for uniformness     
                    
                
            
        
    
    return ret     


# -----------------------------------------------------------------------------

## # debug 
## print sys.argv     


options = _get_keys( sys.argv[1:] )     


if __name__ == "__main__" :

    print __doc__
    print "\n === \n"
    # print "module dir() listing: ", __dict__.keys()
    print "module dir() listing: ", dir()


