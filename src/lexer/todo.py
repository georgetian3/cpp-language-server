from ply.lex import TOKEN

h_char = r'[^\n>]'
q_char = r'[^\n\"]'

q_char_sequence = r'(q_char+)'

h_char_sequence = r'(h_char+)'


@TOKEN(q_char_sequence)
def t_Q_CHAR_SEQUENCE(t):
    return t


@TOKEN(h_char_sequence)
def t_H_CHAR_SEQUENCE(t):
    return t