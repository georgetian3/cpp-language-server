"""
5.3 Character sets

The basic source character set consists of 96 characters: the space character, the control characters representing horizontal tab, vertical tab, form feed, and new-line, plus the following 91 graphical characters:
a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
0 1 2 3 4 5 6 7 8 9
_ { } [ ] # ( ) < > % : ; . ? * + - / ^ & | ~ ! = , \ " ’
"""

basic_source_character_set = set(
    ' \t\v\f\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}[]#()<>%:;.?*+-/^&|~!=,\\"\''
)

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
1   There are five kinds of tokens: identifiers, keywords, literals, operators, and other separators. Blanks, horizontal and vertical tabs, newlines, formfeeds, and comments (collectively, "white space"), as described below, are ignored except as they serve to separate tokens. [Note: Some white space is required to separate otherwise adjacent identifiers, keywords, numeric literals, and alternative tokens containing alphabetic characters. — end note]
"""






"""
5.12 Operators and punctuators
1   The lexical representation of C++ programs includes a number of preprocessing tokens that are used in the syntax of the preprocessor or are converted into tokens for operators and punctuators:

Each operator-or-punctuator is converted to a single token in translation phase 7 (5.2).
"""

preprocessing_operators = ['#', '##', '%:', '%:%:']
operator_or_punctuators = [
    '{', '}', '[', ']', '(', ')', '<:', ':>', '<%', '%>', ';', ':', '...', '?', '::', '.', '.*', '->', '->*', '~', '!', '+', '-', '*', '/', '%', '^', '&', '|', '=', '+=', '-=', '*=', '/=', '%=', '^=', '&=', '|=', '==', '!=', '<', '>', '<=', '>=', '<=>', '&&', '||', '<<', '>>', '<<=', '>>=', '++', '--', ',', 'and', 'or', 'xor', 'not', 'bitand', 'bitor', 'compl', 'and_eq', 'or_eq', 'xor_eq', 'not_eq'
]

if __name__ == '__main__':
    print(basic_source_character_set)
    for char in basic_source_character_set:
        print(ord(char))