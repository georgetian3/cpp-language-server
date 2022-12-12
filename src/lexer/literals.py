from ply.lex import TOKEN
import ply.lex as lex

from .characters import basic_source_character, universal_character_name
from .digits import digit, binary_digit, octal_digit, hexadecimal_digit, hexadecimal_digit_sequence, nonzero_digit, digit_sequence

#############################################################################################################
# 5.13.2 Integer literals

hexadecimal_prefix = r'[0x|0X]'

unsigned_suffix = r'[uU]'
long_suffix = r'[lL]'
long_long_suffix = r'[ll|LL]'

integer_suffix = r'(%s%s?|%s%s?|%s%s?|%s%s?)' % (
    unsigned_suffix, long_suffix,
    unsigned_suffix, long_long_suffix,
    long_suffix, unsigned_suffix,
    long_long_suffix, unsigned_suffix
)

binary_literal = r'(0[b|B](\'?%s)+)' % binary_digit
octal_literal = r'(0(\'?%s)+)' % octal_digit
decimal_literal = r'(%s(\'?%s)+)' % (nonzero_digit, digit)
hexadecimal_literal = r'(%s%s)' % (hexadecimal_prefix, hexadecimal_digit_sequence)

integer_literal = r'(%s%s?|%s%s?|%s%s?|%s%s?)' % (
    binary_literal, integer_suffix,
    octal_literal, integer_suffix,
    decimal_literal, integer_suffix,
    hexadecimal_literal, integer_suffix,
)

integer_literal = r'[\+-]?[0-9]+'


#############################################################################################################
# 5.13.3 Character literals

encoding_prefix = r'[u8|u|U|L]'

simple_escape_sequence = r'[\\\'|\\\"|\\?|\\\\|\\a|\\b|\\f|\\n|\\r|\\t|\\v]'
octal_escape_sequence = r'(\\%s{1-3})' % octal_digit
hexdecimal_escape_sequence = r'(\\x%s+)' % hexadecimal_digit
escape_sequence = r'[%s|%s|%s]' % (simple_escape_sequence, octal_escape_sequence, hexdecimal_escape_sequence)

c_char = r'[(?!\'|\\|\n)%s|%s|%s]' % (basic_source_character, escape_sequence, universal_character_name)
c_char_sequence = r'(%s+)' % c_char
character_literal = r'(%s?\'%s\')' % (encoding_prefix, c_char_sequence)
character_literal = r'\'[^\']\''

#############################################################################################################
# 5.13.4 Floating-point literals

floating_point_suffix = r'[flFL]'
sign = r'[\+-]'
exponent_part = r'([e|E]%s?%s)' % (sign, digit_sequence)
binary_exponent_part = r'([p|P]%s?%s)' % (sign, digit_sequence)


fractional_constant = r'[%s?\.%s|%s\.]' % (digit_sequence, digit_sequence, digit_sequence)
hexadecimal_fractional_constant = r'[%s?\.%s|%s\.]' % (
    hexadecimal_digit_sequence, hexadecimal_digit_sequence, hexadecimal_digit_sequence
)

decimal_floating_point_literal = r'[%s%s?%s?|%s%s%s?]' % (
    fractional_constant, exponent_part, floating_point_suffix,
    digit_sequence, exponent_part, floating_point_suffix
)

hexadecimal_floating_point_literal = r'(%s[%s%s?%s?|%s%s%s?])' % (
    hexadecimal_prefix, fractional_constant, exponent_part, floating_point_suffix,
    digit_sequence, exponent_part, floating_point_suffix
)

floating_point_literal = r'[%s|%s]' % (
    decimal_floating_point_literal,
    hexadecimal_floating_point_literal
)

floating_point_literal = r'[%s\.%s?|%s?\.%s]' % ('[0-9]+', '[0-9]+', '[0-9]+', '[0-9]+') # TODO: not to spec yet

floating_point_literal = r'[\+-]?[0-9]+\.[0-9]+'

#############################################################################################################
# 5.13.5 String literals

s_char = r'[(?!\"|\\|\n)%s|%s|%s]' % (basic_source_character, escape_sequence, universal_character_name)
s_char_sequence = r'(%s+)' % s_char
d_char = r'[(?! |\(|\)|\\|\t|\v|\f|\n)%s|%s|%s]' % (basic_source_character, escape_sequence, universal_character_name)
d_char_sequence = r'(%s+)' % d_char

r_char = r'[(?!\)|%s?|\")%s|%s|%s]' % (d_char_sequence, basic_source_character, escape_sequence, universal_character_name)
r_char_sequence = r'(%s+)' % r_char

raw_string = r'%s?\(%s?\)%s?' % (d_char_sequence, r_char_sequence, d_char_sequence)

string_literal = r'(%s?[\"%s?\"|R%s])' % (encoding_prefix, s_char_sequence, raw_string)

string_literal = r'\".*?\"' # TODO: not to spec yet

#############################################################################################################
# 5.13.6 Boolean literals

boolean_literal = r'(true|false)'

#############################################################################################################
# 5.13.7 Pointer literals
pointer_literal = r'(nullptr)'

#############################################################################################################


literal = '[%s|%s|%s|%s|%s|%s]' % (
    floating_point_literal,
    integer_literal,
    character_literal,
    string_literal,
    boolean_literal,
    pointer_literal,
)
""" 
@TOKEN(integer_literal)
def t_INTEGER_LITERAL(t):
    return t
@TOKEN(character_literal)
def t_CHARACTER_LITERAL(t):
    return t """
@TOKEN(floating_point_literal)
def t_FLOATING_POINT_LITERAL(t):
    return t
""" @TOKEN(string_literal)
def t_STRING_LITERAL(t):
    return t
@TOKEN(boolean_literal)
def t_BOOLEAN_LITERAL(t):
    return t
@TOKEN(pointer_literal)
def t_POINTER_LITERAL(t):
    return t """
@TOKEN(literal)
def t_LITERAL(t):
    return t



if __name__ == '__main__':
    l=lex.lex()
    input = '''
            "u8"absid""
            '''
    l.input(input)
    for tok in l:
        print(tok)