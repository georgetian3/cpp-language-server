"""
5.4 Proprocessing tokenss
"""

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
5.6 Tokens

There are five kinds of tokens: identifiers, keywords, literals, 18 operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, “white space”), as described below, are ignored except as they serve to separate tokens. [ Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note ]
"""

tokens = (
    'IDENTIFIER',
    'KEYWORD',
    'LITERAL',
    'OPERATOR',
    'SEPARATOR',
)

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'

def t_KEYWORD(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    
def t_LITERAL(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    
def t_OPERATOR(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    
def t_SEPARATOR(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    