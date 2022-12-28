from flask import Flask, send_file, request
from flask_cors import CORS
import ply.lex as lex
from ply.yacc import yacc
from lexer.tokens import *
from parser.myast import traverse
from parser.parser import *

app = Flask(__name__)
CORS(app)

lexer = lex.lex(debug=False)

def get_tokens(src):
    lexer.input(src)
    return list(lexer)

def run_parser(src):
    parser = yacc(debug=False)
    ast = parser.parse(src, debug=False)
    tree = traverse(ast)
    return tree


@app.get('/')
def index_get():
    return send_file('static/editor.html')

@app.post('/process')
def process():
    src = request.data.decode('utf8')
    print('Source:', src)

    res = '<span style="color:white">' + src + '</span>'
    suggestions = ['test', 'test1']
    print('Formatting:', res)
    print('Autocomplete:', suggestions)
    return {'formatting': res, 'suggestions': suggestions}


if __name__ == '__main__':
    app.run(debug=False, port='5000')