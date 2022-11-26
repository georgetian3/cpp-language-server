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


# currently not standard compliant, TODO: change later
t_IDENTIFIER = r'[A-Za-z_][A-Za-z0-9_]*'