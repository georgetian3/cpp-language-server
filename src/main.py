import lex



t_ignore_COMMENT = r'[//.*|/*'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex.lex()