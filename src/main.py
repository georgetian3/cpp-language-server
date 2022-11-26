"""
Most of the block comments in this repository originate from the C++ Working Draft N4860
"""

from lexhtmlgenerator import LexHTMLGenerator
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
    parser.add_argument('source_file', help='Source file to be lexed')
    args = parser.parse_args()
    return args

if __name__ == '__main__':


    args = parse_args()
    source_file = args.source_file

    with open(source_file, encoding='utf8') as f:
        source = f.read()

    lexer = lex.lex(debug=False)
    lexer.input(source)

    hg = LexHTMLGenerator()
    for token in lexer:
       print(token)
       #hg.create_html_token(token)

    hg.write_html('output/output.html')