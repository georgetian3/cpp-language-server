from flask import Flask, send_file, request
from flask_cors import CORS
import ply.lex as lex
from ply.yacc import yacc
from lexer.tokens import *
from lexer.keywords import keywords
from lexer.tokens import literals
from lexer.operators import operator_or_punctuators
from parser.myast import traverse
from parser.parser import *
import html
import time
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app)

lexer = lex.lex(debug=False)
parser = yacc(debug=False)


def get_tokens(src):
    lexer.input(src)
    return list(lexer)

def run_parser(src):
    ast = parser.parse(src, debug=False)
    tree = traverse(ast)
    return tree


@app.get('/')
def index_get():
    return send_file('static/editor.html')

ast = {}

@app.post('/process')
def process():
    src = request.data.decode('utf8')
    print('Source:', src)

    tokens = get_tokens(src)
    temp = run_parser(src)

    global ast
    if temp != {None: None}:
        ast = temp
    print(ast)

    formatted_tokens = []
    prev_index = 0
    for token in tokens:
        #print(token.value.ljust(20, ' '), token.type)
        index = src.find(token.value, prev_index)
        whitespace = src[prev_index : index]
        whitespace = whitespace.replace(' ', '&nbsp;')
        whitespace = whitespace.replace('\n', '<br>')
        formatted_tokens.append(whitespace)
        prev_index = index + len(token.value)

        type = token.type.lower()
        if type in keywords:
            type = 'keyword'
        elif type in literals or type in operator_or_punctuators or type in operator_or_punctuators.values():
            type = 'operator'
        formatted_tokens.append(f'<span class="{type}">{html.escape(token.value)}</span>')

    suggestions = []
    if len(tokens) > 0:
        partial = tokens[-1].value
        for keyword in keywords:
            if partial == keyword[:len(partial)] and partial != keyword:
                suggestions.append(f'{html.escape(partial)}<span class="remaining">{html.escape(keyword[len(partial):])}</span>')

    res = ''.join(formatted_tokens)
    #print('Formatting:', res)
    #print('Autocomplete:', suggestions)
    return {'formatting': res, 'suggestions': suggestions}


if __name__ == '__main__':
    app.run(debug=False, port='5000')