from ply.lex import TOKEN
import ply.lex as lex
"""
5.13 Literals


5.13.1 Kinds of literals

1   There are several kinds of literals.
literal :
    integer-literal
    character-literal
    floating-point-literal
    string-literal
    boolean-literal
    pointer-literal
    user-defined-literal
"""
from .integer_literal import integer_literal
from .floating_point_literal import floating_point_literal

@TOKEN(integer_literal)
def t_INTEGER_LITERAL(t):
    return t

@TOKEN(floating_point_literal)
def t_FLOATING_POINT_LITERAL(t):
    return t




"""
5.13.3 Character literals

character-literal :
    encoding-prefixopt ’ c-char-sequence ’
encoding-prefix : one of
    u8 u U L
c-char-sequence :
    c-char
    c-char-sequence c-char
c-char :
    any member of the basic source character set except the single-quote ’, backslash \\, or new-line character
    escape-sequence
    universal-character-name
escape-sequence :
    simple-escape-sequence
    octal-escape-sequence
    hexadecimal-escape-sequence
simple-escape-sequence : one of
    \’ \" \? \\
    \a \b \f \n \r \t \v
octal-escape-sequence :
    \\ octal-digit
    \\ octal-digit octal-digit
    \\ octal-digit octal-digit octal-digit
hexadecimal-escape-sequence :
    \\x hexadecimal-digit
    hexadecimal-escape-sequence hexadecimal-digit
"""

hex_digit = r"([0-9a-fA-F]'?)"
octal_digit = r"([0-7]'?)"
hexdecimal_escape_sequence = r"((\\x)"+r"("+hex_digit+r"+))"
octal_escape_sequence = r"(("+r"\\"+octal_digit+r")|("+r"\\"+octal_digit+octal_digit+r")|("+r"\\"+octal_digit+octal_digit+octal_digit+r"))"
simple_escape_sequence = r"((\\\')|(\\\")|(\\\?)|(\\\\)|(\\a)|(\\b)|(\\f)|(\\n)|(\\r)|(\\t)|(\\v))"
escape_sequence = r"(("+simple_escape_sequence+r")|("+octal_escape_sequence+r")|("+hexdecimal_escape_sequence+r"))"
hex_quad = r"("+hex_digit+hex_digit+hex_digit+hex_digit+r")"
universal_character_name = r"((\\u"+hex_quad+r")|(\\U"+hex_quad+hex_quad+r"))"
c_char = r"(([ \t\v\fa-zA-Z0-9_\{\}\[\]\#\(\)<>%:;\.\?\*\+\-/\^&\|~!=,\"])|("+escape_sequence+r")|("+universal_character_name+r"))"
c_char_sequence=r"("+ c_char + r"+)"
encoding_prefix=r"((u8)|(u)|(U)|(L))"
t_CHARACTER_LITERAL=r"(("+encoding_prefix+r"?)\'"+c_char_sequence+r"\')"




"""
5.13.5 String literals [lex.string]
string-literal:
    encoding-prefixopt " s-char-sequenceopt "
    encoding-prefixopt R raw-string
s-char-sequence :
    s-char
    s-char-sequence s-char
s-char:
    any member of the basic source character set except the double-quote ", backslash \, or new-line character
    escape-sequence
    universal-character-name
raw-string:
    " d-char-sequenceopt ( r-char-sequenceopt ) d-char-sequenceopt "
r-char-sequence :
    r-char
    r-char-sequence r-char
r-char:
    any member of the source character set, except a right parenthesis ) followed by
    the initial d-char-sequence (which may be empty) followed by a double quote ".
d-char-sequence :
    d-char
    d-char-sequence d-char
d-char:
    any member of the basic source character set except:
    space, the left parenthesis (, the right parenthesis ), the backslash \, and the control characters
    representing horizontal tab, vertical tab, form feed, and newline.

"""

d_char = r"([a-zA-Z0-9_\{\}\[\]\#<>%:;\.\?\*\+\-/\^&\|~!=,\"\'])"
d_char_sequence = r"("+ d_char + r"+)"
r_char = r"([ \t\v\f\na-zA-Z0-9_\{\}\[\]\#\(<>%:;\.\?\*\+\-/\^&\|~!=,\"\'\\])"+ d_char_sequence + r"\""
r_char_sequence = r"("+ r_char + r"+)"
raw_string = r"(\"(" + d_char_sequence + r"?)\((" + r_char_sequence + r"?)\)(" + d_char_sequence + r"?)\")"
s_char = r"(([ \t\v\fa-zA-Z0-9_\{\}\[\]\#\(\)<>%:;\.\?\*\+\-/\^&\|~!=,\'])|("+escape_sequence+r")|("+universal_character_name+r"))"
s_char_sequence = r"("+s_char+r"+)"
t_STRING_LITERAL = r"((("+encoding_prefix+r"?)\"("+s_char_sequence+r"?)\")|(("+encoding_prefix+r"?)R"+raw_string+r"))"

if __name__ == '__main__':
    l=lex.lex()
    input = '''
            "u8"absid""
            '''
    l.input(input)
    for tok in l:
        print(tok)