'''
template_declaration:
    template_head declaration
    template_head concept_definition
template_head:
    template < template_parameter_list > requires_clauseopt
template_parameter_list:
    template_parameter
    template_parameter_list , template_parameter
requires_clause:
    requires constraint_logical_or_expression
constraint_logical_or_expression:
    constraint_logical_and_expression
    constraint_logical_or_expression || constraint_logical_and_expression
constraint_logical_and_expression:
    primary_expression
    constraint_logical_and_expression && primary_expression
'''

def p_template_declaration(p):
    '''
        template_declaration : template_head declaration
                             | template_head concept_definition
    '''
def p_template_head(p):
    '''
        template_head : t_TEMPLATE '<' template_parameter_list ">" requires_clause
                      | t_TEMPLATE '<' template_parameter_list '
    '''

def p_template_parameter_list(p):
    '''
        template_parameter_list : template_parameter
                                | template_parameter_list ',' template_parameter
    '''
def p_require_clause(p):
    '''
        require_clause: t_REQUIRES constraint_logical_or_expression
    '''
def p_constraint_logical_or_expression(p):
    '''
        constraint_logical_or_expression : constraint_logical_and_expression
                                         | constraint_logical_or_expression t_LOR constraint_logical_and_expression
    '''
def p_constraint_logical_and_expression(p):
    '''
        constraint_logical_and_expression : primary_expression
                                          | constraint_logical_and_expression t_LAND primary_expression
    '''

'''
template_parameter:
    type_parameter
    parameter_declaration
type_parameter:
    type_parameter_key ...opt identifieropt
    type_parameter_key identifieropt = type_id
    type_constraint ...opt identifieropt
    type_constraint identifieropt = type_id
    template_head type_parameter_key ...opt identifieropt
    template_head type_parameter_key identifieropt = id_expression
type_parameter_key:
    class
    typename
type_constraint:
    nested_name_specifieropt concept_name
    nested_name_specifieropt concept_name < template_argument_listopt >
'''

def p_template_parameter(p):
    ''' 
        template_parameter : type_parameter
                             parameter_declaration
    '''
def p_type_parameter(p):
    '''
        type_parameter : type_parameter_key
                       | type_parameter_key t_ELLIPSIS
                       | type_parameter_key identifier
                       | type_parameter_key t_ELLIPSIS identifier
                       | type_parameter_key '=' type_id
                       | type_parameter_key identifier '=' type_id
                       | type_constraint
                       | type_constraint t_ELLIPSIS
                       | type_constraint identifier
                       | type_constraint t_ELLIPSIS identifier
                       | type_constraint '=' type_id
                       | type_constraint identifier '=' type_id
                       | template_head type_parameter_key
                       | template_head type_parameter_key t_ELLIPSIS
                       | template_head type_parameter_key identifier
                       | template_head type_parameter_key t_ELLIPSIS identifier
                       | template_head type_parameter_key '=' type_id
                       | template_head type_parameter_key identifier '=' type_id
    '''
def p_type_parameter_key(p):
    '''
        type_parameter_key : t_CLASS
                           | t_TYPENAME
    '''
def p_type_constraint(p):
    '''
            p_type_constraint: concept_name
                             | nested_name_specifier concept_name
                             | concept_name '<' '>'
                             | nested_name_specifier concept_name '<' '>'
                             | 
            nested_name_specifieropt concept_name < template_argument_listopt >
    '''