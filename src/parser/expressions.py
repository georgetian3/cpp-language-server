# 7.5 Primary expressions

def p_primary_expression(p):
    ''' primary_expression : LITERAL
                           | this
                           | '('expression')'
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
                       | '~' type_name
                       | '~' decltype_specifier
                       | template_id '''

# 7.5.4.2 Qualified names
def p_qualified_id(p):
    ''' qualified_id : nested_name_specifier TEMPLATE unqualified_id
                     | nested_name_specifier unqualified_id '''

def p_nested_name_specifier(p):
    ''' nested_name_specifier : 
                              | DCOLON
                              | type_name DCOLON
                              | namespace_name DCOLON
                              | decltype_specifier DCOLON
                              | nested_name_specifier identifier DCOLON
                              | nested_name_specifier TEMPLATE simple_template_id DCOLON 
                              | nested_name_specifier simple_template_id DCOLON '''

#7.5.5 Lambda expressions
# TODO
#7.5.6 Fold expressions
# TODO
#7.5.7 Requires expressions
# TODO

# 7.6 Compound expressions

# 7.6.1 Postfix expressions
def p_postfix_expression(p):
    ''' postfix_expression : primary_expression
                           | postfix_expression '[' expr_or_braced_init_list ']'
                           | postfix_expression '(' expression_list ')'
                           | postfix_expression '(' ')'
                           | simple_type_specifier '(' expression_list ')'
                           | simple_type_specifier '(' ')'
                           | typename_specifier '(' expression_list ')'
                           | typename_specifier '(' ')'
                           | simple_type_specifier braced_init_list
                           | typename_specifier braced_init_list
                           | postfix_expression '.' TEMPLATE id_expression
                           | postfix_expression '.' id_expression
                           | postfix_expression ARROW TEMPLATE id_expression
                           | postfix_expression ARROW id_expression
                           | postfix_expression PLUSPLUS
                           | postfix_expression MINUSMINUS
                           | DYNAMIC_CAST '<' type_id '>' '(' expression ')'
                           | STATIC_CAST '<' type_id '>' '(' expression ')'
                           | REINTERPRET_CAST '<' type_id '>' '(' expression ')'
                           | CONST_CAST '<' type_id '>' '(' expression ')'
                           | TYPEID '(' expression ')'
                           | TYPEID '(' type_id ')' '''
 
def p_expression_list(p):
    ''' expression_list : initializer_list '''

# 7.6.2 Unary expressions

def p_unary_expression(p):
    ''' unary_expression : postfix_expression
                         | unary_operator cast_expression
                         | PLUSPLUS cast_expression
                         | MINUSMINUS cast_expression
                         | await_expression
                         | SIZEOF unary_expression
                         | SIZEOF '(' type_id ')'
                         | SIZEOF ELLIPSIS '(' IDENTIFIER ')'
                         | ALIGNOF '(' type_id ')'
                         | noexcept_expression
                         | new_expression
                         | delete_expression '''

def p_unary_operator(p):
    ''' unary_operator : '*' | '&' | '+' | '-' | '!' | '~' '''

# 7.6.2.7 New
# TODO
# 7.6.2.8 Delete
# TODO

# 7.6.3 Explicit type conversion (cast notation)
def p_cast_expression(p):
    ''' cast_expression : unary_expression
                        | '(' type_id ')' cast_expression '''

# 7.6.4 Pointer-to-member operators
def p_pm_expression(p):
    ''' pm_expression : cast_expression
                      | pm_expression PERIODSTAR cast_expression
                      | pm_expression ARROWSTAR cast_expression '''

# 7.6.5 Multiplicative operators
def p_multiplicative_expression(p):
    ''' multiplicative_expression : pm_expression
                                  | multiplicative_expression '*' pm_expression
                                  | multiplicative_expression '/' pm_expression
                                  | multiplicative_expression '%' pm_expression ''' 
# 7.6.6 Additive operators
def p_additive_expression(p):
    ''' additive_expression : multiplicative_expression
                            | additive_expression + multiplicative_expression
                            | additive_expression - multiplicative_expression '''
# 7.6.7 Shift operators
def p_shift_expression(p):
    ''' shift_expression : additive_expression
                         | shift_expression << additive_expression
                         | shift_expression >> additive_expression '''

# 7.7 Constant expressions

def p_constant_expression(p):
    ''' constant_expression : conditional_expression '''