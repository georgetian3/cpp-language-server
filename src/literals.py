from ply.lex import TOKEN
import ply.lex as lex
tokens = ('BINART_LITERAL','OCT_LITERAL','DEC_LITERAL','HEX_LITERAL','INTEGER_LITERAL','CHARACTER_LITERAL','STRING_LITERAL')
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



"""
5.13.2 Integer literals

integer-literal :
    binary-literal integer-suffix(opt)
    octal-literal integer-suffix(opt)
    decimal-literal integer-suffix(opt)
    hexadecimal-literal integer-suffix(opt)
binary-literal :
    0b binary-digit
    0B binary-digit
    binary-literal ’(opt) binary-digit
octal-literal :
    0
    octal-literal ’(opt) octal-digit
decimal-literal :
    nonzero-digit
    decimal-literal ’(opt) digit
hexadecimal-literal :
    hexadecimal-prefix hexadecimal-digit-sequence
binary-digit : one of
    0 1
octal-digit : one of
    0 1 2 3 4 5 6 7
nonzero-digit : one of
    1 2 3 4 5 6 7 8 9
hexadecimal-prefix : one of
    0x 0X
hexadecimal-digit-sequence :
    hexadecimal-digit
    hexadecimal-digit-sequence ’(opt) hexadecimal-digit
hexadecimal-digit : one of
    0 1 2 3 4 5 6 7 8 9
    a b c d e f
    A B C D E F
integer-suffix :
    unsigned-suffix long-suffix(opt)
    unsigned-suffix long-long-suffix(opt)
    long-suffix unsigned-suffix(opt)
    long-long-suffix unsigned-suffix(opt)
unsigned-suffix : one of
    u U
long-suffix : one of
    l L
long-long-suffix : one of
    ll LL
"""
binary_digit = r"([01]'?)"
octal_digit = r"([0-7]'?)"
nonzero_digit = r"([1-9]'?)"
digit = r"([0-9]'?)"
hex_pre = r'(0x|0X)'
bin_pre = r'(0b|0B)'
oct_pre = r'(0)'
hex_digit = r"([0-9a-fA-F]'?)"
binary_literal = r'('+ bin_pre + binary_digit + r'+)'
oct_literal = r'('+oct_pre + octal_digit +r'+)'
dec_literal = r'('+digit+r'+)'
hex_literal = r'('+hex_pre+hex_digit+r'*)'
unsigned_suffix = r'([uU])'
long_suffix = r'([lL])'
long_long_suffix = r'(ll|LL)'
integer_suffix = r'([uU]|[lL]|ll|LL|[uU][lL]|[lL][uU]|[uU]ll|ll[uU]|[uU]LL|LL[uU])?' 
integer_literal = r'((' + binary_literal + '|' +hex_literal + '|'+oct_literal+'|'+dec_literal+')'+integer_suffix+')' 
@TOKEN(integer_literal)
def t_INTEGER_LITERAL(t):
    t.value = t.value.replace('u','')
    t.value = t.value.replace('U','')
    t.value = t.value.replace('L','')
    t.value = t.value.replace('l','')
    t.value = t.value.replace("'",'')
    if t.value == '0':
        t.value = 0
        return t
    if t.value[0]=='0':
        if t.value[1]=='b'or t.value[1]=='B':
            t.value = int(t.value,2)
        elif t.value[1]=='x' or t.value[1]=='X':
            t.value = int(t.value,16)
        else:
            t.value = int(t.value,8)
    else:
        t.value = int(t.value)
    return t


@TOKEN(binary_literal)
def t_BINART_LITERAL(t):
    t.value = int(t.value,2)
    return t
@TOKEN(oct_literal)
def t_OCT_LITERAL(t):
    t.value = int(t.value,8)
    return t
@TOKEN(hex_literal)
def t_HEX_LITERAL(t):
    t.value = int(t.value,16)
    return t
@TOKEN(dec_literal)
def t_DEC_LITERAL(t):
    t.value = int(t.value)
    return t

def t_error(t):
    t.lexer.skip(1)
#def t_LITERAL




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

hexdecimal_escape_sequence = r"((\\x)"+r"("+hex_digit+r"+))"
octal_escape_sequence = r"(("+r"\\"+octal_digit+r")|("+r"\\"+octal_digit+octal_digit+r")|("+r"\\"+octal_digit+octal_digit+octal_digit+r"))"
simple_escape_sequence = r"([\'\"\?\\\a\b\f\n\r\t\v])"
escape_sequence = r"(("+simple_escape_sequence+r")|("+octal_escape_sequence+r")|("+hexdecimal_escape_sequence+r"))"
hex_quad = r"("+hex_digit+hex_digit+hex_digit+hex_digit+r")"
universal_character_name = r"((\\u"+hex_quad+r")|(\\U"+hex_quad+hex_quad+r"))"
c_char = r"(([ \t\v\fa-zA-Z0-9_\{\}\[\]\#\(\)<>%:;\.\?\*\+\-/\^&\|~!=,\"])|("+escape_sequence+r")|("+universal_character_name+r"))"
c_char_sequence=r"("+c_char+r"+)"
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
s_char = r"([ \t\v\fa-zA-Z0-9_\{\}\[\]\#\(\)<>%:;\.\?\*\+\-/\^&\|~!=,\']|("+escape_sequence+r")|("+universal_character_name+r"))"
s_char_sequence = r"("+s_char+r"+)"
t_STRING_LITERAL = r"((("+encoding_prefix+r"?)\"("+s_char_sequence+r"?)\")|(("+encoding_prefix+r"?)R"+raw_string+r"))"


if __name__ == '__main__':
    l=lex.lex()
    input = "b"
    l.input(input)
    for tok in l:
        print(tok)