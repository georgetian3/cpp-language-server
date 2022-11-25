from constants import basic_source_character_set
import re


"""
2.2 Phases of translation 

1. Physical source file characters are mapped, in an implementation-defined manner, to the basic source character set (introducing new-line characters for end-of-line indicators) if necessary. The set of physical source file characters accepted is implementation-defined. Any source file character not in the basic source character set (2.3) is replaced by the universal-character-name that designates that character. (An implementation may use any internal encoding, so long as an actual extended character encountered in the source file, and the same extended character expressed in the source file as a universal-character-name (i.e., using the \\uXXXX notation), are handled equivalently except where this replacement is reverted in a raw string literal.)
"""

def replace_with_basic_source_character_set(input: str):
    output = []
    for char in input:
        if char not in basic_source_character_set:
            output += '\\u'
            output += str(hex(ord(char))[2:].rjust(4, '0'))
        else:
            output += char
    return output

if __name__ == '__main__':
    input = '测试 + f'
    output = replace_with_basic_source_character_set(input)
    print(output)