
from characters import *
from comments import *
from identifiers import identifier
from keywords import keywords
#from literals import *
from operators import preprocessing_operators, operator_or_punctuators

from pprint import pprint


"""
5.6 Tokens

There are five kinds of tokens: identifiers, keywords, literals, operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, “white space”), as described below, are ignored except as they serve to separate tokens. [ Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note ]
"""

token_tree = {
    'preprocessing': 'adfasdfas', # TODO
    'keyword': {
        keyword: keyword for keyword in keywords
    },
    'literal': {
        'floating_point': '[0-9]+\.[0-9]+', # TODO
        'integer': '[0-9]+', # TODO
        'character': '\'[A-Za-z]?\'', # TODO
        'string': '"[A-Za-z]*"', # TODO
        'boolean': 'true|false', # TODO
        'pointer': '->', # TODO
        'user_defined': 'sdfsdfsd', # TODO
    },
    'operator_or_punctuator': {
        #'alternative': alternative_tokens,
        'preprocessing_operators': preprocessing_operators,
        **operator_or_punctuators,
    },
    'separator': {
        'comment': {
            'single_line': '//.*',
            'multi_line': '/\*.*?\*/',
        },
        'space': '\s', # TODO
    },
    'identifier': identifier,
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
            if 'OPERATOR_OR_PUNCTUATOR' in path:
                globals()['t' + new_path] = escape_special_chars(token_tree[token])
            else:
                globals()['t' + new_path] = token_tree[token]
            tokens.append(new_path[1:])
        elif type(token_tree[token]) == function:
            # TODO: ???
            pass
        else:
            print('???')
            exit()

generate_tokens(token_tree)

pprint(tokens)
pprint(globals())
