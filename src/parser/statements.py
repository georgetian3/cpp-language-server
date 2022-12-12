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
                  | declaration_statement
                  | jump_statement '''

    p[0] = InternalNode('statement', p[1:])


def p_init_statement(p):
    ''' init_statement : simple_declaration_definition ';'
                       | simple_definition ';' '''
    p[0] = InternalNode('init_statement', p[1:])
def p_condition(p):
    ''' condition : expression
                  | simple_definition '''
    p[0] = InternalNode('condition', p[1:])


def p_labeled_statement(p):
    '''
        labeled_statement : IDENTIFIER ':' statement
                         | CASE IDENTIFIER ':' statement
                         | DEFAULT ':' statement
    '''
    if len(p) == 5 and str(p[1]) == "case":
        p[2] = ExternalNode('IDENTIFIER', p[2])
    p[0] = InternalNode('labeled_statement', p[1:])


# 8.3 Expression statement
def p_expression_statement(p):
    ''' expression_statement : expression ';'
                             | ';' '''
    p[0] = InternalNode('expression_statement', [p[1]])

def p_compound_statement(p):
    '''
        compound_statement : '{' '}'
                           | '{' statement_seq '}'
    '''
    p[0] = InternalNode('compound_statement', [p[2]])

def p_statement_seq(p):
    '''
        statement_seq : statement
                      | statement_seq statement
    '''
    p[0] = InternalNode('statement_seq', p[1:])


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
    p[0] = InternalNode('selection_statement', p[1:])

def p_iteration_statement(p):
    '''
    iteration_statement : WHILE '(' condition ')' statement
                        | DO statement WHILE '(' expression ')' ';'
                        | FOR '(' init_statement ';' ')' statement
                        | FOR '(' init_statement condition ';' ')' statement
                        | FOR '(' init_statement ';' expression ')' statement
                        | FOR '(' init_statement condition ';' expression ')' statement
    '''
    p[0] = InternalNode('iteration_statement', p[1:])

def p_identifier_list(p):
    '''
    identifier_list : IDENTIFIER
                    | identifier_list ',' IDENTIFIER   
    '''
    if len(p) == 2:
        p[1] = ExternalNode('IDENTIFIER',p[1])
    else :
        p[3] = ExternalNode('IDENTIFIER',p[3])

    p[0] = InternalNode('identifier_list', p[1:])  


def p_jump_statement(p):
    '''
    jump_statement  : BREAK ';'
                    | CONTINUE ';'
                    | RETURN ';'
                    | RETURN expression ';'
                    | GOTO IDENTIFIER ';'
    '''
    if len(p) == 4 and str(p[1]) == "return":
        p[1] = ExternalNode('RETURN', p[1])
    elif len(p) == 4 and str(p[1]) == "goto":
        p[1] = ExternalNode('GOTO', p[1])
        p[2] = ExternalNode('IDENTIFIER',p[2])
    elif len(p) == 3 and str(p[1]) == "return":
        p[1] = ExternalNode('RETURN', p[1])
    elif len(p) == 3 and str(p[1]) == "break":
        p[1] = ExternalNode('BREAK', p[1])
    elif len(p) == 3 and str(p(1)) == "continue":
        p[1] = ExternalNode('CONTINUE', p[1])
    p[0] = InternalNode('jump_statement', p[1:])


def p_declaration_statement(p):
    '''
    declaration_statement : declaration
    '''
    p[0] = InternalNode('declaration_statement', [p[1]])

