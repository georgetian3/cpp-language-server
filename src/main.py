"""
Most of the block comments in this repository originate from the C++ Working Draft N4860
"""
import myply.lex as lex
from myply.yacc import yacc

from lexer.lexhtmlgenerator import LexHTMLGenerator

from lexer.tokens import *
import argparse
import re

import json

import lexer


from parser.myast import traverse
from parser.parser import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='Source file to be lexed')
    parser.add_argument('-o', help='Destination file to save token stream')
    args = parser.parse_args()
    return args


class NoCommentsLexer(lex.Lexer):
    def __init__(self, parent):
        self.__dict__ = parent.__dict__.copy()
    def token(self):
        while True:
            token = super().token()
            if token is None:
                return None
            elif token.type != 'comment':
                return token

test_file = 'test.cpp'

def run_lexer():
    args = parse_args()

    with open(test_file, encoding='utf8') as f:
        source = f.read()
    l = lex.lex(debug=True, name_order=name_order)
    l.input(source)

    hg = LexHTMLGenerator()
    tokens = list(l)
    for token in tokens:
        hg.create_html_token(token)

    hg.write_html('output/output.html')
    return l

def run_parser():
    args = parse_args()
    with open(test_file, encoding='utf8') as f:
        source = f.read()


    parser = yacc(debugfile='parser.out', debug=True)
    ast = parser.parse(source, debug=True, lexer=NoCommentsLexer(lex.lexer))
    print(ast)
    tree = traverse(ast)
    print(tree)
    with open('out.json', 'w') as f:
        json.dump(tree, f, indent=1)


def format():
    with open('in.txt') as f:
        text = f.read()
    text = text.replace('\\br', '')
    text = text.replace('-', '_')
    text = re.sub(r'\\.+?\{(.*?)\}', r'\1', text)


    head, *prods = text.split('\n')
    head = head[:-2]

    f_def = f'def p_{head}(p):\n'
    head = "    ''' " + head + ' '
    prefix = ' ' * len(head) + '| '
    head += ': ' + prods[0] + '\n'
    del prods[0]
    for i in range(len(prods)):
        prods[i] = prefix + prods[i]
    if prods:
        prods[-1] += " '''"
    else:
        head = head[:-1] + " '''"
    text = f_def + head + '\n'.join(prods)
    print(text)


""" precedence = (
    ('left', 'function_definition', 'IDENTIFIER'),
) """




import re
import lexer.literals
import lexer.digits
import lexer.identifiers
if __name__ == '__main__':
    run_lexer()
    run_parser()
    exit()
    text = 'u\'e\''
    #print(lexer.literals.fractional_constant)
    #print(re.fullmatch(lexer.digits.digit_sequence, text))
    print(lexer.literals.character_literal)
    print(re.fullmatch(lexer.literals.character_literal, text))
