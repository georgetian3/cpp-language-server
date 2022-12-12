""" 
from .basics import *
from .expressions import *
from .statements import *
from .declarations import *
 """


def p_start(p):
    ''' start : pp_include start
              | expression start 
              | empty '''

#from .opts import *
from .preprocessing import *
from .expressions import *
#from .statements import *
#from .declarations import *
#from .classes import *

def p_empty(p):
    'empty :'
    p[0] = {'empty': 'empty'}

from ply.yacc import yacc

def p_error(p):
    print('[Error]: type - %s, value - %s, lineno - %d, lexpos - %d' % (p.type, p.value, p.lineno, p.lexpos))

