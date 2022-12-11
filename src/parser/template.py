from .base import p_empty, Node

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
    p[0] = Node('template_declaration', '', p[1:])

def p_template_head(p):
    '''
        template_head : TEMPLATE '<' template_parameter_list ">" requires_clause
                      | TEMPLATE '<' template_parameter_list '
    '''
    p[0] = Node('template_head', '', p[1:])

def p_template_parameter_list(p):
    '''
        template_parameter_list : template_parameter
                                | template_parameter_list ',' template_parameter
    '''
    p[0] = Node('template_parameter_list', '', p[1:])

def p_require_clause(p):
    '''
        require_clause: REQUIRES constraint_logical_or_expression
    '''
    p[0] = Node('require_clause', '', p[1:])

def p_constraint_logical_or_expression(p):
    '''
        constraint_logical_or_expression : constraint_logical_and_expression
                                         | constraint_logical_or_expression t_LOR constraint_logical_and_expression
    '''
    p[0] = Node('constraint_logical_or_expression', '', p[1:])

def p_constraint_logical_and_expression(p):
    '''
        constraint_logical_and_expression : primary_expression
                                          | constraint_logical_and_expression LAND primary_expression
    '''
    p[0] = Node('constraint_logical_and_expression', '', p[1:])

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
    p[0] = Node('template_parameter', '', p[1:])

def p_type_parameter(p):
    '''
        type_parameter : type_parameter_key
                       | type_parameter_key ELLIPSIS
                       | type_parameter_key identifier
                       | type_parameter_key ELLIPSIS identifier
                       | type_parameter_key '=' type_id
                       | type_parameter_key identifier '=' type_id
                       | type_constraint
                       | type_constraint ELLIPSIS
                       | type_constraint identifier
                       | type_constraint ELLIPSIS identifier
                       | type_constraint '=' type_id
                       | type_constraint identifier '=' type_id
                       | template_head type_parameter_key
                       | template_head type_parameter_key ELLIPSIS
                       | template_head type_parameter_key identifier
                       | template_head type_parameter_key ELLIPSIS identifier
                       | template_head type_parameter_key '=' type_id
                       | template_head type_parameter_key identifier '=' type_id
    '''
    p[0] = Node('type_parameter', '', p[1:])

def p_type_parameter_key(p):
    '''
        type_parameter_key : CLASS
                           | TYPENAME
    '''
    p[0] = Node('type_parameter_key', '', p[1:])

def p_type_constraint(p):
    '''
            type_constraint: concept_name
                             | nested_name_specifier concept_name
                             | concept_name '<' '>'
                             | nested_name_specifier concept_name '<' '>'
                             | nested_name_specifier concept_name '<' template_argument_list '>'
                             | concept_name '<' template_argument_list '>'
    '''     
    p[0] = Node('type_constraint', '', p[1:])



'''
simple_template_id:
    template_name < template_argument_listopt >
template_id:
    simple_template_id
    operator_function_id < template_argument_listopt >
    literal_operator_id < template_argument_listopt >
template_name:
    identifier
template_argument_list:
    template_argument ...opt
    template_argument_list , template_argument ...opt
template_argument:
    constant_expression
    type_id
    id_expression
'''

def p_simple_template_id(p):
    '''
        simple_template_id: template_name '<' '>'
                          | template_name '<' template_argument_list '>' 
    '''
    p[0] = Node('simple_template_id', '', p[1:])

def p_template_id(p):
    '''
        template_id : simple_template_id
                    | operator_function_id '<' '>'
                    | operator_function_id '<' template_argument_list '>'
                    | literal_operator_id '<' '>'
                    | literal_operator_id '<' template_argument_list '>'
    '''
    p[0] = Node('template_id', '', p[1:])

def p_template_name(p):
    '''
        template_name : t_IDENTIFIER
    '''
    p[0] = Node('template_name', '', p[1:])

def p_template_argument_list(p):
    '''
        template_argument_list : template_argument
                               | template_argument t_ELLIPSIS
                               | template_argument_list ',' template_argument
                               | template_argument_list ',' template_argument t_ELLIPSIS
    '''
    p[0] = Node('template_argument_list', '', p[1:])

def p_template_argument(p):
    '''
        template_argument: constant_expression
                         | type_id
                         | id_expression
    '''
    p[0] = Node('template_argument', '', p[1:])