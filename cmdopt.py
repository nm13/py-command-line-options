#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-  

import sys     

# class _Structure: pass # convenient syntax to pass arguments     
class _KeyData :     
        
        def __init__( self ) :     
                
                self.key = None     
                self.value = None     



def _get_key( arg ) :     
        """ retun None or Structure """     
        
        if arg is None : return None     
        # else ...             
        
        ret = None     
        if arg.startswith( '--' ) :     
                
                short = arg[2:]     
                
                ret = _KeyData()     

                valstart = short.find('=')     
                if valstart >= 0 :     
                
                        ret.key = short[:valstart]
                        ret.value = short[(valstart+1):]
                
                else : # no '=' in the argument string     
                        
                        ret.key = short
                        # ret.value = None     
                        
        elif arg.startswith( '-' ) :     
                
                # we have checked for '--' above -- so it is a single '-' 
                
                short = arg[1:]     
                
                ret = _KeyData()     
                
                ret.key = short[0]
                
                if len( short ) > 1 :     
                        
                        ret.value = short[1:]     
                
        # check for '--' :     
        if ret is not None and ret.key == '' :     
                
                ret.key = None     
                
        
        return ret     


# 
# want to do things like "if opts['k'] is None and opts[keys] is not None : ... "     
# 
class _Dict(dict):     

    def __getitem__(self, key) :     
    
	return self.get(key)     

# let us teach our Dict() how to store the number of option parameters :     	
class _CounterMixin(object):

    def _set_count(self, count):
        self._count = count     
        
    def count(self): return self._count     

    
class _OptionsDict(dict, _CounterMixin) : pass     

def _get_keys( argv ) :     
        
        # ret = {}     
        # ret = _Dict()          
        ret = _OptionsDict()          
        
        i, N = 0, len( argv )     
        
        lastopt_index = 0
        
        while i < N :     
                
                arg = argv[i]     
                
                keydata = _get_key( arg )     
                
                if keydata is None : 
                        
                        i += 1     

                        continue     
                
                # special case : '--'     
                if keydata.key is None :     
                    
                        lastopt_index = i     
                        break     
                        
                
                # else :     
                if keydata.value is not None :     
                        
                        ret[ keydata.key ] = keydata.value     

                        lastopt_index = i     
                        
                        i += 1     
                        continue     
                        
                else :     
                        
                        k = i+1     
                        if k < N:     
                                
                                arg2 = argv[k]     
                                
                                if not arg2.startswith('-') :     
                                        
                                        ret[ keydata.key ] = arg2     
                                        
                                        lastopt_index = k     
                                        
                                        i = k+1     
                                        continue     
                                        
                        # else     
                        ret[ keydata.key ] = True     

                        lastopt_index = i     

                        i = k     
                        continue  # for uniformness     
                        
        ret._set_count( lastopt_index + 1 )
                
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


