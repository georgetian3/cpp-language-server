from .base import *

def p_member_specification_opt(p):
    '''
    member_specification_opt : member_specification
                             | empty
    '''
    p[0] = Node('member_specification_opt', '', p[1:])

def p_attribute_specifier_seq_opt(p):
    '''
    attribute_specifier_seq_opt : attribute_specifier_seq
                                | empty
    '''
    p[0] = Node('attribute_specifier_seq_opt', '', p[1:])

def p_class_virt_specifier_opt(p):
    '''
    class_virt_specifier_opt : class_virt_specifier
                             | empty
    '''
    p[0] = Node('class_virt_specifier_opt', '', p[1:])
    
def p_base_clause_opt(p):
    '''
    base_clause_opt : base_clause
                    | empty
    '''
    p[0] = Node('base_clause_opt', '', p[1:])

def p_nested_name_specifier_opt(p):
    '''
    nested_name_specifier_opt : nested_name_specifier
                              | empty
    '''
    p[0] = Node('nested_name_specifier_opt', '', p[1:])

def p_member_specification_opt(p):
    '''
    member_specification_opt : member_specification
                             | empty
    '''
    p[0] = Node('member_specification_opt', '', p[1:])

def p_decl_specifier_seq_opt(p):
    '''
    decl_specifier_seq_opt : decl_specifier_seq
                           | empty
    '''
    p[0] = Node('decl_specifier_seq_opt', '', p[1:])

def p_member_declarator_list_opt(p):
    '''
    member_declarator_list_opt : member_declarator_list
                               | empty
    '''
    p[0] = Node('member_declarator_list_opt', '', p[1:])

def p_virt_specifier_seq_opt(p):
    '''
    virt_specifier_seq_opt : virt_specifier_seq
                           | empty
    '''
    p[0] = Node('virt_specifier_seq_opt', '', p[1:])

def p_pure_specifier_opt(p):
    '''
    pure_specifier_opt : pure_specifier
                       | empty
    '''
    p[0] = Node('pure_specifier_opt', '', p[1:])

def p_brace_or_equal_initializer_opt(p):
    '''
    brace_or_equal_initializer_opt : brace_or_equal_initializer
                                   | empty
    '''
    p[0] = Node('brace_or_equal_initializer_opt', '', p[1:])

def p_identifier_opt(p):
    '''
    identifier_opt : IDENTIFIER
                   | empty
    '''
    p[0] = Node('identifier_opt', '', p[1:])

def p_conversion_declarator_opt(p):
    '''
    conversion_declarator_opt : conversion_declarator
                              | empty
    '''
    p[0] = Node('conversion_declarator_opt', '', p[1:])

def p_ellipsis_opt(p):
    '''
    ellipsis_opt : ELLIPSIS
                   | empty
    '''
    p[0] = Node('ellipsis_opt', '', p[1:])

def p_virtual_opt(p):
    '''
    virtual_opt : VIRTUAL
                | empty
    '''
    p[0] = Node('virtual_opt', '', p[1:])

def p_access_specifier_opt(p):
    '''
    access_specifier_opt = access_specifier
                         | empty
    '''
    p[0] = Node('access_specifier_opt', '', p[1:])

def p_expression_list_opt(p):
    '''
    expression_list_opt = expression_list
                        | empty
    '''
    p[0] = Node('expression_list_opt', '', p[1:])

def p_init_declarator_list_opt(p):
    '''
        init_declarator_list_opt = init_declarator_list
                                 | empty
    '''

def p_attribute_specifier_seq_opt(p):
    '''
        attribute_specifier_seq_opt = attribute_specifier_seq
                                    | empty
    '''
def p_ref_qualifier_opt(p):
    '''
        ref_qualifier_opt = ref_qualifier
                          | empty
    '''

def p_attribute_specifier_seq_opt(p):
    '''
        attribute_specifier_seq_opt : attribute_specifier_seq
                                    | empty
    '''
def p_constant_expression_opt(p):
    '''
        constant_expression_opt : constant_expression
                                | empty
    '''

def p_cv_qualifier_seq_opt(p):
    '''
        cv_qualifier_seq_opt : cv_qualifier_seq
                             | empty
    '''

def p_ref_qualifier_opt(p):
    '''
        cv_ref_qualifier_opt : ref_qualifier
                             | empty
    '''
def p_noexcept_specifier_opt(p):
    '''
        noexcept_specifier_opt : noexcept_specifier
                               | empty
    '''
def p_abstract_declarator_opt(p):
    '''
        abstract_declarator_opt : abstract_declarator
                                | empty
    '''
def p_noptr_abstract_declarator_opt(p):
    '''
        noptr_abstract_declarator_opt : noptr_abstract_declarator
                                      | empty
    '''
def p_constant_expression_opt(p):
    '''
        constant_expression_opt : constant_expression
                                | empty
    '''
def p_attribute_specifier_seq_opt(p):
    '''
        attribute_specifier_seq_opt : attribute_specifier_seq
                                    | empty
    '''
def p_comma_opt(p):
    ''' comma_opt : ','
                  | empty '''
    p[0] = Node('comma_opt', '', p[1:])

def p_decl_specifier_seq_opt(p):
    ''' decl_specifier_seq_opt : decl_specifier_seq
                               | empty '''
    p[0] = Node('decl_specifier_seq_opt', '', p[1:])
def p_virt_specifier_seq_opt(p):
    ''' virt_specifier_seq_opt : virt_specifier_seq
                               | empty '''
    p[0] = Node('virt_specifier_seq_opt', '', p[1:])

def p_ctor_initializer_opt(p):
    ''' ctor_initializer_opt : ctor_initializer
                             | empty '''
    p[0] = Node('ctor_initializer_opt', '', p[1:])

def p_enumerator_list_opt(p):
    ''' enumerator_list_opt : enumerator_list
                            | empty '''
    p[0] = Node('enumerator_list_opt', '', p[1:])

def p_enum_head_name_opt(p):
    ''' enum_head_name_opt : enum_head_name
                           | empty '''
    p[0] = Node('enum_head_name_opt', '', p[1:])

def p_enum_base_opt(p):
    ''' enum_base_opt : enum_base
                      | empty '''    
    p[0] = Node('enum_base_opt', '', p[1:])

def p_inline_opt(p):
    ''' inline_opt : INLINE
                   | empty '''
    p[0] = Node('inline_opt', '', p[1:])

def attribute_specifier_seq_opt(p):
    ''' attribute_specifier_seq_opt : attribute_specifier_seq
                                    | empty '''
    p[0] = Node('attribute_specifier_seq_opt', '', p[1:])

def declaration_seq_opt(p):
    ''' declaration_seq_opt : declaration_seq
                            | empty '''
    p[0] = Node('declaration_seq_opt', '', p[1:])

def p_nested_name_specifier_opt(p):
    ''' nested_name_specifier_opt : nested_name_specifier
                                  | empty '''
    p[0] = Node('nested_name_specifier_opt', '', p[1:])

def p_ellipsis_opt(p):
    ''' ellipsis_opt : ELLIPSIS
                       | empty '''
    p[0] = Node('ellipsis_opt', '', p[1:])

def p_attribute_using_prefix_opt(p):
    ''' attribute_using_prefix_opt : attribute_using_prefix
                                   | empty '''
    p[0] = Node('attribute_using_prefix_opt', '', p[1:])


def attribute_opt(p):
    ''' attribute_opt : attribute
                      | empty '''
    p[0] = Node('attribute_opt', '', p[1:])


def p_attribute_argument_clause_opt(p):
    ''' attribute_argument_clause_opt : attribute_argument_clause
                                      | empty '''
    p[0] = Node('attribute_argument_clause_opt', '', p[1:])


def p_balanced_token_seq_opt(p):
    ''' balanced_token_seq_opt : balanced_token_seq
                               | empty '''
    p[0] = Node('balanced_token_seq_opt', '', p[1:])

def p_attribute_specifier_seq_opt(p):
    '''
        attribute_specifier_seq_opt : attribute_specifier_seq 
                                    | empty
    '''