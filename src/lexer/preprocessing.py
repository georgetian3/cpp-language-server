from .characters import basic_source_character
from myply.lex import TOKEN
"""
5.4 Proprocessing tokens
"""

import re

h_char = r'((?!\n|\>)%s)' % basic_source_character
q_char = r'((?!\n|\")%s)' % basic_source_character

h_char_sequence = r'(%s+)' % h_char
q_char_sequence = r'(%s+)' % q_char


system_include = r'(\#include\s*\<%s\>)' % h_char_sequence
local_include = r'(\#include\s*\"%s\")' % q_char_sequence

print(system_include)

include = r'(%s|%s)' % (system_include, local_include)

@TOKEN(include)
def t_INCLUDE(t):
    return t