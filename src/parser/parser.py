from .expressions import *
from .statements import *
from .declarations import *

from ply.yacc import yacc

def p_error(p):
    print('[Error]: type - %s, value - %s, lineno - %d, lexpos - %d' % (p.type, p.value, p.lineno, p.lexpos))


parser = None#yacc()