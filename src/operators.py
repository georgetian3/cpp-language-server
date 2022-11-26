"""
5.12 Operators and punctuators
1   The lexical representation of C++ programs includes a number of preprocessing tokens that are used in the syntax of the preprocessor or are converted into tokens for operators and punctuators:

Each operator-or-punctuator is converted to a single token in translation phase 7 (5.2).
"""

preprocessing_operators = ['#', '##', '%:', '%:%:']
operator_or_punctuators = [
    '{', '}', '[', ']', '(', ')', '<:', ':>', '<%', '%>', ';', ':', '...', '?', '::', '.', '.*', '->', '->*', '~', '!', '+', '-', '*', '/', '%', '^', '&', '|', '=', '+=', '-=', '*=', '/=', '%=', '^=', '&=', '|=', '==', '!=', '<', '>', '<=', '>=', '<=>', '&&', '||', '<<', '>>', '<<=', '>>=', '++', '--', ',', 'and', 'or', 'xor', 'not', 'bitand', 'bitor', 'compl', 'and_eq', 'or_eq', 'xor_eq', 'not_eq'
]

