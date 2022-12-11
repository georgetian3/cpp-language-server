# 5.3 Character sets

from .digits import hexadecimal_digit

basic_source_character = r'[\u0020-\u003f|\u0041-\u005f|\u0061-\u007e|[\t\n\v\f]]'
hex_quad = r'(%s{4})' % hexadecimal_digit
universal_character_name = r'(\\[u|U]%s{1,2})' % hex_quad