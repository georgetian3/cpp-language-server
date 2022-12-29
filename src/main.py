"""
Most of the block comments in this repository originate from the C++ Working Draft N4860
"""

import myply.lex as lex
from myply.yacc import yacc

from lexer.lexhtmlgenerator import LexHTMLGenerator

from lexer.tokens import *
import argparse

import json
from app import app

from lexer.tokens import NoCommentsLexer

from parser.myast import traverse
from parser.parser import *

arg_parser = argparse.ArgumentParser()
def parse_args():
    arg_parser.add_argument('-i', help='Source file (default test.cpp)', default='test.cpp')
    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument('-g', action='store_true', help='Run editor GUI')
    group.add_argument('-l', action='store_true', help='Run lexer')
    group.add_argument('-p', action='store_true', help='Run parser')
    args = arg_parser.parse_args()
    return args




input_file = ''

def run_lexer():
    with open(args.i, encoding='utf8') as f:
        source = f.read()
    l = lex.lex(debug=True, name_order=name_order)
    l.input(source)

    hg = LexHTMLGenerator()
    tokens = list(l)
    for token in tokens:
        hg.create_html_token(token)
    with open('output/tokens.txt', 'w') as f:
        f.write('\n'.join(map(str, tokens)))
    hg.write_html('output/tokens.html')
    print('Tokens saved in output/tokens.txt, HTMl saved in output/tokens.html')
    return l

def run_parser():
    with open(args.i, encoding='utf8') as f:
        source = f.read()
    parser = yacc(debug=False)
    ast = parser.parse(source, debug=True, lexer=NoCommentsLexer(lex.lexer))
    tree = traverse(ast)
    with open('output/ast.json', 'w') as f:
        json.dump(tree, f, indent=1)
    print('AST saved in output/ast.json')


if __name__ == '__main__':
    args = parse_args()
    input_file = args.i


    if args.l:
        run_lexer()
    elif args.p:
        run_parser()
    elif args.g:
        print('Visit http://127.0.0.1:5000')
        app.run()
    else:
        arg_parser.print_help()

