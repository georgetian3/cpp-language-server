from .base import *

def p_operator_function_id(p):
    ''' operator_function_id : OPERATOR operator '''

def p_operator(p):
    ''' operator : NEW
                 | DELETE
                 | NEW '[' ']'
                 | DELETE '[' ']'
                 | CO_AWAIT '(' ')'
                 | '[' ']'

                 '''