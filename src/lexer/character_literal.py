from .characters import basic_source_character, universal_character_name
from .integer_literal import octal_digit, hexadecimal_digit
import re

encoding_prefix = r'[u8|u|U|L]'

simple_escape_sequence = r'[\\\'|\\"|\\?|\\\\|\\a|\\b|\\f|\\n|\\r|\\t|\\v]'
octal_escape_sequence = r'(\\%s{1-3})' % octal_digit
hexdecimal_escape_sequence = r'(\\x%s+)' % hexadecimal_digit
escape_sequence = r'[%s|%s|%s]' % (simple_escape_sequence, octal_escape_sequence, hexdecimal_escape_sequence)

c_char = r"[(?!['\\\n]|%s|%s]" % (basic_source_character, escape_sequence, universal_character_name)
c_char_sequence = r'(%s+)' % c_char
character_literal = r"(%s?'%s')" % c_char_sequence