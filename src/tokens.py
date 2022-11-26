from characters import *
from comments import *
from identifiers import identifier
from keywords import keywords
from literals import *
from operators import preprocessing_operators, operator_or_punctuators

from pprint import pprint


"""
5.6 Tokens

There are five kinds of tokens: identifiers, keywords, literals, operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, “white space”), as described below, are ignored except as they serve to separate tokens. [ Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note ]
"""


token_tree = {
    'identifier': identifier,
    'keyword': {
        keyword: keyword for keyword in keywords
    },
    'literal': {
        'integer': '[0-9]+',
        'character': '\'[A-Za-z]?\'',
        'floating_point': '[0-9]+.[0-9]+',
        'string': '"[A-Za-z]*"',
        'boolean': 'true|false',
        'pointer': '->',
        'user_defined': 'sdfsdfsd',
    },
    'operator_or_punctuator': {
        #'alternative': alternative_tokens,
        'preprocessing_operators': preprocessing_operators,
        **operator_or_punctuators,
    },
    'separator': {
        'comment': {
            'multi_line': '//$',
            'single_line': '/*.?*/',
        },
        'space': '\s',
    },
}


tokens = []

__special_chars = set(['.', '+', '*', '?', '^', '$', '(', ')', '[', ']', '{', '}', '|', '\\', '#'])

def escape_special_chars(s):
    output = []
    for char in s:
        if char in __special_chars:
            output += '\\' + char
        else:
            output += char
    return ''.join(output)


def generate_tokens(token_tree, path=''):
    for token in token_tree:
        new_path = path + '_' + token.upper()
        if type(token_tree[token]) == dict:
            generate_tokens(token_tree[token], new_path)
        elif type(token_tree[token]) == str:
            globals()['t' + new_path] = escape_special_chars(token_tree[token])
            tokens.append(new_path[1:])

generate_tokens(token_tree)

#pprint(tokens)
#pprint(globals())

