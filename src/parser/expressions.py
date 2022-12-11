from .myast import Node

# 7.5 Primary expressions

def p_primary_expression(p):
    ''' primary_expression : LITERAL
                           | THIS
                           | '(' expression ')'
                           | id_expression
                           | lambda_expression
                           | fold_expression
                           | requires_expression '''
    p[0] = Node('primary_expression', '', p[1:])

def p_lambda_expression(p):
    ''' lambda_expression : IDENTIFIER '''
    # TODO

def p_fold_expression(p):
    ''' fold_expression : IDENTIFIER '''
    # TODO

def p_requires_expression(p):
    ''' requires_expression : IDENTIFIER '''
    # TODO
# 7.5.4 Names

def p_id_expression(p):
    ''' id_expression : unqualified_id
                      | qualified_id '''
    p[0] = Node('id_expression', '', p[1:])

# 7.5.4.1 Unqualified names

def p_unqualified_id(p):
    ''' unqualified_id : IDENTIFIER
                       | operator_function_id
                       | conversion_function_id
                       | literal_operator_id
                       | '~' type_name
                       | '~' decltype_specifier
                       | template_id '''
    p[0] = Node('unqualified_id', '', p[1:])

# 7.5.4.2 Qualified names
def p_qualified_id(p):
    ''' qualified_id : nested_name_specifier TEMPLATE unqualified_id
                     | nested_name_specifier unqualified_id '''
    p[0] = Node('qualified_id', '', p[1:])

def p_nested_name_specifier(p):
    ''' nested_name_specifier : 
                              | DCOLON
                              | type_name DCOLON
                              | namespace_name DCOLON
                              | decltype_specifier DCOLON
                              | nested_name_specifier IDENTIFIER DCOLON
                              | nested_name_specifier TEMPLATE simple_template_id DCOLON 
                              | nested_name_specifier simple_template_id DCOLON '''
    p[0] = Node('nested_name_specifier', '', p[1:])

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
    p[0] = Node('postfix_expression', '', p[1:])
 
def p_expression_list(p):
    ''' expression_list : initializer_list '''
    p[0] = Node('expression_list', '', p[1:])

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
    p[0] = Node('unary_expression', '', p[1:])

def p_unary_operator(p):
    ''' unary_operator : '*'
                       | '&'
                       | '+'
                       | '-'
                       | '!'
                       | '~' '''
    p[0] = Node('unary_operator', '', p[1:])

# 7.6.2.3 Await
def p_await_expression(p):
    ''' await_expression : CO_AWAIT cast_expression '''

# 7.6.2.6 noexcept operator
def p_noexcept_expression(p):
    ''' noexcept_expression : NOEXCEPT '(' expression ')' '''

# 7.6.2.7 New

def p_new_expression(p):
    ''' new_expression : dcolon_opt NEW new_placement_opt new_type_id new_initializer_opt
                       | dcolon_opt NEW new_placement_opt '(' type_id ')' new_initializer_opt '''

def p_new_placement(p):
    ''' new_placement : '(' expression_list ')' '''
def p_new_type_id(p):
    ''' new_type_id : type_specifier_seq new_declarator_opt '''

def p_new_declarator(p):
    ''' new_declarator : new_declarator_opt
                     | noptr_new_declarator '''

def p_noptr_new_declarator(p):
    ''' noptr_new_declarator : '[' expression_opt ']' attribute_specifier_seq_opt
                             | noptr_new_declarator '[' constant_expression ']' attribute_specifier_seq_opt '''
def p_new_initializer(p):
    ''' new_initializer : '(' expression_list_opt ')'
                        | braced_init_list '''

# 7.6.2.8 Delete

def p_delete_expression(p):
    ''' delete_expression : dcolon_opt DELETE cast_expression
                          | dcolon_opt DELETE '[' ']' cast_expression '''

# 7.6.3 Explicit type conversion (cast notation)
def p_cast_expression(p):
    ''' cast_expression : unary_expression
                        | '(' type_id ')' cast_expression '''
    p[0] = Node('cast_expression', '', p[1:])

# 7.6.4 Pointer-to-member operators
def p_pm_expression(p):
    ''' pm_expression : cast_expression
                      | pm_expression PERIODSTAR cast_expression
                      | pm_expression ARROWSTAR cast_expression '''
    p[0] = Node('pm_expression', '', p[1:])

# 7.6.5 Multiplicative operators
def p_multiplicative_expression(p):
    ''' multiplicative_expression : pm_expression
                                  | multiplicative_expression '*' pm_expression
                                  | multiplicative_expression '/' pm_expression
                                  | multiplicative_expression '%' pm_expression ''' 
    p[0] = Node('multiplicative_expression', '', p[1:])

# 7.6.6 Additive operators
def p_additive_expression(p):
    ''' additive_expression : multiplicative_expression
                            | additive_expression '+' multiplicative_expression
                            | additive_expression '-' multiplicative_expression '''
    p[0] = Node('additive_expression', '', p[1:])

# 7.6.7 Shift operators
def p_shift_expression(p):
    ''' shift_expression : additive_expression
                         | shift_expression LSHIFT additive_expression
                         | shift_expression RSHIFT additive_expression '''
    p[0] = Node('shift_expression', '', p[1:])
# 7.6.8 Three-way comparison operator
def p_compare_expression(p):
    ''' compare_expression : shift_expression
                           | compare_expression SPACESHIP shift_expression '''
    p[0] = Node('compare_expression', '', p[1:])

# 7.6.9 Relational operators
def p_relational_expression(p):
    ''' relational_expression : compare_expression
                              | relational_expression '<' compare_expression
                              | relational_expression '>' compare_expression
                              | relational_expression LE compare_expression
                              | relational_expression GE compare_expression '''
    p[0] = Node('relational_expression', '', p[1:])
# 7.6.10 Equality operators
def p_equality_expression(p):
    ''' equality_expression : relational_expression
                            | equality_expression EQ relational_expression
                            | equality_expression NE relational_expression '''
    p[0] = Node('equality_expression', '', p[1:])
# 7.6.11 Bitwise AND operator
def p_and_expression(p):
    ''' and_expression : equality_expression
                       | and_expression '&' equality_expression '''

    p[0] = Node('and_expression', '', p[1:])
# 7.6.12 Bitwise exclusive OR operator
def p_exclusive_or_expression(p):
    ''' exclusive_or_expression : and_expression
                                | exclusive_or_expression '^' and_expression '''
    p[0] = Node('exclusive_or_expression', '', p[1:])



# 7.6.13 Bitwise inclusive OR operator
def p_inclusive_or_expression(p):
    ''' inclusive_or_expression : exclusive_or_expression
                                | inclusive_or_expression '|' exclusive_or_expression '''
    p[0] = Node('inclusive_or_expression', '', p[1:])

# 7.6.14 Logical AND operator

def p_logical_and_expression(p):
    ''' logical_and_expression : inclusive_or_expression
                               | logical_and_expression LAND inclusive_or_expression '''
    p[0] = Node('logical_and_expression', '', p[1:])

# 7.6.15 Logical OR operator
def p_logical_or_expression(p):
    ''' logical_or_expression : logical_and_expression
                              | logical_or_expression LOR logical_and_expression '''
    p[0] = Node('logical_or_expression', '', p[1:])
# 7.6.16 Conditional operator
def p_conditional_expression(p):
    ''' conditional_expression : logical_or_expression
                               | logical_or_expression CONDOP expression ':' assignment_expression '''
    p[0] = Node('conditional_expression', '', p[1:])

# 7.6.17 Yielding a value
def p_yield_expression(p):
    ''' yield_expression : CO_YIELD assignment_expression
                         | CO_YIELD braced_init_list '''
    p[0] = Node('yield_expression', '', p[1:])

# 7.6.18 Throwing an exception
def p_throw_expression(p):
    ''' throw_expression : THROW assignment_expression
                         | empty '''
    p[0] = Node('throw_expression', '', p[1:])

# 7.6.19 Assignment and compound assignment operators
def p_assignment_expression(p):
    ''' assignment_expression : conditional_expression
                              | yield_expression
                              | throw_expression
                              | logical_or_expression assignment_operator initializer_clause '''
    p[0] = Node('assignment_expression', '', p[1:])
def p_assignment_operator(p):
    ''' assignment_operator : '='
                            | TIMESEQUAL
                            | DIVEQUAL
                            | MODEQUAL
                            | PLUSEQUAL
                            | MINUSEQUAL
                            | RSHIFTEQUAL
                            | LSHIFTEQUAL
                            | ANDEQUAL
                            | XOREQUAL
                            | OREQUAL '''
    p[0] = Node('assignment_operator', '', p[1:])

# 7.6.20 Comma operator
def p_expression(p):
    ''' expression : assignment_expression
                   | expression ',' assignment_expression '''
    p[0] = Node('expression', '', p[1:])

# 7.7 Constant expressions
def p_constant_expression(p):
    ''' constant_expression : conditional_expression '''
    p[0] = Node('constant_expression', '', p[1:])
