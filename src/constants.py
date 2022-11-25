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
5.11 Keywords

1 The identifiers shown in Table 5 are reserved for use as keywords (that is, they are unconditionally treated as keywords in phase 7) except in an attribute-token (9.12.1). [Note: The register keyword is unused but is reserved for future use. — end note]
"""



keywords = [
    'alignas', 'alignof', 'asm', 'auto', 'bool', 'break', 'case', 'catch', 'char', 'char16_t', 'char32_t', 'char8_t', 'class', 'co_await', 'co_return', 'co_yield', 'concept', 'const', 'const_cast', 'consteval', 'constexpr', 'constinit', 'continue', 'decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast', 'else', 'enum', 'explicit', 'export', 'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline', 'int', 'long', 'mutable', 'namespace', 'new', 'noexcept', 'nullptr', 'operator', 'private', 'protected', 'public', 'register', 'reinterpret_cast', 'requires', 'return', 'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch', 'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while'
]

"""
5.12 Operators and punctuators
1 The lexical representation of C++ programs includes a number of preprocessing tokens that are used in the syntax of the preprocessor or are converted into tokens for operators and punctuators:

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