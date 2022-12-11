from .myast import InternalNode, ExternalNode

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

    p[0] = ExternalNode('statement', p[1:])


def p_init_statement(p):
    ''' init_statement : expression_statement
                       | simple_declaration '''
    p[0] = ExternalNode('init_statement', p[1:])
def p_condition(p):
    ''' condition : expression
                  | decl_specifier_seq declarator brace_or_equal_initializer
                  | attribute_specifier_seq decl_specifier_seq declarator brace_or_equal_initializer '''
    p[0] = ExternalNode('condition', p[1:])


def p_labeled_statement(p):
    '''
        labeled_statement : IDENTIFIER ':' statement
                         | attribute_specifier_seq IDENTIFIER ':' statement
                         | CASE constant_expression ':' statement
                         | attribute_specifier_seq CASE constant_expression ':' statement
                         | DEFAULT ':' statement
                         | attribute_specifier_seq DEFAULT ':' statement
    '''
    p[0] = ExternalNode('labeled_statement', p[1:])


# 8.3 Expression statement
def p_expression_statement(p):
    ''' expression_statement : expression
                             | empty '''
    p[0] = ExternalNode('expression_statement', [p[1]])

def p_compound_statement(p):
    '''
        compound_statement : '{' '}'
                           | '{' statement_seq '}'
    '''
    p[0] = ExternalNode('compound_statement', p[1:])

def p_statement_seq(p):
    '''
        statement_seq : statement
                      | statement_seq statement
    '''
    p[0] = ExternalNode('statement_seq', p[1:])


def p_selection_statement(p):
    '''
        selection_statement : IF '(' condition ')' statement
                            | IF CONSTEXPR '(' condition ')' statement
                            | IF '(' init_statement condition ')' statement
                            | IF CONSTEXPR '(' init_statement condition ')' statement
                            | IF '(' condition ')' statement ELSE statement
                            | IF CONSTEXPR '(' condition ')' statement ELSE statement
                            | IF '(' init_statement condition ')' statement ELSE statement
                            | IF CONSTEXPR '(' init_statement condition ')' statement ELSE statement
                            | SWITCH '(' condition ')' statement
                            | SWITCH '('  init_statement condition ')' statement
    '''
    p[0] = ExternalNode('selection_statement', p[1:])

def p_iteration_statement(p):
    '''
        iteration_statement : WHILE '(' condition ')' statement
                            | DO statement WHILE '(' expression ')' ';'
                            | FOR '(' init_statement ';' ')' statement
                            | FOR '(' init_statement condition ';' ')' statement
                            | FOR '(' init_statement ';' expression ')' statement
                            | FOR '(' init_statement condition ';' expression ')' statement
                            | FOR '(' for_range_declaration ':' for_range_initializer ')' statement
                            | FOR '(' init_statement for_range_declaration ':' for_range_initializer ')' statement
    '''
    p[0] = ExternalNode('iteration_statement', p[1:])

def p_for_range_declaration(p):
    '''
        for_range_declaration : decl_specifier_seq declarator
                              | attribute_specifier_seq decl_specifier_seq declarator
                              | decl_specifier_seq '[' identifier_list ']'
                              | attribute_specifier_seq decl_specifier_seq '[' identifier_list ']'
                              | decl_specifier_seq ref_qualifier '[' identifier_list ']'
                              | attribute_specifier_seq decl_specifier_seq ref_qualifier '[' identifier_list ']'
    '''
    p[0] = ExternalNode('for_range_declaration', p[1:])

def p_for_range_initializer(p):
    '''
        for_range_initializer : expr_or_braced_init_list
    '''
    p[0] = ExternalNode('for_range_initializer', p[1:])

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
        jump_statement : BREAK ';'
                       | CONTINUE ';'
                       | RETURN ';'
                       | RETURN expr_or_braced_init_list ';'
                       | coroutine_return_statement
                       | GOTO IDENTIFIER ';'
    '''
    p[0] = ExternalNode('for_jump_statement', p[1:])

'''
coroutine_return_statement:
    co_return expr_or_braced_init_listopt ;
'''

def p_coroutine_return_statement(p):
    '''
        coroutine_return_statement : CO_RETURN expr_or_braced_init_list ';'
                                   | ';'
    '''
    p[0] = ExternalNode('coroutine_return_statement', p[1:])

'''
declaration_statement:
    block_declaration
'''

def p_declaration_statement(p):
    '''
        declaration_statement : block_declaration
    '''
    p[0] = ExternalNode('declaration_statement', p[1:])

