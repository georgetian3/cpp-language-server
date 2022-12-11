from .myast import InternalNode, ExternalNode

def p_member_specification_opt(p):
    '''
    member_specification_opt : member_specification
                             | empty
    '''
    p[0] = ExternalNode('member_specification_opt', p[1:])
    

def p_class_virt_specifier_opt(p):
    '''
    class_virt_specifier_opt : class_virt_specifier
                             | empty
    '''
    p[0] = ExternalNode('class_virt_specifier_opt', p[1:])
    
def p_base_clause_opt(p):
    '''
    base_clause_opt : base_clause
                    | empty
    '''
    p[0] = ExternalNode('base_clause_opt', p[1:])


def p_member_declarator_list_opt(p):
    '''
    member_declarator_list_opt : member_declarator_list
                               | empty
    '''
    p[0] = ExternalNode('member_declarator_list_opt', p[1:])


def p_pure_specifier_opt(p):
    '''
    pure_specifier_opt : pure_specifier
                       | empty
    '''
    p[0] = ExternalNode('pure_specifier_opt', p[1:])

def p_brace_or_equal_initializer_opt(p):
    '''
    brace_or_equal_initializer_opt : brace_or_equal_initializer
                                   | empty
    '''
    p[0] = ExternalNode('brace_or_equal_initializer_opt', p[1:])

def p_identifier_opt(p):
    '''
    identifier_opt : IDENTIFIER
                   | empty
    '''
    p[0] = ExternalNode('identifier_opt', p[1:])

def p_conversion_declarator_opt(p):
    '''
    conversion_declarator_opt : conversion_declarator
                              | empty
    '''
    p[0] = ExternalNode('conversion_declarator_opt', p[1:])


def p_virtual_opt(p):
    '''
    virtual_opt : VIRTUAL
                | empty
    '''
    p[0] = ExternalNode('virtual_opt', p[1:])

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

def p_init_declarator_list_opt(p):
    '''
        init_declarator_list_opt : init_declarator_list
                                 | empty
    '''
    p[0] = ExternalNode('init_declarator_list_opt', p[1:])


def p_constant_expression_opt(p):
    '''
        constant_expression_opt : constant_expression
                                | empty
    '''
    p[0] = ExternalNode('constant_expression_opt', p[1:])

def p_cv_qualifier_seq_opt(p):
    '''
        cv_qualifier_seq_opt : cv_qualifier_seq
                             | empty
    '''
    p[0] = ExternalNode('cv_qualifier_seq_opt', p[1:])

def p_ref_qualifier_opt(p):
    '''
        ref_qualifier_opt : ref_qualifier
                             | empty
    '''
    p[0] = ExternalNode('ref_qualifier_opt', p[1:])

def p_noexcept_specifier_opt(p):
    '''
        noexcept_specifier_opt : noexcept_specifier
                               | empty
    '''
    p[0] = ExternalNode('noexcept_specifier_opt', p[1:])

def p_abstract_declarator_opt(p):
    '''
        abstract_declarator_opt : abstract_declarator
                                | empty
    '''
    p[0] = ExternalNode('abstract_declarator_opt', p[1:])

def p_noptr_abstract_declarator_opt(p):
    '''
        noptr_abstract_declarator_opt : noptr_abstract_declarator
                                      | empty
    '''
    p[0] = ExternalNode('noptr_abstract_declarator_opt', p[1:])

def p_comma_opt(p):
    ''' comma_opt : ','
                  | empty '''
    p[0] = ExternalNode('comma_opt', p[1:])

def p_decl_specifier_seq_opt(p):
    ''' decl_specifier_seq_opt : decl_specifier_seq
                               | empty '''
    p[0] = ExternalNode('decl_specifier_seq_opt', p[1:])
def p_virt_specifier_seq_opt(p):
    ''' virt_specifier_seq_opt : virt_specifier_seq
                               | empty '''
    p[0] = ExternalNode('virt_specifier_seq_opt', p[1:])

def p_ctor_initializer_opt(p):
    ''' ctor_initializer_opt : ctor_initializer
                             | empty '''
    p[0] = ExternalNode('ctor_initializer_opt', p[1:])

def p_enumerator_list_opt(p):
    ''' enumerator_list_opt : enumerator_list
                            | empty '''
    p[0] = ExternalNode('enumerator_list_opt', p[1:])

def p_enum_head_name_opt(p):
    ''' enum_head_name_opt : enum_head_name
                           | empty '''
    p[0] = ExternalNode('enum_head_name_opt', p[1:])

def p_enum_base_opt(p):
    ''' enum_base_opt : enum_base
                      | empty '''    
    p[0] = ExternalNode('enum_base_opt', p[1:])

def p_inline_opt(p):
    ''' inline_opt : INLINE
                   | empty '''
    p[0] = ExternalNode('inline_opt', p[1:])

def p_declaration_seq_opt(p):
    ''' declaration_seq_opt : declaration_seq
                            | empty '''
    p[0] = ExternalNode('declaration_seq_opt', p[1:])

def p_nested_name_specifier_opt(p):
    ''' nested_name_specifier_opt : nested_name_specifier
                                  | empty '''
    p[0] = ExternalNode('nested_name_specifier_opt', p[1:])

def p_ellipsis_opt(p):
    ''' ellipsis_opt : ELLIPSIS
                       | empty '''
    p[0] = ExternalNode('ellipsis_opt', p[1:])

def p_attribute_using_prefix_opt(p):
    ''' attribute_using_prefix_opt : attribute_using_prefix
                                   | empty '''
    p[0] = ExternalNode('attribute_using_prefix_opt', p[1:])


def p_attribute_opt(p):
    ''' attribute_opt : attribute
                      | empty '''
    p[0] = ExternalNode('attribute_opt', p[1:])


def p_attribute_argument_clause_opt(p):
    ''' attribute_argument_clause_opt : attribute_argument_clause
                                      | empty '''
    p[0] = ExternalNode('attribute_argument_clause_opt', p[1:])


def p_balanced_token_seq_opt(p):
    ''' balanced_token_seq_opt : balanced_token_seq
                               | empty '''
    p[0] = ExternalNode('balanced_token_seq_opt', p[1:])
    
def p_handler_seq_opt(p):
    ''' handler_seq_opt : handler_seq
                        | empty '''
    p[0] = ExternalNode('handler_seq_opt', p[1:])

def p_group_opt(p):
    ''' group_opt : group
                  | empty '''
    p[0] = ExternalNode('group_opt', p[1:])
def p_pp_global_module_fragment_opt(p):
    ''' pp_global_module_fragment_opt : pp_global_module_fragment
                                      | empty '''
    p[0] = ExternalNode('pp_global_module_fragment_opt', p[1:])
def p_pp_private_module_fragment_opt(p):
    ''' pp_private_module_fragment_opt : pp_private_module_fragment
                                       | empty '''
    p[0] = ExternalNode('pp_private_module_fragment_opt', p[1:])
def p_identifier_list_opt(p):
    ''' identifier_list_opt : identifier_list
                            | empty '''
    p[0] = ExternalNode('identifier_list_opt', p[1:])
def p_pp_tokens_opt(p):
    ''' pp_tokens_opt : pp_tokens
                      | empty '''
    p[0] = ExternalNode('pp_tokens_opt', p[1:])
def p_elif_groups_opt(p):
    ''' elif_groups_opt : elif_groups
                        | empty '''
    p[0] = ExternalNode('elif_groups_opt', p[1:])    
def p_else_groups_opt(p):
    ''' else_group_opt : else_group
                       | empty '''
    p[0] = ExternalNode('else_group_opt', p[1:])
def p_export_opt(p):
    ''' export_opt : EXPORT
                      | empty '''
    p[0] = ExternalNode('export_opt', p[1:])

def p_template_opt(p):
    ''' template_opt : TEMPLATE
                     | empty '''
    p[0] = ExternalNode('template_opt', p[1:])

def p_explicit_specifier_opt(p):
    ''' explicit_specifier_opt : explicit_specifier
                               | empty '''
    p[0] = ExternalNode('explicit_specifier_opt', p[1:])

def p_extern_opt(p):
    ''' extern_opt : EXTERN
                   | empty '''
    p[0] = ExternalNode('extern_opt', p[1:])

def p_parameter_declaration_list_opt(p):
    ''' parameter_declaration_list_opt : parameter_declaration_list
                                       | empty '''
    p[0] = ExternalNode('parameter_declaration_list_opt', p[1:])

def p_typename_opt(p):
    ''' typename_opt : TYPENAME
                     | empty '''
    p[0] = ExternalNode('typename_opt', p[1:])

def p_ptr_abstract_declarator_opt(p):
    ''' ptr_abstract_declarator_opt : ptr_abstract_declarator
                                    | empty '''
    p[0] = ExternalNode('ptr_abstract_declarator_opt', p[1:])

def p_dcolon_opt(p):
    ''' dcolon_opt : DCOLON
                   | empty '''
    p[0] = ExternalNode('dcolon_opt', p[1:])

def p_new_placement_opt(p):
    ''' new_placement_opt : new_placement
                          | empty '''
    p[0] = ExternalNode('new_placement_opt', p[1:])

def p_new_initializer_opt(p):
    ''' new_initializer_opt : new_initializer
                            | empty '''
    p[0] = ExternalNode('new_initializer_opt', p[1:])

def p_new_declarator_opt(p):
    ''' new_declarator_opt : new_declarator
                           | empty '''
    p[0] = ExternalNode('new_declarator_opt', p[1:])

def p_expression_opt(p):
    ''' expression_opt : expression
                       | empty '''
    p[0] = ExternalNode('expression_opt', p[1:])

def p_attribute_specifier_seq_opt(p):
    ''' attribute_specifier_seq_opt : attribute_specifier_seq
                                   | empty '''
    p[0] = ExternalNode('attribute_specifier_seq_opt', p[1:])

def p_global_module_fragment_opt(p):
    ''' global_module_fragment_opt : global_module_fragment
                                   | empty '''
    p[0] = ExternalNode('global_module_fragment_opt', p[1:])
def p_private_module_fragment_opt(p):
    ''' private_module_fragment_opt : private_module_fragment
                                    | empty '''
    p[0] = ExternalNode('private_module_fragment_opt', p[1:])