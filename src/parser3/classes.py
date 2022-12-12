from .myast import InternalNode, ExternalNode


def p_class_declaration(p):
    '''
    class_declaration   : CLASS IDENTIFIER
    '''
    p[0] = ExternalNode('class_declaration', p[2])

def p_class_declaration_definition(p):
    '''
    class_declaration_definition    : class_declaration '{' member_specification '}'
    '''
    p[0] = InternalNode('class_declaration_definition', p[1:])



def p_member_specification(p):
    '''
    member_specification    : declaration member_specification
                            | access_specifier ':' member_specification
                            | empty
    '''
    p[0] = InternalNode('member_specification', p[1:])


def p_access_specifier(p):
    '''
    access_specifier    : PRIVATE
                        | PROTECTED
                        | PUBLIC
    '''
    p[0] = ExternalNode('access_specifier', p[1])

