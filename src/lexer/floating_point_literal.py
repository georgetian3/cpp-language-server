from .digits import digit_sequence, hexadecimal_digit_sequence
from .integer_literal import hexadecimal_prefix

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