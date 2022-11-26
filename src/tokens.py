from characters import *
from comments import *
from identifiers import identifier
from keywords import *
from literals import *
from operators import *



"""
5.6 Tokens

There are five kinds of tokens: identifiers, keywords, literals, operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, “white space”), as described below, are ignored except as they serve to separate tokens. [ Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note ]
"""

from keywords import keywords
from operators import preprocessing_operators, operator_or_punctuators

token_tree = {
    'identifier': identifier,
    'keyword': {
        keyword: keyword for keyword in keywords
    },
    'literal': {
        'integer': {},
        'character': {},
        'floating_point': {},
        'string': {},
        'boolean': {},
        'pointer': {},
        'user_defined': {},
    },
    'operator_or_punctuator': {
        'alternative': alternative_tokens,
        'preprocessing_operators': preprocessing_operators,
        'operator_or_punctuator': operator_or_punctuators,
    },
    'separator': {
        'comment': {
            'multi_line': '',
            'single_line': '',
        },
        'space': ' ',
    },
}


tokens = []


def generate_tokens(token_tree, path=''):
    for token in token_tree:
        if type(token) == dict:
            generate_tokens(token_tree, path + '_' + token)
        elif type(token) == str:
            globals()['t' + path] = token
            tokens.append(path)

generate_tokens(token_tree)

print(tokens)

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)