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
5.10 Identifiers

identifier :
    identifier-nondigit
    identifier identifier-nondigit
    identifier digit
identifier-nondigit :
    nondigit
    universal-character-name
nondigit : one of
    a b c d e f g h i j k l m
    n o p q r s t u v w x y z
    A B C D E F G H I J K L M
    N O P Q R S T U V W X Y Z _
digit : one of
    0 1 2 3 4 5 6 7 8 9


1   An identifier is an arbitrarily long sequence of letters and digits. Each universal-character-name in an identifier shall designate a character whose encoding in ISO/IEC 10646 falls into one of the ranges specified in `names_allowed`. The initial element shall not be a universal-character-name designating a character whose encoding falls into one of the ranges specified in Table `names_disallowed`. Upper- and lower-case letters are different. All characters are significant.
"""

names_allowed = [
    '\u00A8', '\u00AA', '\u00AD', '\u00AF', '\u00B2-\u00B5', '\u00B7-\u00BA', '\u00BC-\u00BE', '\u00C0-\u00D6', '\u00D8-\u00F6', '\u00F8-\u00FF', '\u0100-\u167F', '\u1681-\u180D', '\u180F-\u1FFF', '\u200B-\u200D', '\u202A-\u202E', '\u203F-\u2040', '\u2054', '\u2060-\u206F', '\u2070-\u218F', '\u2460-\u24FF', '\u2776-\u2793', '\u2C00-\u2DFF', '\u2E80-\u2FFF', '\u3004-\u3007', '\u3021-\u302F', '\u3031-\uD7FF', '\uF900-\uFD3D', '\uFD40-\uFDCF', '\uFDF0-\uFE44', '\uFE47-\uFFFD', '\u10000-\u1FFFD', '\u20000-\u2FFFD', '\u30000-\u3FFFD', '\u40000-\u4FFFD', '\u50000-\u5FFFD', '\u60000-\u6FFFD', '\u70000-\u7FFFD', '\u80000-\u8FFFD', '\u90000-\u9FFFD', '\uA0000-\uAFFFD', '\uB0000-\uBFFFD', '\uC0000-\uCFFFD', '\uD0000-\uDFFFD', '\uE0000-\uEFFFD'
]

names_disallowed = ['\u0300-\u036F', '\u1DC0-\u1DFF', '\u20D0-\u20FF', '\uFE20-\uFE2F']


"""
5.11 Keywords

1   The identifiers shown in Table `keywords` are reserved for use as keywords (that is, they are unconditionally treated as keywords in phase 7) except in an attribute-token (9.12.1). [Note: The register keyword is unused but is reserved for future use. — end note]
"""

keywords = [
    'alignas', 'alignof', 'asm', 'auto', 'bool', 'break', 'case', 'catch', 'char', 'char16_t', 'char32_t', 'char8_t', 'class', 'co_await', 'co_return', 'co_yield', 'concept', 'const', 'const_cast', 'consteval', 'constexpr', 'constinit', 'continue', 'decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast', 'else', 'enum', 'explicit', 'export', 'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline', 'int', 'long', 'mutable', 'namespace', 'new', 'noexcept', 'nullptr', 'operator', 'private', 'protected', 'public', 'register', 'reinterpret_cast', 'requires', 'return', 'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch', 'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while'
]


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