"""
2.7 Comments

The characters /* start a comment, which terminates with the characters */. These comments do not nest. The characters // start a comment, which terminates immediately before the next new-line character. If there is a form-feed or a vertical-tab character in such a comment, only white-space characters shall appear between it and the new-line that terminates the comment; no diagnostic is required. [ Note: The comment characters //, /*, and */ have no special meaning within a // comment and are treated just like other characters. Similarly, the comment characters // and /* have no special meaning within a /* comment.
— end note ]
"""


def whitespace(t):
    r'\s+'
    t.lexer.lineno += t.value.count('\n')
    return t

def t_COMMENT_SINGLE_LINE(t):
    r'(//.*?(\n|$))'
    t.type = 'WS'
    return t

def t_COMMENT_MULTI_LINE(t):
    r'(/\*(.|\n)*?\*/)'
    ncr = t.value.count("\n")
    t.lexer.lineno += ncr
    # replace with one space or a number of '\n'
    t.type = 'WS'
    #t.value = '\n' * ncr if ncr else ' '
    return t