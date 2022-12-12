from .myast import InternalNode, ExternalNode

def p_class_name(p):
    '''
    class_name : CONSTEXPR
    '''
    p[0] = InternalNode('class_name', p[1])


def p_class_specifier(p):
    '''
    class_specifier : class_name '{' member_specification_opt '}'
    '''
    p[0] = ExternalNode('class_specifier', p[1:])





def p_member_specification(p):
    '''
    member_specification : member_declaration member_specification_opt
                         | access_specifier ':' member_specification_opt
    '''
    p[0] = ExternalNode('member_specification', p[1:])



def p_member_declaration(p):
    '''
    member_declaration : decl_specifier_seq_opt member_declarator_list_opt ';'
                       | function_definition
                       | empty_declaration
    '''
    p[0] = ExternalNode('member_declaration', p[1:])

def p_member_declarator_list(p):
    '''
    member_declarator_list : member_declarator
                           | member_declarator_list ',' member_declarator
    '''
    p[0] = ExternalNode('member_declarator_list', p[1:])





def p_member_declarator(p):
    '''
    member_declarator : declarator
                      | declarator initializer_opt
                      | identifier_opt ':' initializer_opt
    '''
    p[0] = InternalNode('member_declarator', p[1:])



def p_access_specifier(p):
    '''
    access_specifier : PRIVATE
                     | PROTECTED
                     | PUBLIC
    '''
    p[0] = ExternalNode('access_specifier', p[1:])

