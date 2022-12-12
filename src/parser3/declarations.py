from .myast import InternalNode, ExternalNode


def p_declaration_seq(p):
    '''
        declaration_seq : declaration
                        | declaration_seq declaration
    '''
    p[0] = ExternalNode('declaration_seq', p[1:])

def p_declaration(p):
    '''
        declaration : simple_declaration
                    | nodeclspec_function_declaration
                    | function_definition
                    | empty_declaration
    '''
    p[0] = ExternalNode('declaration', p[1:])


def p_nodeclspec_function_declaration(p):
    '''
        nodeclspec_function_declaration : declarator ';'
    '''
    p[0] = ExternalNode('nodeclspec_function_declaration', p[1:])



def p_function_declaration(p):
    ''' function_declaration : function_head '''
    p[0] = InternalNode('function_declaration', p[1:])


def p_function_head(p):
    ''' function_head : type_specifier IDENTIFIER '(' parameter_declaration_list ')' '''
    p[0] = InternalNode('function_head', p[1:])


def p_function_definition(p):
    ''' function_definition : function_head function_body '''
    p[0] = InternalNode('function_definition', p[1:])

def p_simple_declaration(p):
    '''
        simple_declaration : decl_specifier_seq init_declarator_list_opt ';'
    '''


def p_empty_declaration(p):
    '''
        empty_declaration : ';'
    '''
    p[0] = ExternalNode('empty_declaration', p[1:])


def p_defining_type_specifier(p):
    '''
        defining_type_specifier : type_specifier
                                | class_specifier
    '''

def p_decl_specifier(p):
    '''
        decl_specifier : defining_type_specifier
    '''
    p[0] = ExternalNode('decl_specifier', p[1:])

def p_decl_specifier_seq(p):
    '''
        decl_specifier_seq : decl_specifier
                           | decl_specifier decl_specifier_seq
    '''
    p[0] = ExternalNode('decl_specifier_seq', p[1:])





def p_type_specifier_seq(p):
    '''
        type_specifier_seq : type_specifier
                           | type_specifier type_specifier_seq
    '''


def p_init_declarator_list(p):
    '''
        init_declarator_list : init_declarator
                             | init_declarator_list ',' init_declarator
    '''
    p[0] = ExternalNode('init_declarator_list', p[1:])

def p_init_declarator(p):
    '''
        init_declarator : declarator
                        | declarator initializer
    '''
    p[0] = ExternalNode('init_declarator', p[1:])


def p_declarator(p):
    '''
        declarator : ptr_declarator
                   | noptr_declarator
    '''
    p[0] = ExternalNode('declarator', p[1:])

def p_ptr_declarator(p):
    '''
        ptr_declarator : noptr_declarator
                       | ptr_operator ptr_declarator
    '''
    p[0] = ExternalNode('ptr_declarator', p[1:])


def p_noptr_declarator(p):
    '''
        noptr_declarator : declarator_id
                         | noptr_declarator '[' constant_expression_opt ']'
                         | '(' ptr_declarator ')'
    '''

    p[0] = ExternalNode('noptr_declarator', p[1:])




def p_ptr_operator(p):
    '''
        ptr_operator : '*'
                     | '&'
                     | LAND
    '''
    p[0] = ExternalNode('ptr_operator', p[1:])

def p_declarator_id(p):
    '''
        declarator_id : id_expression
    '''
    p[0] = ExternalNode('declarator_id', p[1:])



# 9.3.3.5 Functions

def p_parameter_declaration(p):
    ''' parameter_declaration : decl_specifier_seq declarator 
                              | decl_specifier_seq declarator '=' assignment_expression
    '''
def p_parameter_declaration_list(p):
    ''' parameter_declaration_list : parameter_declaration
                                   | parameter_declaration_list ',' parameter_declaration '''




# 9.5 Function definitions

# 9.5.1 In general

def p_function_body(p):
    ''' function_body : compound_statement '''
    p[0] = ExternalNode('function_body', p[1:])
# 9.6 Structured binding declarations


def p_balanced_token_seq(p):
    ''' balanced_token_seq : balanced_token
                           | balanced_token_seq balanced_token '''
    p[0] = ExternalNode('balanced_token_seq', p[1:])

def p_balanced_token(p):
    ''' balanced_token : '(' balanced_token_seq_opt ')'
                       | '[' balanced_token_seq_opt ']'
                       | '{' balanced_token_seq_opt '}' '''
    #  any token other than a parenthesis, a bracket, or a brace '''  
    # TODO
    p[0] = ExternalNode('balanced_token', p[1:])
