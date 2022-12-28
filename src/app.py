from flask import Flask, send_file, request
from flask_cors import CORS
import ply.lex as lex
from ply.yacc import yacc
from lexer.tokens import *
from lexer.keywords import keywords
from lexer.tokens import literals
from lexer.operators import operator_or_punctuators
from functools import reduce
from parser.myast import traverse
from parser.parser import *
import html
import time
import logging

def list_dict_duplicate_removal(data_list):
    run_function = lambda x, y: x if y in x else x + [y]
    return reduce(run_function, [[], ] + data_list)


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
    data = request.get_json()
    src = data['text']
    cursor = data['cursor']
    print('Source:', src)
    print('Cursor:', cursor)

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
        whitespace = whitespace.replace(' ', '&ensp;')
        whitespace = whitespace.replace('\n', '<br>')
        formatted_tokens.append(whitespace)
        prev_index = index + len(token.value)

        type = token.type.lower()
        if type in keywords:
            type = 'keyword'
        elif type in literals or type in operator_or_punctuators or type in operator_or_punctuators.values():
            type = 'operator'
        formatted_tokens.append(f'<span class="{type}">{html.escape(token.value)}</span>')
    elements,table = find_element(ast)
    elements = list_dict_duplicate_removal(elements)
    print(elements)
    suggestions = []
    i = cursor
    while(i <= len(src) and i > 0 and  not ' ' in src[i-1] and not '\n' in src[i-1] and not ',' in src[i-1]):
        i -= 1
    partial = src[i:cursor]
    print(f'partial is {partial}')
    if len(tokens) > 0 and partial !='':
        for keyword in keywords:
            if partial == keyword[:len(partial)] and partial != keyword:
                suggestions.append({'full':keyword,'complete':keyword[len(partial):]})
        for element in elements:
            if partial == element['complete'][:len(partial)] and partial != element['complete']:
                suggestions.append({'full':element['full'],'complete':element['complete'][len(partial):]})
        if partial[-1] == '.':
            for k,v in table.items():
                if partial[:-1] == k:
                    if isinstance(v,str):
                        type_list = ['int','float','double','char','bool']
                        if v not in type_list:
                            members = table[v]['member']
                            for member in members:
                                if isinstance(member,str):
                                    suggestions.append({'full':member,'complete':member})
                                elif isinstance(member,dict):
                                    suggestions.append({'full':member['full'],'complete':member['complete']})


    res = ''.join(formatted_tokens)
    #print('Formatting:', res)
    print('Autocomplete:', suggestions)
    return {'formatting': res, 'suggestions': list(suggestions)}
    
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
def find_class_name(declarations,result=None):
    for i,item in enumerate(declarations):
        if isinstance(item,str):
            continue
        elif isinstance(item,list):
            result = find_class_name(item)
        elif isinstance(item,dict):
            if 'IDENTIFIER' in item:
                result = item['IDENTIFIER']
    return result
def find_member(declarations,result=None):
    if result is None:
        result = []
    flag = 0
    for i,item in enumerate(declarations):
        if flag == 1:
            flag = 0
            continue
        if isinstance(item,str):
            if item == 'function_declaration_definition':
                full,complete = process_function(declarations[i+1][0][1])
                flag = 1
                result.append({'full':full,'complete':complete})
        elif isinstance(item,list):
            result = find_member(item,result)
        elif isinstance(item,dict):
            if 'IDENTIFIER' in item:
                result.append(item['IDENTIFIER']) 
    return result
def find_type(declarations , result = None):
    for i,item in enumerate(declarations):
        if isinstance(item,str):
            continue
        elif isinstance(item,list):
            result = find_type(item,result)
        elif isinstance(item,dict):
            type_list = ['IDENTIFIER','int','float','double','char','bool']
            for type in type_list:
                if type in item:
                    result = item[type] 
    return result
def add_to_table(type,declarations,table):
    if type == 'class_declaration_definition':
        class_name = find_class_name(declarations[0])
        table[class_name] = {'type':'class','member':[]}
        member = find_member(declarations[1:])
        table[class_name]['member']=member
    elif type == 'simple_declaration':
        type = find_type(declarations[0])
        name = declarations[2]['IDENTIFIER']
        table[name] = type
    return table
def find_element(ast,result = None,table = None):
    flag = 0
    if result is None:
        result = []
    if table is None:
        table = {}
    for i,item in enumerate(ast):
        if flag == 1:
            flag = 0
            continue
        if isinstance(item,str):
            if item == 'function_declaration':
                full , complete = process_function(ast[i+1])
                result.append({'full':full,'complete':complete})
                flag = 1
            if item == 'class_declaration_definition' or item == 'simple_declaration':
                table = add_to_table(ast[i],ast[i+1],table)
                print(f'table is {table}')
                flag = 1 
        elif isinstance(item,list):
            result,table = find_element(item,result,table)
        elif isinstance(item,dict):
            if 'IDENTIFIER' in item:
                result.append({'full':item['IDENTIFIER'],'complete':item['IDENTIFIER']})
    return result,table
if __name__ == '__main__':
    app.run(debug=False, port='5000')