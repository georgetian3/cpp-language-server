"""
Most of the block comments in this repository originate from the C++ Working Draft N4860
"""
import ply
import ply.yacc as yacc

from lexer.lexhtmlgenerator import LexHTMLGenerator

from lexer.tokens import *
import argparse




def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='Source file to be lexed')
    parser.add_argument('-o', help='Destination file to save token stream')
    args = parser.parse_args()
    return args


def run_lexer():
    args = parse_args()

    with open('test.cpp', encoding='utf8') as f:
        source = f.read()

    lexer = ply.lex.lex(debug=True)
    lexer.input(source)

    hg = LexHTMLGenerator()
    tokens = list(lexer)
    for token in tokens:
        hg.create_html_token(token)

    hg.write_html('output/output.html')

    """ with open(args.o, 'w', encoding='utf8') as f:
        f.write('\n'.join(str(token) for token in tokens)) """

    """ lexer = lex.lex(debug=False)
    lexer.input(source)
    return lexer """

def run_parser():
    args = parse_args()
    with open(args.i, encoding='utf8') as f:
        source = f.read()


    parser = yacc.parse(lexer=run_lexer())
    parser.parse(source, debug=True)    


import re
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

if __name__ == '__main__':
    run_lexer()
    #run_parser()
    #format()
    """ expr = '2 * 3 + 4 * (5 - x)'
    ast = AST(parser.parse(expr, debug=False))
    print(expr)
    pprint(ast.get_list()) """


    