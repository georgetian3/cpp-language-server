from .base import *

def p_operator_function_id(p):
    ''' operator_function_id : OPERATOR operator '''
    p[0] = Node('operator_function_id', '', p[1:])


def p_operator(p):
    ''' operator : NEW
                 | DELETE
                 | NEW '[' ']'
                 | DELETE '[' ']'
                 | CO_AWAIT '(' ')'
                 | '[' ']'
                 | ARROW
                 | ARROWSTAR
                 | '~'
                 | '!'
                 | '+'
                 | '-'
                 | '*'
                 | '/'
                 | '%'
                 | '^'
                 | '&'
                 | '|'
                 | '='
                 | PLUSEQUAL
                 | MINUSEQUAL
                 | TIMESEQUAL
                 | DIVEQUAL
                 | MODEQUAL
                 | XOREQUAL
                 | ANDEQUAL
                 | OREQUAL
                 | EQ
                 | NE
                 | '<'
                 | '>'
                 | LE
                 | GE
                 | SPACESHIP
                 | LAND
                 | LOR
                 | LSHIFT
                 | RSHIFT
                 | LSHIFTEQUAL
                 | RSHIFTEQUAL
                 | PLUSPLUS
                 | MINUSMINUS
                 | ',' '''
    p[0] = Node('operator', '', p[1:])

def p_literal_operator_id(p):
    ''' literal_operator_id : OPERATOR STRING_LITERAL IDENTIFIER
                            | OPERATOR USER_DEFINED_STRING_LITERAL '''
    p[0] = Node('literal_operator_id', '', p[1:])