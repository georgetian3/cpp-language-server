from .base import p_empty, Node

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


'''
;abeled_statement:
    attribute_specifier_seqopt identifier : statement
    attribute_specifier_seqopt case constant_expression : statement
    attribute_specifier_seqopt default : statement
'''

def p_abeled_statement(p):
    '''
        abeled_statement : identifier ':' statement
                         | attribute_specifier_seq identifier ':' statement
                         | t_CASE constant_expression ':' statement
                         | attribute_specifier_seq t_CASE constant_expression ':' statement
                         | t_DEFAULT ':' statement
                         | attribute_specifier_seq t_DEFAULT ':' statement
    '''


# 8.3 Expression statement
def p_expression_statement(p):
    ''' expression_statement : expression
                             | empty '''
    p[0] = Node('expression_statement', '', [p[1]])

'''
compound_statement:
    '{' statement_seqopt '}'
statement_seq:
    statement
    statement_seq statement
'''
def p_compound_statement(p):
    '''
        compound_statement : '{' '}'
                           | '{' statement_seq '}'
    '''
def p_statement_seq(p):
    '''
        statement_seq : statement
                      | statement_seq statement
    '''

'''
selection_statement:
    if constexpropt ( init_statementopt condition ) statement
    if constexpropt ( init_statementopt condition ) statement else statement
    switch ( init_statementopt condition ) statement
'''
def p_selection_statement(p):
    '''
        selection_statement : t_IF '(' condition ')' statement
                            | t_IF constexpr '(' condition ')' statement
                            | t_IF '(' init_statement condition ')' statement
                            | t_IF constexpr '(' init_statement condition ')' statement
                            | t_IF '(' condition ')' statement t_ELSE statement
                            | t_IF constexpr '(' condition ')' statement t_ELSE statement
                            | t_IF '(' init_statement condition ')' statement t_ELSE statement
                            | t_IF constexpr '(' init_statement condition ')' statement t_ELSE statement
                            | t_SWITCH '(' condition ')' statement
                            | t_SWITCH '('  init_statement condition ')' statement
    '''

'''
iteration_statement:
    while ( condition ) statement
    do statement while ( expression ) ;
    for ( init_statement conditionopt ; expressionopt ) statement
    for ( init_statementopt for_range_declaration : for_range_initializer ) statement
for_range_declaration:
    attribute_specifier_seqopt decl_specifier_seq declarator
    attribute_specifier_seqopt decl_specifier_seq ref_qualifieropt [ identifier_list ]
for_range_initializer:
    expr_or_braced_init_list
'''

def p_iteration_statement(p):
    '''
        iteration_statement : t_WHILE '(' condition ')' statement
                            | t_DO statement t_WHILE '(' expression ')' ';'
                            | t_FOR '(' init_statement ';' ) statement
                            | t_FOR '(' init_statement condition ';' ) statement
                            | t_FOR '(' init_statement ';' expression ) statement
                            | t_FOR '(' init_statement condition ';' expression ) statement
                            | t_FOR '(' for_range_declaration ':' for_range_initializer ) statement
                            | t_FOR '(' init_statement for_range_declaration ':' for_range_initializer ) statement
    '''

def p_for_range_declaration(p):
    '''
        for_range_declaration : decl_specifier_seq declarator
                              | attribute_specifier_seq decl_specifier_seq declarator
                              | decl_specifier_seq '[' identifier_list ']'
                              | attribute_specifier_seq decl_specifier_seq '[' identifier_list ']'
                              | decl_specifier_seq ref_qualifier '[' identifier_list ']'
                              | attribute_specifier_seq decl_specifier_seq ref_qualifier '[' identifier_list ']'
    '''
def p_for_range_initializer(p):
    '''
        for_range_initializer : expr_or_braced_init_list
    '''
'''
jump_statement:
    break ;
    continue ;
    return expr_or_braced_init_listopt ;
    coroutine_return_statement
    goto identifier ;
'''

def p_jump_statement(p):
    '''
        jump_statement : t_BREAK ';'
                       | t_CONTINUE ';'
                       | t_RETURN ';'
                       | t_RETURN expr_or_braced_init_list ';'
                       | coroutine_return_statement
                       | t_GOTO identifier ';'
    '''

'''
coroutine_return_statement:
    co_return expr_or_braced_init_listopt ;
'''

def p_coroutine_return_statement(p):
    '''
        coroutine_return_statement : co_return expr_or_braced_init_list ';'
                                   | ';'
    '''

'''
declaration_statement:
    block_declaration
'''

def p_declaration_statement(p):
    '''
        declaration_statement : block_declaration
    '''

