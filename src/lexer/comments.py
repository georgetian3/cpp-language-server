from ply.lex import TOKEN

"""
2.7 Comments

The characters /* start a comment, which terminates with the characters */. These comments do not nest. The characters // start a comment, which terminates immediately before the next new-line character. If there is a form-feed or a vertical-tab character in such a comment, only white-space characters shall appear between it and the new-line that terminates the comment; no diagnostic is required. [ Note: The comment characters //, /*, and */ have no special meaning within a // comment and are treated just like other characters. Similarly, the comment characters // and /* have no special meaning within a /* comment.
— end note ]
"""




single_line_comment = r'(//.*?(\n|$))'
multi_line_comment = r'(/\*(.|\n)*?\*/)'
comment = r'(%s|%s)' % (single_line_comment, multi_line_comment)

@TOKEN(comment)
def t_COMMENT(t):
    t.lexer.lineno += t.value.count("\n")
    return t

def t_WHITESPACE(t):
    r'\s+'
    t.lexer.lineno += t.value.count('\n')
    #return t