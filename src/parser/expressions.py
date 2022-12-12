from .myast import InternalNode, ExternalNode
import re
from lexer.identifiers import identifier
from lexer.keywords import keywords
from lexer.literals import literal

def p_expression(p):
    ''' expression : assignment_expression
                   | expression ',' assignment_expression '''
    p[0] = InternalNode('expression', p[1:])


# 7.5 Primary expressions

def p_primary_expression(p):
    ''' primary_expression : LITERAL
                           | IDENTIFIER
                           | '(' expression ')' '''
    if len(p) == 2:
        if re.match(literal, p[1]):
            p[0] = ExternalNode('literal', p[1])
        else:
            p[0] = ExternalNode('IDENTIFIER', p[1])
    else:
        p[0] = InternalNode('primary_expression', [p[2]])


# 7.6 Compound expressions


def p_type_specifier(p):
    '''
        type_specifier : class_name
                       | CHAR
                       | CHAR8_T
                       | CHAR16_T
                       | CHAR32_T
                       | WCHAR_T
                       | BOOL
                       | SHORT
                       | INT
                       | LONG
                       | SIGNED
                       | UNSIGNED
                       | FLOAT
                       | DOUBLE
                       | VOID
    '''
    p[0] = InternalNode('type_specifier', p[1:])

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
    if len(p) == 4 and p[1] != '(':
        p[3] = ExternalNode('IDENTIFIER',p[3])
    p[0] = InternalNode('postfix_expression', p[1:])
 
def p_expression_list(p):
    ''' expression_list : initializer_list '''
    p[0] = InternalNode('expression_list', p[1:])

# 7.6.2 Unary expressions

def p_unary_expression(p):
    ''' unary_expression : postfix_expression
                         | unary_operator cast_expression
                         | PLUSPLUS cast_expression
                         | MINUSMINUS cast_expression '''
    p[0] = InternalNode('unary_expression', p[1:])

def p_unary_operator(p):
    ''' unary_operator : '*'
                       | '&'
                       | '+'
                       | '-'
                       | '!'
                       | '~' '''
    p[0] = InternalNode('unary_operator', p[1:])

def p_cast_expression(p):
    ''' cast_expression : unary_expression '''
    p[0] = InternalNode('cast_expression', p[1:])


def p_pm_expression(p): # 7.6.4 Pointer-to-member operators
    ''' pm_expression : cast_expression
                      | pm_expression PERIODSTAR cast_expression
                      | pm_expression ARROWSTAR cast_expression '''
    p[0] = InternalNode('pm_expression', p[1:])
def p_multiplicative_expression(p): # 7.6.5 Multiplicative operators
    ''' multiplicative_expression : pm_expression
                                  | multiplicative_expression '*' pm_expression
                                  | multiplicative_expression '/' pm_expression
                                  | multiplicative_expression '%' pm_expression ''' 
    p[0] = InternalNode('multiplicative_expression', p[1:])
def p_additive_expression(p): # 7.6.6 Additive operators
    ''' additive_expression : multiplicative_expression
                            | additive_expression '+' multiplicative_expression
                            | additive_expression '-' multiplicative_expression '''
    p[0] = InternalNode('additive_expression', p[1:])
def p_shift_expression(p): # 7.6.7 Shift operators
    ''' shift_expression : additive_expression
                         | shift_expression LSHIFT additive_expression
                         | shift_expression RSHIFT additive_expression '''
    p[0] = InternalNode('shift_expression', p[1:])
def p_relational_expression(p): # 7.6.9 Relational operators
    ''' relational_expression : shift_expression
                              | relational_expression '<' shift_expression
                              | relational_expression '>' shift_expression
                              | relational_expression LE shift_expression
                              | relational_expression GE shift_expression '''
    p[0] = InternalNode('relational_expression', p[1:])
def p_equality_expression(p): # 7.6.10 Equality operators
    ''' equality_expression : relational_expression
                            | equality_expression EQ relational_expression
                            | equality_expression NE relational_expression '''
    p[0] = InternalNode('equality_expression', p[1:])
def p_and_expression(p): # 7.6.11 Bitwise AND operator
    ''' and_expression : equality_expression
                       | and_expression '&' equality_expression '''

    p[0] = InternalNode('and_expression', p[1:])
def p_exclusive_or_expression(p): # 7.6.12 Bitwise exclusive OR operator
    ''' exclusive_or_expression : and_expression
                                | exclusive_or_expression '^' and_expression '''
    p[0] = InternalNode('exclusive_or_expression', p[1:])
def p_inclusive_or_expression(p): # 7.6.13 Bitwise inclusive OR operator
    ''' inclusive_or_expression : exclusive_or_expression
                                | inclusive_or_expression '|' exclusive_or_expression '''
    p[0] = InternalNode('inclusive_or_expression', p[1:])
def p_logical_and_expression(p): # 7.6.14 Logical AND operator
    ''' logical_and_expression : inclusive_or_expression
                               | logical_and_expression LAND inclusive_or_expression '''
    p[0] = InternalNode('logical_and_expression', p[1:])
def p_logical_or_expression(p): # 7.6.15 Logical OR operator
    ''' logical_or_expression : logical_and_expression
                              | logical_or_expression LOR logical_and_expression '''
    p[0] = InternalNode('logical_or_expression', p[1:])
def p_conditional_expression(p): # 7.6.16 Conditional operator
    ''' conditional_expression : logical_or_expression
                               | logical_or_expression '?' expression ':' assignment_expression '''
    p[0] = InternalNode('conditional_expression', p[1:])
def p_assignment_expression(p): # 7.6.19 Assignment and compound assignment operators
    ''' assignment_expression : conditional_expression
                              | logical_or_expression assignment_operator assignment_expression '''
    p[0] = InternalNode('assignment_expression', p[1:])
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
    p[0] = InternalNode('assignment_operator', p[1:])

def p_constant_expression(p): # 7.7 Constant expressions
    ''' constant_expression : conditional_expression '''
    p[0] = InternalNode('constant_expression', p[1:])



def p_initializer(p): # 9.4 Initializers
    ''' initializer : '=' assignment_expression
                    | '(' expression_list ')' '''
    p[0] = InternalNode('initializer', p[1:])


def p_initializer_list(p):
    ''' initializer_list : assignment_expression
                         | initializer_list ',' assignment_expression '''
    p[0] = InternalNode('initializer_list', p[1:])

def p_class_name(p):
    '''
    class_name : IDENTIFIER
    '''
    p[1] = ExternalNode('IDENTIFIER',p[1])
    p[0] = InternalNode('class_name', p[1:])


def p_redirection(p):
    '''
    redirection : '*'
                | '&'
    '''
    p[0] = ExternalNode('redirection', p[1])