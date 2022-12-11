"""
5.3 Character sets

The basic source character set consists of 96 characters: the space character, the control characters representing horizontal tab, vertical tab, form feed, and new-line, plus the following 91 graphical characters:
a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
0 1 2 3 4 5 6 7 8 9
_ { } [ ] # ( ) < > % : ; . ? * + - / ^ & | ~ ! = , \ " ’
"""

from .digits import hexadecimal_digit

basic_source_character = r'[\u0020-\u003f|\u0041-\u005f|\u0061-\u007e]'
hex_quad = r'(%s{4})' % hexadecimal_digit
universal_character_name = r'(\\[u|U]%s{1,2})' % hex_quad