from lex import lex
from literals import *
from comments import *
from keywords import *
from identifiers import *
from tokens import *

"""
Several comments in this repository originate from the C++ Working Draft N4860
"""

"""
5.2 Phases of translation

3   The source file is decomposed into preprocessing tokens (5.4) and sequences of white-space characters
(including comments). A source file shall not end in a partial preprocessing token or in a partial
comment.7 Each comment is replaced by one space character. New-line characters are retained.
Whether each nonempty sequence of white-space characters other than new-line is retained or replaced
by one space character is unspecified. The process of dividing a source file’s characters into preprocessing
tokens is context-dependent. [Example: See the handling of < within a #include preprocessing directive.
— end example]
"""



with open('test.cpp', encoding='utf8') as f:
    input = f.read()

lexer = lex(debug=False)
lexer.input(input)

for token in lexer:
    print(token)