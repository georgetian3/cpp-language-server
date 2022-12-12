

from .myast import InternalNode

def p_start(p):
    ''' start : start pp_include 
              | start declaration 
              | pp_include
              | declaration '''
    p[0] = InternalNode('start', p[1:])

from .opts import *
from .preprocessing import *
from .expressions import *
from .statements import *
from .declarations import *
from .classes import *

def p_empty(p):
    'empty :'
    p[0] = {'empty': 'empty'}


start = 'start'

from ply.yacc import yacc

def p_error(p):
    print('[Error]: type - %s, value - %s, lineno - %d, lexpos - %d' % (p.type, p.value, p.lineno, p.lexpos))

