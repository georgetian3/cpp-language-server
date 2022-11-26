import lex
from lex import TOKEN
tokens = ('BINART_LITERAL','OCT_LITERAL','DEC_LITERAL','HEX_LITERAL','INTEGER_LITERAL')
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
binary_digit = r"(['01])"
octal_digit = r"([0-7'])"
nonzero_digit = r"([1-9'])"
digit = r"([0-9'])"
hex_pre = r'(0x|0X)'
bin_pre = r'(0b|0B)'
oct_pre = r'(0)'
hex_digit = r'([0-9a-fA-F])'
binary_literal = r'('+ bin_pre + binary_digit + r'+)'
oct_literal = r'('+oct_pre + octal_digit +r'+)'
dec_literal = r'('+nonzero_digit+digit+r'*)'
hex_literal = r'('+hex_pre+hex_digit+r'*)'
unsigned_suffix = r'([uU])'
long_suffix = r'([lL])'
long_long_suffix = r'(ll|LL)'
integer_suffix = r'([uU]|[lL]|ll|LL|[uU][lL]|[lL][uU]|[uU]ll|ll[uU]|[uU]LL|LL[uU])?' 
integer_literal = r'((' + binary_literal + '|' +oct_literal + '|'+dec_literal+'|'+hex_literal+')'+integer_suffix+')' 
@TOKEN(integer_literal)
def t_INTEGER_LITERAL(t):
    print(t.value)
    t.value = t.value.replace('u','')
    t.value = t.value.replace('U','')
    t.value = t.value.replace('L','')
    t.value = t.value.replace('l','')
    t.value = t.value.replace("'",'')
    if t.value == '0':
        return 0
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
if __name__ == '__main__':
    l=lex.lex()
    input = "0b10'11ul+110'1lu+011ull+0X11llu"
    l.input(input)
    for tok in l:
        print(tok)