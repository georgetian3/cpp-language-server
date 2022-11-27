"""
Most of the block comments in this repository originate from the C++ Working Draft N4860
"""

from lexhtmlgenerator import LexHTMLGenerator
import ply.lex as lex
from tokens import *
import argparse


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='Source file to be lexed')
    parser.add_argument('-o', help='Destination file to save token stream')
    args = parser.parse_args()
    return args

if __name__ == '__main__':


    args = parse_args()

    with open(args.i, encoding='utf8') as f:
        source = f.read()

    lexer = lex.lex(debug=False)
    lexer.input(source)

    hg = LexHTMLGenerator()
    tokens = list(lexer)
    for token in tokens:
        hg.create_html_token(token)

    hg.write_html('output/output.html')

    with open(args.o, 'w', encoding='utf8') as f:
        f.write('\n'.join(str(token) for token in tokens))