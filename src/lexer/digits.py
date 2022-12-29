digit = r'[0-9]'
nonzero_digit = r'[1-9]'
digit_sequence = r'(%s(\'?%s)*)' % (digit, digit)
binary_digit = r'[01]'
octal_digit = r'[0-7]'
hexadecimal_digit = r'[0-9a-fA-F]'
hexadecimal_digit_sequence = r'(%s(\'?%s)*)' % (hexadecimal_digit, hexadecimal_digit)
