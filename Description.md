As I said, the module does "quick-and-dirty" command line parsing for those who (as myself) think that _typing extra code characters is a heresy_ -- and typing extra code lines is a crime Ж:-)

Informally, by <tt> import cmdopt </tt> we parse <tt> sys.argv </tt> and return a dictionary object.

If the command line had sth like <tt> --option 42 </tt>, then this dictionary will have a key/value pair <tt> { ...,  "option" : "42" , ... } </tt> .

Below follows a more formal description -- for those who wants to know about the corner cases and such .



# Options #

1. We consider everything that starts with '-' _an option key_, and everything else -- an option value or a positional argument (i.e. "not a value for some option"), depending on the context.

2. I will call every option key that starts from '--' _a long key_, and every option key that does not _a short key_ . ( So the short keys start only with a single '-' . )

3. For an option key, we strip the leading '-' or '--' to get the option name ; there are two exceptions -- (1) the dash character '-' alone gets a name '-' ( and value "True" ), and (2) two dashes '--' do not produce a key/value pair, **but stop any further option parsing** and treat all the remaining arguments as positional ones .

4. For an option value, there are three possibilities :

  * the corresponding value goes in the next command line argument, e.g. :
```

--option 42
-O 42
```

  * the corresponding value follows the option key within the same command line argument, e.g. :
```

--option=42
-O42
```
> > in this case, we assume that the value immediately follows the short option key -- and is separated by the equation character '=' from the long option keys ;

  * last, there could be no corresponding value, as for the '-o' flag in the examples below :
```

-o --option=42
-o -O42
-o --
```
> > note that in the last example we are following the standard convention, where command line argument '--' is treated as nor a value neither an option and marks the end of the command line options. ( Otherwise in <tt> -o something </tt> "something" would be recognized as the value for the option key "o" . )

5. Finally, we will call everything else in the command line -- i.e. everything that is not an option key or an option value, a _positional argument_ and they go to the <tt>cmdopt.options.args</tt> list.


# Usage #

1. We get and parse the command line arguments by simply importing the module, i.e. after
```

import cmdopts
```

we have access to the <tt> cmdopts.options </tt> dictionary, that has option keys as the keys ( with the leading '-' characters stripped ), and the option values, not surprisingly, as values.

The module silently tries to interpret the option values as python expressions, leaving them alone if that fails.
A dictionary of _uninterpreted_ options is avalable as <tt> cmdopts.string_options </tt>, so one can apply own conversion rules to achieve the desired behaviour.

Here is an example ( see the ..._test... files for more ) :_```

import sys
import cmdopt

options = cmdopt.string_options

print "before conversion:", options

conv_table = {    "i,int"    : int
,    "f,float"  : float
# custom stuff: translate integers starting with '0x' as base 16 ones, else as base 10 ones
,    "custom"   : lambda x: int(x[2:],16) if x.startswith('0x') else int(x) #
}


print "after conversion:", options.convert( conv_table )

```

Now the conversion table from the above will convert any options like <tt> "-i42" </tt> to a <tt> { "i" : 42 } </tt> pair, an option <tt> --float 2.7 </tt> would become <tt> { 'float': 2.7000000000000002 } </tt> ( or so, depending on the round-off error ), and any "custom" option value would be treated as an integer (base 16 for '0x'-prefixed numbers and base 10 for the rest): <tt> --custom 0xB </tt> => <tt> { 'custom': 11 } </tt> .


2. To access the positional arguments, use <tt>.args</tt> .

For example, for a command line
<tt> sample.py --option1 1 --option2 2 -- 3 </tt>

the code
```

import sys
import cmdopt

# print cmdopt.options

for arg in cmdopt.options.args:
print arg

```

will print "3" as the output .


3. Finally, it is probably worth mentioning that the returned dictionary object is completely free from the 'KeyError' disease ( i.e. the item `[ ... ]` access works exactly as Python dict().get( ... ) method ), so one can do simple checks like :
```

if cmdopt.options['O'] is None and cmdopt.options['option'] is None:

print " neither '-O' nor '--option' keys were specified ! "

```


# Pitfalls #

1. If the same option key would be given twice with different option values, **the last one will be used**. For example, <tt> -o1 -o2 -o3 </tt> will simply result in <tt> { 'o': 3 } </tt>, what might not be the desired behaviour.

Feel free to grab the code and replace the returned object to a list of pairs to change this .

2. Single-character options can't be combined in a single word: <tt> -abcd </tt> would yield <tt> { 'a': 'bcd' } </tt> . To get <tt> {'a': True, 'c': True, 'b': True, 'd': True} </tt>, pass in the command line <tt> -a -b -c -d </tt> instead .

<a href='Hidden comment: 

= Download =

I have noticed that for the ones who are not acquainted with the Google Code it is sometimes difficult to figure out how to actually get the stuff Ж:-)

So here is [http://py-command-line-options.googlecode.com/hg/cmdopt.py a direct link to the file]

'></a>