'''
declaration_seq:
    declaration
    declaration_seq declaration
declaration:
    block_declaration
    nodeclspec_function_declaration
    function_definition
    template_declaration
    deduction_guide
    explicit_instantiation
    explicit_specialization
    export_declaration
    linkage_specification
    namespace_definition
    empty_declaration
    attribute_declaration
    module_import_declaration
block_declaration:
    simple_declaration
    asm_declaration
    namespace_alias_definition
    using_declaration
    using_enum_declaration
    using_directive
    static_assert_declaration
    alias_declaration
    opaque_enum_declaration
nodeclspec_function_declaration:
    attribute_specifier_seqopt declarator ;
alias_declaration:
    using identifier attribute_specifier_seqopt = defining_type_id ;
simple_declaration:
    decl_specifier_seq init_declarator_listopt ;
    attribute_specifier_seq decl_specifier_seq init_declarator_list ;
    attribute_specifier_seqopt decl_specifier_seq ref_qualifieropt [ identifier_list ] initializer ;
static_assert_declaration:
    static_assert ( constant_expression ) ;
    static_assert ( constant_expression , string_literal ) ;
empty_declaration:
    ;
attribute_declaration:
    attribute_specifier_seq ;
'''
def p_declaration_seq(p):
    '''
        declaration_seq : declaration
                        | declaration_seq declaration
    '''

def p_declaration(p):
    '''
        declaration : block_declaration
                    | nodeclspec_function_declaration
                    | function_definition
                    | template_declaration
                    | deduction_guide
                    | explicit_instantiation
                    | explicit_specialization
                    | export_declaration
                    | linkage_specification
                    | namespace_definition
                    | empty_declaration
                    | attribute_declaration
                    | module_import_declaration
    '''
def p_block_declaration(p):
    '''
        block_declaration : simple_declaration
                          | asm_declaration
                          | namespace_alias_definition
                          | using_declaration
                          | using_enum_declaration
                          | using_directive
                          | static_assert_declaration
                          | alias_declaration
                          | opaque_enum_declaration
    '''

def p_nodeclspec_function_declaration(p):
    '''
        nodeclspec_function_declaration : declarator ';'
                                        | attribute_specifier_seq declarator ';'
    '''

def p_alias_declaration(p):
    '''
        alias_declaration : using identifier '=' defining_type_id ';'
                          | using identifier attribute_specifier_seq '=' defining_type_id ';' 
    '''
def p_simple_declaration(p):
    '''
        simple_declaration : decl_specifier_seq init_declarator_list_opt ';'
                           | attribute_specifier_seq decl_specifier_seq init_declarator_list ';'
                           | attribute_specifier_seq_opt decl_specifier_seq ref_qualifier_opt '[' identifier_list ']' initializer ';'
    '''
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

def p_static_assert_declaration(p):
    '''
        static_assert_declaration = static_assert '(' constant_expression ')' ';'
                                  | static_assert '(' constant_expression ',' string_literal ')' ';'
    '''

def p_empty_declaration(p):
    '''
        empty_declaration : ';'
    '''

def p_attribute_declaration(p):
    '''
        attribute_declaration : attribute_specifier_seq ';'
    '''