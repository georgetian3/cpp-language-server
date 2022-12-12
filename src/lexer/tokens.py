
from .keywords import keywords
from .operators import operator_or_punctuators


from .literals import t_STRING_LITERAL, t_LITERAL
from .comments import t_COMMENT, t_WHITESPACE
from .identifiers import t_IDENTIFIER

"""
5.6 Tokens

There are five kinds of tokens: identifiers, keywords, literals, operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, “white space”), as described below, are ignored except as they serve to separate tokens. [ Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note ]
"""



tokens = [
    'COMMENT',
    'WHITESPACE',
    'LITERAL',
    'STRING_LITERAL',
    'IDENTIFIER',
]

literals = r'{}[]();:?.~!+-*/%^&$|=<>,\#'
tokens += [keyword.upper() for keyword in keywords]

for name, symbol in operator_or_punctuators.items():
    globals()['t_' + name.upper()] = symbol
    tokens.append(name.upper())

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

