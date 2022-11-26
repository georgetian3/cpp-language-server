"""
Most of the block comments in this repository originate from the C++ Working Draft N4860
"""

import ply.lex as lex
from characters import *
from comments import *
from identifiers import *
from keywords import *
from literals import *
from operators import *
from tokens import *

tokens = [
    'LITERAL',
    'IDENTIFIER',
    'SEPARATOR',
    'OPERATOR_OR_PUNCTUATOR',
    'PREPROCESSING_OPERATOR',
    *(keyword.upper() for keyword in keywords)
]

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


if __name__ == '__main__':

    with open('test.cpp', encoding='utf8') as f:
        input = f.read()

    lexer = lex.lex(debug=False)
    lexer.input(input)

    for token in lexer:
        print(token)