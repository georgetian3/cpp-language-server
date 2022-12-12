from .opts import *
from .basics import *
from .expressions import *
from .statements import *
from .declarations import *
from .modules import *
from .classes import *
from .overloading import *
from .templates import *
from .exceptions import *
from .preprocessing import *
from .keywords import *

from .myast import ExternalNode

def p_empty(p):
    'empty :'
    p[0] = {'empty': 'empty'}

from ply.yacc import yacc

def p_error(p):
    print('[Error]: type - %s, value - %s, lineno - %d, lexpos - %d' % (p.type, p.value, p.lineno, p.lexpos))


parser = None#yacc()