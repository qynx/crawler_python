# -*- coding :utf-8 -*-

"""
Usage:
    test [-gf] <from> <to> <date>
    
Options:
    -g    是
    -f    项
    
Example:
    test 北京 上海 2016-10-10
    
"""
from docopt import docopt
def cli():
    
    print ('this is a test..')
    #print (__doc__)
    arguments=docopt(__doc__)
    print ('haha;')
    print (arguments)
    options=''.join([key for key,value in arguments.items() if value  is True])
    print (type(options),options)
if __name__=='__main__':
    cli()
