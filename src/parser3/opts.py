from .myast import InternalNode, ExternalNode

def p_member_specification_opt(p):
    '''
    member_specification_opt : member_specification
                             | empty
    '''
    p[0] = ExternalNode('member_specification_opt', p[1:])
    



def initializer_opt(p):
    '''
    initializer_opt : initializer
                    | empty
    '''
    p[0] = ExternalNode('initializer_opt', p[1:])

def p_identifier_opt(p):
    '''
    identifier_opt : IDENTIFIER
                   | empty
    '''
    p[0] = ExternalNode('identifier_opt', p[1:])





def p_access_specifier_opt(p):
    '''
    access_specifier_opt : access_specifier
                         | empty
    '''
    p[0] = ExternalNode('access_specifier_opt', p[1:])

def p_expression_list_opt(p):
    '''
    expression_list_opt : expression_list
                        | empty
    '''
    p[0] = ExternalNode('expression_list_opt', p[1:])




def p_comma_opt(p):
    ''' comma_opt : ','
                  | empty '''
    p[0] = ExternalNode('comma_opt', p[1:])





def p_declaration_seq_opt(p):
    ''' declaration_seq_opt : declaration_seq
                            | empty '''
    p[0] = ExternalNode('declaration_seq_opt', p[1:])




def p_balanced_token_seq_opt(p):
    ''' balanced_token_seq_opt : balanced_token_seq
                               | empty '''
    p[0] = ExternalNode('balanced_token_seq_opt', p[1:])


def p_identifier_list_opt(p):
    ''' identifier_list_opt : identifier_list
                            | empty '''
    p[0] = ExternalNode('identifier_list_opt', p[1:])




def p_parameter_declaration_list_opt(p):
    ''' parameter_declaration_list_opt : parameter_declaration_list
                                       | empty '''
    p[0] = ExternalNode('parameter_declaration_list_opt', p[1:])

def p_typename_opt(p):
    ''' typename_opt : TYPENAME
                     | empty '''
    p[0] = ExternalNode('typename_opt', p[1:])


def p_expression_opt(p):
    ''' expression_opt : expression
                       | empty '''
    p[0] = ExternalNode('expression_opt', p[1:])

def p_initializer_opt(p):
    ''' initializer_opt : initializer
                        | empty '''
    p[0] = ExternalNode('initializer_opt', p[1:])

def p_constant_expression_opt(p):
    ''' constant_expression_opt : constant_expression
                                | empty '''
    p[0] = ExternalNode('constant_expression_opt', p[1:])
