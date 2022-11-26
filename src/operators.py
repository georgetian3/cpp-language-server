"""
5.12 Operators and punctuators
1   The lexical representation of C++ programs includes a number of preprocessing tokens that are used in the syntax of the preprocessor or are converted into tokens for operators and punctuators:

Each operator-or-punctuator is converted to a single token in translation phase 7 (5.2).
"""

preprocessing_operators = ['#', '##', '%:', '%:%:']
operator_or_punctuators = [
    '{', '}', '[', ']', '(', ')', '<:', ':>', '<%', '%>', ';', ':', '...', '?', '::', '.', '.*', '->', '->*', '~', '!', '+', '-', '*', '/', '%', '^', '&', '|', '=', '+=', '-=', '*=', '/=', '%=', '^=', '&=', '|=', '==', '!=', '<', '>', '<=', '>=', '<=>', '&&', '||', '<<', '>>', '<<=', '>>=', '++', '--', ',', 'and', 'or', 'xor', 'not', 'bitand', 'bitor', 'compl', 'and_eq', 'or_eq', 'xor_eq', 'not_eq'
]

__special_chars = set(['.', '+', '*', '?', '^', '$', '(', ')', '[', ']', '{', '}', '|', '\\'])

def escape_special_chars(s):
    output = []
    for char in s:
        if char in __special_chars:
            output += '\\' + char
        else:
            output += char
    return ''.join(output)



t_OPERATOR_OR_PUNCTUATOR = f"{'|'.join(escape_special_chars(x) for x in operator_or_punctuators)}"



if __name__ == '__main__':
    print(t_OPERATOR_OR_PUNCTUATOR)
    pass