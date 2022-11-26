"""
Most of the block comments in this repository originate from the C++ Working Draft N4860
"""

from ply.lex import lex
from characters import *
from comments import *
from identifiers import *
from keywords import *
from literals import *
from operators import *
from tokens import *

import argparse
from lexhtmlgenerator import LexHTMLGenerator

tokens = [
    'LITERAL',
    'IDENTIFIER',
    'SEPARATOR',
    'OPERATOR_OR_PUNCTUATOR',
    'PREPROCESSING_OPERATOR',
    'COMMENT_SINGLE_LINE',
    'COMMENT_MULTI_LINE',
    *(keyword.upper() for keyword in keywords)
]

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', help='Source file to be lexed')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    hg = LexHTMLGenerator()

    args = parse_args()
    source_file = args.source_file

    with open(source_file, encoding='utf8') as f:
        source = f.read()

    lexer = lex(debug=False)
    lexer.input(source)

    for token in lexer:
        hg.create_html_token(token)

    hg.write_html('output/index.html')