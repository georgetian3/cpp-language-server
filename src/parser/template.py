'''
template-declaration:
    template-head declaration
    template-head concept-definition
template-head:
    template < template-parameter-list > requires-clauseopt
template-parameter-list:
    template-parameter
    template-parameter-list , template-parameter
requires-clause:
    requires constraint-logical-or-expression
constraint-logical-or-expression:
    constraint-logical-and-expression
    constraint-logical-or-expression || constraint-logical-and-expression
constraint-logical-and-expression:
    primary-expression
    constraint-logical-and-expression && primary-expression
'''

def p_template_declaration(p):
    '''
        template_declaration : template-head declaration
                             | template-head concept-definition
    '''
def p_template_head(p):
    '''
        template_head : template-head declaration
                      | template-head concept-definition
    '''
def p_template_parameter(p):
    ''' 
        template_parameter : TEMPLATE '<' template_parameter_list ">" requires_clause
                           | TEMPLATE '<' template_parameter_list '>'
    '''
def p_template_parameter_list(p):
    '''
        template_parameter_list : template-parameter
                                | template-parameter-list ',' template-parameter
    '''
def p_require_clause(p):
    '''
        require_clause: REQUIRES constraint_logical_or_expression
    '''
def p_constraint_logical_or_expression(p):
    '''
        constraint_logical_or_expression : constraint_logical_and_expression
                                         | constraint_logical_or_expression
    '''
def p_type_parameter(p):
    '''
        type_parameter : 
    '''
                      