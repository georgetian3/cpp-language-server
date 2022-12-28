

from .myast import InternalNode

def p_start(p):
    '''
        start   : pp_include start
                | declaration start
                | pp_include
                | declaration
    '''

    if len(p) == 2:
        children = p[1:]
    else:
        children = p[1:]

    p[0] = InternalNode('start', children)


from .opts import *
from .preprocessing import *
from .expressions import *
from .declarations import *
from .statements import *
from .classes import *

def p_empty(p):
    'empty :'
    p[0] = {'empty': 'empty'}


start = 'start'

from ply.yacc import yacc
