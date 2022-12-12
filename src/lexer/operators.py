"""
5.5 Alternative tokens
1   Alternative token representations are provided for some operators and punctuators.
2   In all respects of the language, each alternative token behaves the same, respectively, as its primary token, except for its spelling.12 The set of alternative tokens is defined in `alternative_tokens`.
"""

alternative_tokens = {
    '<%': '{',
    '%>': '}',
    '<:': '[',
    ':>': ']',
    '%:': '#',
    '%:%:': '##',
    'and': '&&',
    'bitor': '|',
    'or': '||',
    'xor': '^',
    'compl': '~',
    'bitand': '&',
    'and_eq': '&=',
    'or_eq': '|=',
    'xor_eq': '^=',
    'not': '!',
    'not_eq': '!=',
}


"""
5.12 Operators and punctuators
1   The lexical representation of C++ programs includes a number of preprocessing tokens that are used in the syntax of the preprocessor or are converted into tokens for operators and punctuators:

Each operator-or-punctuator is converted to a single token in translation phase 7 (5.2).
"""

preprocessing_operators = {
    'pphash': r'\#',
    'ppdhash': r'\#\#', # TODO: find official name

}
operator_or_punctuators = {
    #'pphash': r'\#',
    'ppdhash': r'\#\#', # TODO: find official name

    #'lbrace': '\{',
    #'rbrace': '\}',
    #'lbracket': '\[',
    #'rbracket': '\]',
    #'lparen': '\(', 
    #'rparen': '\)',
    #'semi': ';',
    #'colon': ':',
    'ellipsis': '\.\.\.',
    #'condop': '\?',
    'dcolon': '::', # TODO: find official name
    #'period': '\.',
    'periodstar': '\.\*', # TODO: find official name
    'arrow': '-\>',
    'arrowstar': '-\>\*', # TODO: find official name
    #'not': '~',
    #'lnot': '!',
    #'plus': '+',
    #'minus': '-',
    #'times': '*',
    #'divide': '/',
    #'mod': '%',
    #'xor': '^',
    #'and': '&',
    #'or': '|',
    #'equals': '=',
    'plusequal': '\+=',
    'minusequal': '-=',
    'timesequal': '\*=',
    'divequal': '/=',
    'modequal': '%=',
    'xorequal': '^=',
    'andequal': '&=',
    'orequal': '\|=',
    'eq': '==',
    'ne': '!=',
    #'lt': '<',
    #'gt': '>',
    'le': '<=',
    'ge': '>=',
    'spaceship': '<=>',
    'land': '&&',
    'lor': '\|\|',
    'lshift': '<<',
    'rshift': '>>',
    'lshiftequal': '<<=',
    'rshiftequal': '>>=',
    'plusplus': '\+\+',
    'minusminus': '\-\-',
    #'comma': ',',
}

# TODO: alternative tokens
'''
    '': '%:',
    '': '%:%:',
    '': '<:',
    '': ':>',
    '': '<%',
    '': '%>',
    '': 'and',
    '': 'or',
    '': 'xor',
    '': 'not',
    '': 'bitand',
    '': 'bitor',
    '': 'compl',
    '': 'and_eq',
    '': 'or_eq',
    '': 'xor_eq',
    '': 'not_eq'
'''


for name, symbol in operator_or_punctuators.items():
    globals()['t_' + name.upper()] = symbol



if __name__ == '__main__':
    pass