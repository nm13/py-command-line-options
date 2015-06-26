An ultra-short and simple module to handle command line arguments in a small [throwaway](http://www.paulgraham.com/langdes.html) program.

Usage (_quick-and-dirty_ version):
```

import cmdopts # now you have ''cmdopts.options'' dictionary

# now run this as a script and feed it some arbitrary set of parameters :
print cmdopts.options

```


A bit more formal example :
```

#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-

if __name__ == '__main__' :
import cmdopts

# it's a "smart" (well, at least well-behaving) dictionary, so one can write :
if cmdopts.options['o'] == None and cmdopts.options['Option'] is None:
print "option is not specified (("

# as the only purpose of this script is demonstration,
# the only reasonable thing to do with arguments is print it :
print cmdopts.options

```


Now run any of these snippets as

```

python snippet.py --arg=value
python snippet.py --arg value
python snippet.py -A value
python snippet.py -Avalue
python snippet.py -Avalue -b
# ... your line here ...
```

-- and see what happens Ж:-)

If this looks as a snippet you were looking for, then [here](Description.md) is a more detailed description of the module.

And here is a direct link to [get the module code](http://py-command-line-options.googlecode.com/hg/cmdopt.py) .


