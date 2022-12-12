from .myast import InternalNode, ExternalNode


def p_expression(p):
    ''' expression : assignment_expression
                   | expression ',' assignment_expression '''
    p[0] = InternalNode('expression', p[1:])


# 7.5 Primary expressions

def p_primary_expression(p):
    ''' primary_expression : LITERAL
                           | '(' expression ')' '''
    p[0] = ExternalNode('primary_expression', p[1:])

def p_id_expression(p):
    ''' id_expression : unqualified_id '''
    p[0] = ExternalNode('id_expression', p[1:])

def p_unqualified_id(p):
    ''' unqualified_id : IDENTIFIER
                       | '~' type_specifier '''
    p[0] = ExternalNode('unqualified_id', p[1:])


# 7.6 Compound expressions

# 7.6.1 Postfix expressions
def p_postfix_expression(p):
    ''' postfix_expression : primary_expression
                           | postfix_expression '[' expression ']'
                           | postfix_expression '(' expression_list ')'
                           | postfix_expression '(' ')'
                           | type_specifier '(' expression_list ')'
                           | type_specifier '(' ')'
                           | '(' expression_list ')'
                           | '(' ')'
                           | postfix_expression '.' IDENTIFIER
                           | postfix_expression ARROW IDENTIFIER
                           | postfix_expression PLUSPLUS
                           | postfix_expression MINUSMINUS '''
    p[0] = ExternalNode('postfix_expression', p[1:])
 
def p_expression_list(p):
    ''' expression_list : initializer_list '''
    p[0] = ExternalNode('expression_list', p[1:])

# 7.6.2 Unary expressions

def p_unary_expression(p):
    ''' unary_expression : postfix_expression
                         | unary_operator cast_expression
                         | PLUSPLUS cast_expression
                         | MINUSMINUS cast_expression '''
    p[0] = ExternalNode('unary_expression', p[1:])

def p_unary_operator(p):
    ''' unary_operator : '*'
                       | '&'
                       | '+'
                       | '-'
                       | '!'
                       | '~' '''
    p[0] = ExternalNode('unary_operator', p[1:])

def p_cast_expression(p):
    ''' cast_expression : unary_expression
                        | '(' type_id ')' cast_expression '''
    p[0] = ExternalNode('cast_expression', p[1:])

# 7.6.4 Pointer-to-member operators
def p_pm_expression(p):
    ''' pm_expression : cast_expression
                      | pm_expression PERIODSTAR cast_expression
                      | pm_expression ARROWSTAR cast_expression '''
    p[0] = ExternalNode('pm_expression', p[1:])

# 7.6.5 Multiplicative operators
def p_multiplicative_expression(p):
    ''' multiplicative_expression : pm_expression
                                  | multiplicative_expression '*' pm_expression
                                  | multiplicative_expression '/' pm_expression
                                  | multiplicative_expression '%' pm_expression ''' 
    p[0] = ExternalNode('multiplicative_expression', p[1:])

# 7.6.6 Additive operators
def p_additive_expression(p):
    ''' additive_expression : multiplicative_expression
                            | additive_expression '+' multiplicative_expression
                            | additive_expression '-' multiplicative_expression '''
    p[0] = ExternalNode('additive_expression', p[1:])

# 7.6.7 Shift operators
def p_shift_expression(p):
    ''' shift_expression : additive_expression
                         | shift_expression LSHIFT additive_expression
                         | shift_expression RSHIFT additive_expression '''
    p[0] = ExternalNode('shift_expression', p[1:])

# 7.6.9 Relational operators
def p_relational_expression(p):
    ''' relational_expression : shift_expression
                              | relational_expression '<' shift_expression
                              | relational_expression '>' shift_expression
                              | relational_expression LE shift_expression
                              | relational_expression GE shift_expression '''
    p[0] = ExternalNode('relational_expression', p[1:])
# 7.6.10 Equality operators
def p_equality_expression(p):
    ''' equality_expression : relational_expression
                            | equality_expression EQ relational_expression
                            | equality_expression NE relational_expression '''
    p[0] = ExternalNode('equality_expression', p[1:])
# 7.6.11 Bitwise AND operator
def p_and_expression(p):
    ''' and_expression : equality_expression
                       | and_expression '&' equality_expression '''

    p[0] = ExternalNode('and_expression', p[1:])
# 7.6.12 Bitwise exclusive OR operator
def p_exclusive_or_expression(p):
    ''' exclusive_or_expression : and_expression
                                | exclusive_or_expression '^' and_expression '''
    p[0] = ExternalNode('exclusive_or_expression', p[1:])
# 7.6.13 Bitwise inclusive OR operator
def p_inclusive_or_expression(p):
    ''' inclusive_or_expression : exclusive_or_expression
                                | inclusive_or_expression '|' exclusive_or_expression '''
    p[0] = ExternalNode('inclusive_or_expression', p[1:])
# 7.6.14 Logical AND operator
def p_logical_and_expression(p):
    ''' logical_and_expression : inclusive_or_expression
                               | logical_and_expression LAND inclusive_or_expression '''
    p[0] = ExternalNode('logical_and_expression', p[1:])
# 7.6.15 Logical OR operator
def p_logical_or_expression(p):
    ''' logical_or_expression : logical_and_expression
                              | logical_or_expression LOR logical_and_expression '''
    p[0] = ExternalNode('logical_or_expression', p[1:])
# 7.6.16 Conditional operator
def p_conditional_expression(p):
    ''' conditional_expression : logical_or_expression
                               | logical_or_expression '?' expression ':' assignment_expression '''
    p[0] = ExternalNode('conditional_expression', p[1:])
# 7.6.19 Assignment and compound assignment operators
def p_assignment_expression(p):
    ''' assignment_expression : conditional_expression
                              | logical_or_expression assignment_operator assignment_expression '''
    p[0] = ExternalNode('assignment_expression', p[1:])
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
    p[0] = ExternalNode('assignment_operator', p[1:])
# 7.7 Constant expressions
def p_constant_expression(p):
    ''' constant_expression : conditional_expression '''
    p[0] = ExternalNode('constant_expression', p[1:])