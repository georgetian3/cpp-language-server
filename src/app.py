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
    elements = find_element(ast)
    print(elements)
    suggestions = []
    if len(tokens) > 0:
        partial = tokens[-1].value
        for keyword in keywords:
            if partial == keyword[:len(partial)] and partial != keyword:
                suggestions.append({'full':keyword,'complete':keyword[len(partial):]})
        for element in elements:
            if partial == element['complete'][:len(partial)] and partial != element['complete']:
                suggestions.append({'full':element['full'],'complete':element['complete'][len(partial):]})
    res = ''.join(formatted_tokens)

    #print('Formatting:', res)
    #print('Autocomplete:', suggestions)
    return {'formatting': res, 'suggestions': suggestions}
def process_function(function_list,full = '',complete = '',flag = 0):
    for i, item in enumerate(function_list):
        if isinstance(item,str):
            if item == 'type_specifier':
                flag = 1
        elif isinstance(item,list):
            full,complete = process_function(item,full,complete,flag)
        elif isinstance(item,dict):
            k = item.keys()
            v = item.values()
            if list(v)[0] == "{'empty': 'empty'}":
                continue
            if flag != 1:
                complete = complete + ' ' + list(v)[0]
            flag = 0
            full = full + ' ' + list(v)[0]
    return full.lstrip(),complete.lstrip()
def find_element(ast,result = []):
    flag = 0
    for i,item in enumerate(ast):
        if flag == 1:
            flag = 0
            continue
        if isinstance(item,str):
            if item == 'function_declaration':
                full , complete = process_function(ast[i+1])
                print(f'there is a function')
                result.append({'full':full,'complete':complete})
                flag = 1
        elif isinstance(item,list):
            result = find_element(item,result)
        elif isinstance(item,dict):
            if 'IDENTIFIER' in item:
                result.append({'full':item['IDENTIFIER'],'complete':item['IDENTIFIER']})
    return result
if __name__ == '__main__':
    app.run(debug=False, port='5000')