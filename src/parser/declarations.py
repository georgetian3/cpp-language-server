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
        alias_declaration : USING IDENTIFIER '=' defining_type_id ';'
                          | USING IDENTIFIER attribute_specifier_seq '=' defining_type_id ';' 
    '''
def p_simple_declaration(p):
    '''
        simple_declaration : decl_specifier_seq init_declarator_list_opt ';'
                           | attribute_specifier_seq decl_specifier_seq init_declarator_list ';'
                           | attribute_specifier_seq_opt decl_specifier_seq ref_qualifier_opt '[' identifier_list ']' initializer ';'
    '''
def p_init_declarator_list_opt(p):
    '''
        init_declarator_list_opt : init_declarator_list
                                 | empty
    '''

def p_attribute_specifier_seq_opt(p):
    '''
        attribute_specifier_seq_opt : attribute_specifier_seq
                                    | empty
    '''
def p_ref_qualifier_opt(p):
    '''
        ref_qualifier_opt : ref_qualifier
                          | empty
    '''

def p_static_assert_declaration(p):
    '''
        static_assert_declaration : STATIC_ASSERT '(' constant_expression ')' ';'
                                  | STATIC_ASSERT '(' constant_expression ',' string_literal ')' ';'
    '''

def p_empty_declaration(p):
    '''
        empty_declaration : ';'
    '''

def p_attribute_declaration(p):
    '''
        attribute_declaration : attribute_specifier_seq ';'
    '''

'''
decl_specifier:
    storage_class_specifier
    defining_type_specifier
    function_specifier
    friend
    typedef
    constexpr
    consteval
    constinit
    inline
decl_specifier_seq:
    decl_specifier attribute_specifier_seqopt
    decl_specifier decl_specifier_seq
'''

def p_decl_specifier(p):
    '''
        decl_specifier : storage_class_specifier
                       | defining_type_specifier
                       | function_specifier
                       | FRIEND
                       | TYPEDEF
                       | constexpr
                       | consteval
                       | constinit
                       | INLINE
    '''

def p_decl_specifier_seq(p):
    '''
        decl_specifier_seq : decl_specifier
                           | decl_specifier attribute_specifier_seq
                           | decl_specifier decl_specifier_seq
    '''

'''
storage_class_specifier:
    static
    thread_local
    extern
    mutable
'''

def p_storage_class_specifier(p):
    '''
        storage_class_specifier : STATIC
                                | THREAD_LOCAL
                                | EXTERN
                                | MUTABLE
    '''

'''
function_specifier:
    virtual
    explicit_specifier
explicit_specifier:
    explicit ( constant_expression )
    explicit
'''

def p_function_specifier(p):
    '''
        function_specifier : VIRTUAL
                           | explicit_specifier
    '''
def p_explicit_specifier(p):
    '''
        explicit_specifier : explicit '(' constant_expression ')'
                           | explicit
    '''

'''
typedef_name:
    identifier
    simple_template_id
'''

def p_typedef_name(p):
    '''
        typedef_name : IDENTIFIER
                     | simple_template_id
    '''


'''
type_specifier:
    simple_type_specifier
    elaborated_type_specifier
    typename_specifier
    cv_qualifier
type_specifier_seq:
    type_specifier attribute_specifier_seqopt
    type_specifier type_specifier_seq
defining_type_specifier:
    type_specifier
    class_specifier
    enum_specifier
defining_type_specifier_seq:
    defining_type_specifier attribute_specifier_seqopt
    defining_type_specifier defining_type_specifier_seq
'''

def p_type_specifier(p):
    '''
        type_specifier : simple_type_specifier
                       | elaborated_type_specifier
                       | typename_specifier
                       | cv_qualifier
    '''
def p_type_specifier_seq(p):
    '''
        type_specifier_seq : type_specifier
                           | type_specifier  attribute_specifier_seq
                           | type_specifier type_specifier_seq
    '''
def p_defining_type_specifier(p):
    '''
        defining_type_specifier : type_specifier
                                | class_specifier
                                | enum_specifier
    '''
def p_defining_type_specifier_seq(p):
    '''
        defining_type_specifier_seq : defining_type_specifier
                                    | defining_type_specifier attribute_specifier_seq
                                    | defining_type_specifier defining_type_specifier_seq
    '''

'''
simple_type_specifier:
    nested_name_specifieropt type_name
    nested_name_specifier template simple_template_id
    decltype_specifier
    placeholder_type_specifier
    nested_name_specifieropt template_name
    char
    char8_t
    char16_t
    char32_t
    wchar_t
    bool
    short
    int
    long
    signed
    unsigned
    float
    double
    void
type_name:
    class_name
    enum_name
    typedef_name
'''
def p_simple_type_specifier(p):
    '''
        simple_type_specifier : type_name
                              | nested_name_specifier type_name
                              | nested_name_specifier template simple_template_id
                              | decltype_specifier
                              | placeholder_type_specifier
                              | template_name
                              | nested_name_specifier template_name
                              | CHAR
                              | CHAR8_T
                              | CHAR_16_T
                              | CHAR_32_T
                              | WCHAR_T
                              | BOOL
                              | SHORT
                              | INT
                              | LONG
                              | SIGNED
                              | UNSIGNED
                              | float
                              | DOUBLE
                              | VOID
    '''
def p_type_name(p):
    '''
        type_name : class_name
                  | enum_name
                  | typedef_name
    '''

'''
elaborated_type_specifier:
    class_key attribute_specifier_seqopt nested_name_specifieropt identifier
    class_key simple_template_id
    class_key nested_name_specifier templateopt simple_template_id
    elaborated_enum_specifier
elaborated_enum_specifier:
    enum nested_name_specifieropt identifier
'''

def p_elaborated_type_specifier(p):
    '''
        elaborated_type_specifier : class_key attribute_specifier_seq_opt IDENTIFIER
                                  | class_key attribute_specifier_seq_opt nested_name_specifier IDENTIFIER
                                  | class_key simple_template_id
                                  | simple_template_id
                                  | class_key nested_name_specifier template simple_template_id
                                  | elaborated_enum_specifier
    '''

def p_attribute_specifier_seq_opt(p):
    '''
        attribute_specifier_seq_opt : attribute_specifier_seq 
                                    | empty
    '''
def p_elaborated_enum_specifier(p):
    '''
        elaborated_enum_specifier : enum nested_name_specifier IDENTIFIER
                                  | IDENTIFIER
    '''

'''
placeholder_type_specifier:
    type_constraintopt auto
    type_constraintopt decltype ( auto )
'''

def p_placeholder_type_specifier(p):
    '''
        placeholder_type_specifier : AUTO
                                   | type_constraint AUTO
                                   | decltype '(' AUTO ')'
                                   | type_constraint decltype '(' AUTO ')'
    '''


'''
init_declarator_list:
    init_declarator
    init_declarator_list , init_declarator
init_declarator:
    declarator initializeropt
    declarator requires_clause
'''

def p_init_declarator_list(p):
    '''
        init_declarator_list : init_declarator
                             | init_declarator_list ',' init_declarator
    '''
def p_init_declarator(p):
    '''
        init_declarator : declarator
                        | declarator initializer
                        | declarator requires_clause
    '''
'''
declarator:
    ptr_declarator
    noptr_declarator parameters_and_qualifiers trailing_return_type
ptr_declarator:
    noptr_declarator
    ptr_operator ptr_declarator
noptr_declarator:
    declarator_id attribute_specifier_seqopt
    noptr_declarator parameters_and_qualifiers
    noptr_declarator [ constant_expressionopt ] attribute_specifier_seqopt
    ( ptr_declarator )
parameters_and_qualifiers:
    ( parameter_declaration_clause ) cv_qualifier_seqopt
    ref_qualifieropt noexcept_specifieropt attribute_specifier_seqopt
trailing_return_type :
    _> type_id
ptr_operator:
    * attribute_specifier_seqopt cv_qualifier_seqopt
    & attribute_specifier_seqopt
    && attribute_specifier_seqopt
    nested_name_specifier * attribute_specifier_seqopt cv_qualifier_seqopt
cv_qualifier_seq:
    cv_qualifier cv_qualifier_seqopt
cv_qualifier:
    const
    volatile
ref_qualifier:
    &
    &&
declarator_id:
    ...opt id_expression
'''
def p_declarator(p):
    '''
        declarator : ptr_declarator
                   | noptr_declarator parameters_and_qualifiers trailing_return_type
    '''
def p_ptr_declarator(p):
    '''
        ptr_declarator : noptr_declarator
                       | ptr_operator ptr_declarator
    '''
def p_noptr_declarator(p):
    '''
        noptr_declarator : declarator_id attribute_specifier_seq_opt
                         | noptr_declarator parameters_and_qualifiers
                         | noptr_declarator '[' constant_expression_opt ']' attribute_specifier_seq_opt
                         | '(' ptr_declarator ')'
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

def p_parameters_and_qualifiers(p):
    '''
        parameters_and_qualifiers : '(' parameter_declaration_clause ')' cv_qualifier_seq_opt
                                  | ref_qualifier_opt noexcept_specifier_opt attribute_specifier_seq_opt
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

def p_trailing_return_type(p):
    '''
       trailing_return_type : ARROW type_id
    '''
def p_ptr_operator(p):
    '''
        ptr_operator : '*' attribute_specifier_seq_opt cv_qualifier_seq_opt
                     | '&' attribute_specifier_seq_opt
                     | LAND attribute_specifier_seq_opt
                     | nested_name_specifier '*' attribute_specifier_seq_opt cv_qualifier_seq_opt
    '''
def p_cv_qualifier_seq(p):
    '''
        cv_qualifier_seq : cv_qualifier cv_qualifier_seq_opt
    '''
def p_cv_qualifier(p):
    '''
        cv_qualifier : CONST
                     | VOLATILE 
    '''   

def p_ref_qualifier(p):
    '''
        ref_qualifier : '&'
                      | LAND
    '''
def p_declarator_id(p):
    '''
        declarator_id : id_expression
                      | ELLIPSIS id_expression  
    '''

'''
type_id:
    type_specifier_seq abstract_declaratoropt
defining_type_id:
    defining_type_specifier_seq abstract_declaratoropt
abstract_declarator:
    ptr_abstract_declarator
    noptr_abstract_declaratoropt parameters_and_qualifiers trailing_return_type
    abstract_pack_declarator
ptr_abstract_declarator:
    noptr_abstract_declarator
    ptr_operator ptr_abstract_declaratoropt
noptr_abstract_declarator:
    noptr_abstract_declaratoropt parameters_and_qualifiers
    noptr_abstract_declaratoropt [ constant_expressionopt ] attribute_specifier_seqopt
    ( ptr_abstract_declarator )
abstract_pack_declarator:
    noptr_abstract_pack_declarator
    ptr_operator abstract_pack_declarator
noptr_abstract_pack_declarator:
    noptr_abstract_pack_declarator parameters_and_qualifiers
    noptr_abstract_pack_declarator [ constant_expressionopt ] attribute_specifier_seqopt
    ...
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
def p_type_id(p):
    '''
        type_id : type_specifier_seq abstract_declarator_opt
    '''
def p_defining_type_id(p):
    '''
        defining_type_id : defining_type_specifier_seq abstract_declarator_opt
    '''
def p_abstract_declarator(p):
    '''
        abstract_declarator : ptr_abstract_declarator
                            | noptr_abstract_declarator_opt parameters_and_qualifiers trailing_return_type
                            | abstract_pack_declarator
    '''
def p_noptr_abstract_declarator(p):
    '''
        noptr_abstract_declarator : noptr_abstract_declarator_opt parameters_and_qualifiers
                                  | noptr_abstract_declarator_opt '[' constant_expression_opt ']' attribute_specifier_seq_opt
                                  | '(' ptr_abstract_declarator ')'
    '''
def p_abstract_pack_declarator(p):
    '''
        abstract_pack_declarator : noptr_abstract_pack_declarator
                                 | ptr_operator abstract_pack_declarator
    '''
def p_noptr_abstract_pack_declarator(p):
    '''
        noptr_abstract_pack_declarator : noptr_abstract_pack_declarator parameters_and_qualifiers
                                       | noptr_abstract_pack_declarator '[' constant_expression_opt ']' attribute_specifier_seq_opt
                                       | ELLIPSIS
    '''


# 9.4 Initializers

def p_initializer(p):
    ''' initializer : brace_or_equal_initializer
                    | '(' expression_list ')' '''

def p_brace_or_equal_initializer(p):
    ''' brace_or_equal_initializer : '=' initializer_clause
                                   | braced_init_list '''


def p_initializer_clause(p):
    ''' initializer_clause : assignment_expression
                           | braced_init_list '''

def p_comma_opt(p):
    ''' comma_opt : ','
                  | empty '''

def p_braced_init_list(p):
    ''' braced_init_list : '{' initializer_list comma_opt '}'
                         | '{' designated_initializer_list comma_opt '}'
                         | '{' '}' '''


def p_initializer_list(p):
    ''' initializer_list : initializer_clause ellipsis_opt
                         | initializer_list ',' initializer_clause ellipsis_opt '''


def p_designated_initializer_list(p):
    ''' designated_initializer_list : designated_initializer_clause       
                                    | designated_initializer_list ',' designated_initializer_clause '''

def p_designated_initializer_clause(p):
    ''' designated_initializer_clause : designator brace_or_equal_initializer '''

def p_designator(p):
    ''' designator : '.' IDENTIFIER'''

def p_expr_or_braced_init_list(p):
    ''' expr_or_braced_init_list : expression
                                 | braced_init_list '''

# 9.5 Function definitions

# 9.5.1 In general


def p_decl_specifier_seq_opt(p):
    ''' decl_specifier_seq_opt : decl_specifier_seq
                               | empty '''
def p_virt_specifier_seq_opt(p):
    ''' virt_specifier_seq_opt : virt_specifier_seq
                               | empty '''
def p_function_definition(p):
    ''' function_definition : attribute_specifier_seq_opt decl_specifier_seq_opt declarator virt_specifier_seq_opt function_body
                            | attribute_specifier_seq_opt decl_specifier_seq_opt declarator requires_clause function_body '''

def p_ctor_initializer_opt(p):
    ''' ctor_initializer_opt : ctor_initializer
                             | empty '''
def p_function_body(p):
    ''' function_body : ctor_initializer_opt compound_statement
                      | function_try_block
                      | '=' DEFAULT ';'
                      | '=' DELETE ';' '''
# 9.6 Structured binding declarations

# 9.7 Enumerations

# 9.7.1 Enumeration declarations

def p_enum_name(p):
    ''' enum_name : IDENTIFIER '''

def p_enum_specifier(p):
    ''' enum_specifier : enum_head '{' enumerator_list_opt '}'
                       | enum_head '{' enumerator_list ',' '}' '''

def p_enumerator_list_opt(p):
    ''' enumerator_list_opt : enumerator_list
                            | empty '''

def p_enum_head_name_opt(p):
    ''' enum_head_name_opt : enum_head_name
                           | empty '''

def p_enum_base_opt(p):
    ''' enum_base_opt : enum_base
                      | empty '''    

def p_enum_head(p):
    ''' enum_head : enum_key attribute_specifier_seq_opt enum_head_name_opt enum_base_opt '''

def p_enum_head_name(p):
    ''' enum_head_name : nested_name_specifier_opt IDENTIFIER '''

def p_opaque_enum_declaration(p):
    ''' opaque_enum_declaration : enum_key attribute_specifier_seq_opt enum_head_name enum_base_opt ';' '''

def p_enum_key(p):
    ''' enum_key : ENUM
                 | ENUM CLASS
                 | ENUM STRUCT '''

def p_enum_base(p):
    ''' enum_base : ':' type_specifier_seq '''

    
def p_enumerator_list(p):
    ''' enumerator_list : enumerator_definition
                        | enumerator_list ',' enumerator_definition '''

def p_enumerator_definition(p):
    ''' enumerator_definition : enumerator
                              | enumerator '=' constant_expression '''

def p_enumerator(p):
    ''' enumerator : IDENTIFIER attribute_specifier_seq_opt '''

# 9.7.2 The using enum declaration
 
def p_using_enum_declaration(p):
    ''' using_enum_declaration : USING elaborated_enum_specifier ';' '''


# 9.8 Namespaces

# 9.8.1 Namespace definition

def p_namespace_name(p):
    ''' namespace_name : IDENTIFIER
                       | namespace_alias '''


def p_namespace_definition(p):
    ''' namespace_definition : named_namespace_definition
                             | unnamed_namespace_definition
                             | nested_namespace_definition '''

def p_inline_opt(p):
    ''' inline_opt : INLINE
                   | empty '''

def attribute_specifier_seq_opt(p):
    ''' attribute_specifier_seq_opt : attribute_specifier_seq
                                    | empty '''

def declaration_seq_opt(p):
    ''' declaration_seq_opt : declaration_seq
                            | empty '''

def p_named_namespace_definition(p):
    ''' named_namespace_definition : inline_opt NAMESPACE attribute_specifier_seq_opt IDENTIFIER '{' namespace_body '}' '''

def p_unnamed_namespace_definition(p):
    ''' unnamed_namespace_definition : inline_opt NAMESPACE attribute_specifier_seq_opt '{' namespace_body '}' '''

def p_nested_namespace_definition(p):
    ''' nested_namespace_definition : NAMESPACE enclosing_namespace_specifier DCOLON inline_opt IDENTIFIER '{' namespace_body '}' '''

def p_enclosing_namespace_specifier(p):
    ''' enclosing_namespace_specifier : IDENTIFIER
                                      | enclosing_namespace_specifier DCOLON inline_opt IDENTIFIER'''

def p_namespace_body(p):
    ''' namespace_body : declaration_seq_opt '''

# 9.8.2 Namespace alias

def p_namespace_alias(p):
    ''' namespace_alias : IDENTIFIER '''

def p_namespace_alias_definition(p):
    ''' namespace_alias_definition : NAMESPACE IDENTIFIER '=' qualified_namespace_specifier ';' '''

def p_nested_name_specifier_opt(p):
    ''' nested_name_specifier_opt : nested_name_specifier
                                  | empty '''

def p_qualified_namespace_specifier(p):
    ''' qualified_namespace_specifier : nested_name_specifier_opt namespace_name '''

# 9.8.3 Using namespace directive

def p_using_directive(p):
    ''' using_directive : attribute_specifier_seq_opt USING NAMESPACE nested_name_specifier_opt namespace_name ';' '''


# 9.9 The using declaration

def p_ellipsis_opt(p):
    ''' p_ellipsis_opt : ELLIPSIS
                       | empty '''

def p_using_declaration(p):
    ''' using_declaration : USING using_declarator_list ';' '''

def p_using_declarator_list(p):
    ''' using_declarator_list : using_declarator ellipsis_opt
                              | using_declarator_list ',' using_declarator ellipsis_opt ''' 

# 9.10 The asm declaration
def p_asm_declaration(p):
    ''' asm_declaration : attribute_specifier_seq_opt ASM '(' STRING_LITERAL ')' ';' '''

# 9.11 Linkage specifications
def p_linkage_specification(p):
    ''' linkage_specification : EXTERN STRING_LITERAL '{' declaration_seq_opt '}'
                              | EXTERN STRING_LITERAL declaration '''


# 9.12 Attributes

# 9.12.1 Attribute syntax and semantics

def p_attribute_specifier_seq(p):
    ''' attribute_specifier_seq : attribute_specifier_seq_opt attribute_specifier '''

def p_attribute_using_prefix_opt(p):
    ''' attribute_using_prefix_opt : attribute_using_prefix
                                   | empty '''

def p_attribute_specifier(p):
    ''' attribute_specifier : '[' '[' attribute_using_prefix_opt attribute_list ']' ']'
                            | alignment_specifier '''

def p_alignment_specifier(p):
    ''' alignment_specifier : ALIGNAS '(' type_id ellipsis_opt ')'
                            | ALIGNAS '(' constant_expression ellipsis_opt ')' '''

def p_attribute_using_prefix(p):
    ''' attribute_using_prefix : using attribute_namespace ':' '''

def attribute_opt(p):
    ''' attribute_opt : attribute
                      | empty '''

def p_attribute_list(p):
    ''' attribute_list : attribute_opt
                       | attribute_list ',' attribute_opt
                       | attribute ELLIPSIS
                       | attribute_list , attribute ELLIPSIS '''

def p_attribute_argument_clause_opt(p):
    ''' attribute_argument_clause_opt : attribute_argument_clause
                                      | empty '''

def p_attribute(p):
    ''' attribute : attribute_token attribute_argument_clause_opt '''

def p_attribute_token(p):
    ''' attribute_token : IDENTIFIER
                        | attribute_scoped_token '''


def p_attribute_scoped_token(p):
    ''' attribute_scoped_token : attribute_namespace DCOLON IDENTIFIER '''


def p_attribute_namespace(p):
    ''' attribute_namespace : IDENTIFIER '''

def p_balanced_token_seq_opt(p):
    ''' balanced_token_seq_opt : balanced_token_seq
                               | empty '''

def p_attribute_argument_clause(p):
    ''' attribute_argument_clause : '(' balanced_token_seq_opt ')' '''

def p_balanced_token_seq(p):
    ''' balanced_token_seq : balanced_token
                           | balanced_token_seq balanced_token '''

def p_balanced_token(p):
    ''' balanced_token : '(' balanced_token_seq_opt ')'
                       | '[' balanced_token_seq_opt ']'
                       | '{' balanced_token_seq_opt '}' '''
    #  any token other than a parenthesis, a bracket, or a brace '''  
    # TODO