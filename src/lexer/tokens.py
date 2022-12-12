
from .identifiers import t_IDENTIFIER
from .keywords import keywords
from .operators import operator_or_punctuators


from .literals import t_STRING_LITERAL, t_LITERAL
from .comments import t_COMMENT, t_WHITESPACE

"""
5.6 Tokens

There are five kinds of tokens: identifiers, keywords, literals, operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, “white space”), as described below, are ignored except as they serve to separate tokens. [ Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note ]
"""


t_USER_DEFINED_STRING_LITERAL = r'ttttoooodddoooo'

tokens = [
    'WHITESPACE',
    'COMMENT',
    'IDENTIFIER',
    'LITERAL',
    'STRING_LITERAL',
    'Q_CHAR_SEQUENCE',
    'H_CHAR_SEQUENCE',
    'USER_DEFINED_STRING_LITERAL'
]

literals = '{}[]();:?.~!+-*/%^&|=<>,\#'
tokens += [keyword.upper() for keyword in keywords]

for name, symbol in operator_or_punctuators.items():
    globals()['t_' + name.upper()] = symbol
    tokens.append(name.upper())

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

