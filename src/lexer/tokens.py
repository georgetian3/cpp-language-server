
from .characters import *
from .comments import *
from .identifiers import t_IDENTIFIER
from .keywords import keywords
#from literals import *
from .operators import preprocessing_operators, operator_or_punctuators

from pprint import pprint

import types
from collections import OrderedDict
from .literals import t_DEC_FLOAT_LITERAL, t_BINARY_LITERAL, t_OCT_LITERAL, t_HEX_LITERAL, t_DEC_LITERAL, t_STRING_LITERAL

"""
5.6 Tokens

There are five kinds of tokens: identifiers, keywords, literals, operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, “white space”), as described below, are ignored except as they serve to separate tokens. [ Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note ]
"""

token_tree = {
    'preprocessing': 'adfaasdfasdfsdfas', # TODO
    'literal': {
        'floating_point': {
            'decimal': 't_DEC_FLOAT_LITERAL',
        },
        'integer': {
            'binary': 't_BINARY_LITERAL',
            'oct': 't_OCT_LITERAL',
            'hex': 't_HEX_LITERAL',
            'dec': 't_DEC_LITERAL',
        },
        'character': '\'.?\'', #'t_CHARACTER_LITERAL',
        'string': 't_STRING_LITERAL',
        'boolean': 'true|false',
        'pointer': 'nullptr',
        'user_defined': 'sdasdfasdfasdffsdfsd', # TODO
    },
    'operator_or_punctuator': {
        #'alternative': alternative_tokens,
        'preprocessing_operators': preprocessing_operators,
        **operator_or_punctuators,
    },
    'separator': {
        'comment': {
            'single_line': '//.*\n',
            'multi_line': r'(/\*(.|\n)*?\*/)',
        },
        'space': 't_WS', # TODO
    },
}

""" token_tree = (
    ('separator',
        (
            ('comment',
                    (
                        ('single_line', '//.*\n'),
                        ('multi_line', r'(/\*(.|\n)*?\*/)'),
                    ),
            ),
            ('space', whitespace), # TODO
        )
    ),
    ('preprocessing', 'adfasdfas'), # TODO
    ('keyword',
        (
            tuple((keyword, keyword) for keyword in keywords)
        )
    ),
    ('literal',
        (
            ('floating_point', '[0-9]+\.[0-9]+'), # TODO
            ('integer', '[0-9]+'), # TODO
            ('character', '\'[A-Za-z]?\''), # TODO
            ('string', '"[A-Za-z]*"'), # TODO
            ('boolean', 'true|false'), # TODO
            ('pointer', 'nullptr'), # TODO
            ('user_defined', 'sdfsdfsd'), # TODO
        )
    ),
    ('operator_or_punctuator',
        (
            #'alternative', alternative_tokens,
            ('preprocessing_operators', preprocessing_operators),
            *((k, v) for k, v in operator_or_punctuators.items()),
        )
    ),
    ('identifier', identifier),
) """


#pprint(token_tree)



tokens = ['IDENTIFIER', 'LITERAL']


tokens += list(keywords.values())


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
            if token_tree[token][:2] == 't_':
                tokens.append(token_tree[token][2:])
                continue
            if 'OPERATOR_OR_PUNCTUATOR' in path:
                globals()['t' + new_path] = escape_special_chars(token_tree[token])
            else:
                globals()['t' + new_path] = token_tree[token]
            tokens.append(new_path[1:])
        elif type(token_tree[token]) == types.FunctionType:
            #token_tree[token].__name__ = 't' + new_path
            tokens.append(token_tree[token].__name__[2:])
        else:
            print('???')
            exit()

generate_tokens(token_tree)

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#pprint(globals())
