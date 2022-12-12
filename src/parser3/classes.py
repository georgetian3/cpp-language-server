from .myast import InternalNode, ExternalNode


def p_class_declaration(p):
    '''
    class_declaration   : CLASS class_name
    '''
    p[2] = ExternalNode('IDENTIFIER', p[2])
    p[0] = InternalNode('class_declaration',p[1:])
def p_class_declaration_definition(p):
    '''
    class_declaration_definition    : class_declaration '{' member_specification '}'
    '''
    p[0] = InternalNode('class_declaration_definition', p[1:])



def p_member_specification(p):
    '''
    member_specification    : declaration ';' member_specification 
                            | access_specifier ':' member_specification
                            | special_function_declaration member_specification
                            | special_function_declaration_definition member_specification
                            | '~' special_function_declaration member_specification
                            | '~' special_function_declaration_definition member_specification
                            | empty
    '''
    p[0] = InternalNode('member_specification', p[1:])


def p_special_function_declaration(p):
    '''
    special_function_declaration : class_name '(' parameter_declaration_list ')'
    '''
    p[0] = InternalNode('special_function_declaration', p[1:])

def p_special_function_declaration_definition(p):
    '''
    special_function_declaration_definition : special_function_declaration function_body
    '''
    p[0] = InternalNode('special_function_declaration_definition', p[1:])


def p_access_specifier(p):
    '''
    access_specifier    : PRIVATE
                        | PROTECTED
                        | PUBLIC
    '''
    p[0] = ExternalNode('access_specifier', p[1])

