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
from .character_literal import character_literal

@TOKEN(integer_literal)
def t_INTEGER_LITERAL(t):
    return t

@TOKEN(floating_point_literal)
def t_FLOATING_POINT_LITERAL(t):
    return t

@TOKEN(character_literal)
def t_CHARACTER_LITERAL(t):
    return t




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