from .digits import digit

binary_digit = r'[01]'
octal_digit = r'[0-7]'
nonzero_digit = r'[1-9]'

hexadecimal_prefix = r'[0x|0X]'
hexadecimal_digit = r'[0-9a-fA-F]'
hexadecimal_digit_sequence = r"(%s('?%s)*)" % hexadecimal_digit

unsigned_suffix = r'[uU]'
long_suffix = r'[lL]'
long_long_suffix = r'[ll|LL]'

integer_suffix = r'(%s%s?|%s%s?|%s%s?|%s%s?)' % (
    unsigned_suffix, long_suffix,
    unsigned_suffix, long_long_suffix,
    long_suffix, unsigned_suffix,
    long_long_suffix, unsigned_suffix
)

binary_literal = r"(0[b|B]('?%s)+)" % binary_digit
octal_literal = r"(0('?%s)+)" % octal_digit
decimal_literal = r"(%s('?%s)+)" % (nonzero_digit, digit)
hexadecimal_literal = r'(%s%s)' % (hexadecimal_prefix, hexadecimal_digit_sequence)

integer_literal = r'(%s%s?|%s%s?|%s%s?|%s%s?)' % (
    binary_literal, integer_suffix,
    octal_literal, integer_suffix,
    decimal_literal, integer_suffix,
    hexadecimal_literal, integer_suffix,
)

if __name__ == '__main__':
    import re
    s = "013"
    print(re.match(octal_literal, s))