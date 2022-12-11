
from .integer_literal import octal_digit, hexadecimal_digit


encoding_prefix = r'[u8|u|U|L]'
simple_escape_sequence = r'[\\\'|\\"|\\?|\\\\|\\a|\\b|\\f|\\n|\\r|\\t|\\v]'
octal_escape_sequence = r'(\\%s{1-3})' % octal_digit
hexdecimal_escape_sequence = r'(\\x%s+)' % hexadecimal_digit

escape_sequence = r'[%s|%s|%s]' % (simple_escape_sequence, octal_escape_sequence, hexdecimal_escape_sequence)

c_char = ''

hex_quad = r"("+hex_digit+hex_digit+hex_digit+hex_digit+r")"
universal_character_name = r"((\\u"+hex_quad+r")|(\\U"+hex_quad+hex_quad+r"))"
c_char = r"(([ \t\v\fa-zA-Z0-9_\{\}\[\]\#\(\)<>%:;\.\?\*\+\-/\^&\|~!=,\"])|("+escape_sequence+r")|("+universal_character_name+r"))"


c_char_sequence = r'(%s+)' % c_char

character_literal = r"(%s?'%s')" % c_char_sequence