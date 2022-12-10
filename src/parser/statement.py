from .base import p_empty

"""
8 Statements
"""

# 8.1 Preamble
def p_statement(p):
    ''' statement : labeled_statement
                  | expression_statement
                  | compound_statement
                  | selection_statement
                  | iteration_statement
                  | jump_statement
                  | declaration_statement
                  | try_block
                  | attribute_specifier_seq expression_statement
                  | attribute_specifier_seq compound_statement
                  | attribute_specifier_seq selection_statement
                  | attribute_specifier_seq iteration_statement
                  | attribute_specifier_seq jump_statement
                  | attribute_specifier_seq try_block '''

def p_init_statement(p):
    ''' init_statement : expression_statement
                       | simple_declaration '''

def p_condition(p):
    ''' condition : expression
                  | decl_specifier_seq declarator brace_or_equal_initializer
                  | attribute_specifier_seq decl_specifier_seq declarator brace_or_equal_initializer '''

# 8.3 Expression statement
def p_expression_statement(p):
    ''' expression_statement : expression
                             | empty '''