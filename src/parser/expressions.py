# 7.5 Primary expressions

def p_primary_expression(p):
    ''' primary_expression : literal
                           | this
                           | ( expression )
                           | id_expression
                           | lambda_expression
                           | fold_expression
                           | requires_expression '''

# 7.5.4 Names

def p_id_expression(p):
    ''' id_expression : unqualified_id
                      | qualified_id '''

# 7.5.4.1 Unqualified names

def p_unqualified_id(p):
    ''' unqualified_id : identifier
                       | operator_function_id
                       | conversion_function_id
                       | literal_operator_id
                       | ~ type_name
                       | ~ decltype_specifier
                       | template_id '''

# 7.5.4.2 Qualified names
def p_qualified_id(p):
    ''' qualified_id : nested_name_specifier templateopt unqualified_id
                     | nested_name_specifier :
                     | ::
                     | type_name ::
                     | namespace_name ::
                     | decltype_specifier ::
                     | nested_name_specifier identifier ::
                     | nested_name_specifier templateopt simple_template_id :: '''

# 7.7 Constant expressions

def p_constant_expression(p):
    ''' constant_expression : conditional_expression '''