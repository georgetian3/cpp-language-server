from .myast import InternalNode, ExternalNode


def p_declaration_seq(p):
    '''
    declaration_seq : declaration
                    | declaration_seq declaration
    '''
    p[0] = InternalNode('declaration_seq', p[1:])


def p_declaration(p):
    '''
    declaration : simple_declaration ';'
                | simple_declaration_definition ';'
                | function_declaration ';'
                | function_declaration_definition
                | class_declaration ';'
                | class_declaration_definition ';'
    '''
    p[0] = InternalNode('declaration', p[1:])

def p_brackets(p):
    '''
    brackets    : '[' expression_opt ']'
    '''

def p_simple_declaration(p):
    '''
    simple_declaration  : qualifier_opt type_specifier redirection_opt IDENTIFIER brackets_opt
    '''
    if len(p) == 3:
        p[2] = ExternalNode('IDENTIFIER',p[2])
    elif len(p) == 2:
        p[1] = ExternalNode('IDENTIFIER',p[1])
    p[0] = InternalNode('simple_declaration', p[1:])


def p_qualifier(p):
    '''
    qualifier   : CONST
                | VOLATILE
    '''
    p[0] = ExternalNode('qualifier', p[1])

def p_simple_declaration_definition(p):
    '''
        simple_declaration_definition   : simple_declaration
                                        | simple_declaration '=' assignment_expression
    '''
    p[0] = InternalNode('simple_declaration_definition', p[1:])
def p_definition(p):
    '''
        definition  : simple_definition ';'
    '''
    p[0] = InternalNode('definition', p[1:])
def p_simple_definition(p):
    '''
        simple_definition   : IDENTIFIER '=' assignment_expression
    '''
    #p[1] = ExternalNode('IDENTIFIER',p[1])
    p[0] = InternalNode('simple_definition', p[1:])

def p_function_declaration(p):
    ''' function_declaration : simple_declaration '(' parameter_declaration_list ')' '''
    p[0] = InternalNode('function_declaration', p[1:])
def p_function_declaration_definition(p):
    ''' function_declaration_definition : function_declaration function_body '''
    p[0] = InternalNode('function_declaration_definition', p[1:])
def p_parameter_declaration_list(p):
    '''
    parameter_declaration_list  : simple_declaration_definition
                                | parameter_declaration_list ',' simple_declaration_definition
                                | empty
    '''
    p[0] = InternalNode('parameter_declaration_list', p[1:])


# 9.5 Function definitions

# 9.5.1 In general

def p_function_body(p):
    ''' function_body : compound_statement '''
    p[0] = InternalNode('function_body', p[1:])
# 9.6 Structured binding declarations


def p_balanced_token_seq(p):
    ''' balanced_token_seq : balanced_token
                           | balanced_token_seq balanced_token '''
    p[0] = InternalNode('balanced_token_seq', p[1:])

def p_balanced_token(p):
    ''' balanced_token : '(' balanced_token_seq_opt ')'
                       | '[' balanced_token_seq_opt ']'
                       | '{' balanced_token_seq_opt '}' '''
    #  any token other than a parenthesis, a bracket, or a brace '''  
    # TODO
    p[0] = InternalNode('balanced_token', p[1:])
