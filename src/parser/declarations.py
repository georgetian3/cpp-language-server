from .myast import Node

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
    p[0] = Node('declaration_seq', '', p[1:])

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
    p[0] = Node('declaration', '', p[1:])

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
    p[0] = Node('block_declaration', '', p[1:])

def p_nodeclspec_function_declaration(p):
    '''
        nodeclspec_function_declaration : declarator ';'
                                        | attribute_specifier_seq declarator ';'
    '''
    p[0] = Node('nodeclspec_function_declaration', '', p[1:])

def p_alias_declaration(p):
    '''
        alias_declaration : USING IDENTIFIER '=' defining_type_id ';'
                          | USING IDENTIFIER attribute_specifier_seq '=' defining_type_id ';' 
    '''
    p[0] = Node('alias_declaration', '', p[1:])

def p_simple_declaration(p):
    '''
        simple_declaration : decl_specifier_seq init_declarator_list_opt ';'
                           | attribute_specifier_seq decl_specifier_seq init_declarator_list ';'
                           | attribute_specifier_seq_opt decl_specifier_seq ref_qualifier_opt '[' identifier_list ']' initializer ';'
    '''


def p_static_assert_declaration(p):
    '''
        static_assert_declaration : STATIC_ASSERT '(' constant_expression ')' ';'
                                  | STATIC_ASSERT '(' constant_expression ',' string_literal ')' ';'
    '''
    p[0] = Node('static_assert_declaration', '', p[1:])

def p_empty_declaration(p):
    '''
        empty_declaration : ';'
    '''
    p[0] = Node('empty_declaration', '', p[1:])

def p_attribute_declaration(p):
    '''
        attribute_declaration : attribute_specifier_seq ';'
    '''
    p[0] = Node('attribute_declaration', '', p[1:])

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
                       | CONSTEXPR
                       | CONSTEVAL
                       | CONSTINIT
                       | INLINE
    '''
    p[0] = Node('decl_specifier', '', p[1:])

def p_decl_specifier_seq(p):
    '''
        decl_specifier_seq : decl_specifier
                           | decl_specifier attribute_specifier_seq
                           | decl_specifier decl_specifier_seq
    '''
    p[0] = Node('decl_specifier_seq', '', p[1:])

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
    p[0] = Node('storage_class_specifier', '', p[1:])

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
    p[0] = Node('function_specifier', '', p[1:])

def p_explicit_specifier(p):
    '''
        explicit_specifier : EXPLICIT '(' constant_expression ')'
                           | EXPLICIT
    '''
    p[0] = Node('explicit_specifier', '', p[1:])

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
    p[0] = Node('typedef_name', '', p[1:])

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
    p[0] = Node('type_specifier', '', p[1:])

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
    p[0] = Node('defining_type_specifier', '', p[1:])

def p_defining_type_specifier_seq(p):
    '''
        defining_type_specifier_seq : defining_type_specifier
                                    | defining_type_specifier attribute_specifier_seq
                                    | defining_type_specifier defining_type_specifier_seq
    '''
    p[0] = Node('defining_type_specifier_seq', '', p[1:])

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
                              | nested_name_specifier TEMPLATE simple_template_id
                              | decltype_specifier
                              | placeholder_type_specifier
                              | template_name
                              | nested_name_specifier template_name
                              | CHAR
                              | CHAR8_T
                              | CHAR16_T
                              | CHAR32_T
                              | WCHAR_T
                              | BOOL
                              | SHORT
                              | INT
                              | LONG
                              | SIGNED
                              | UNSIGNED
                              | FLOAT
                              | DOUBLE
                              | VOID
    '''
    p[0] = Node('simple_type_specifier', '', p[1:])

def p_decltype_specifier(p):
    ''' decltype_specifier : DECLTYPE '(' expression ')' '''
    p[0] = Node('decltype_specifier', '', p[1:])


def p_type_name(p):
    '''
        type_name : class_name
                  | enum_name
                  | typedef_name
    '''
    p[0] = Node('type_name', '', p[1:])

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
                                  | class_key nested_name_specifier TEMPLATE simple_template_id
                                  | elaborated_enum_specifier
    '''
    p[0] = Node('elaborated_type_specifier', '', p[1:])


def p_elaborated_enum_specifier(p):
    '''
        elaborated_enum_specifier : ENUM nested_name_specifier IDENTIFIER
                                  | IDENTIFIER
    '''
    p[0] = Node('elaborated_enum_specifier', '', p[1:])

'''
placeholder_type_specifier:
    type_constraintopt auto
    type_constraintopt decltype ( auto )
'''

def p_placeholder_type_specifier(p):
    '''
        placeholder_type_specifier : AUTO
                                   | type_constraint AUTO
                                   | DECLTYPE '(' AUTO ')'
                                   | type_constraint DECLTYPE '(' AUTO ')'
    '''

    p[0] = Node('placeholder_type_specifier', '', p[1:])

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
    p[0] = Node('init_declarator_list', '', p[1:])

def p_init_declarator(p):
    '''
        init_declarator : declarator
                        | declarator initializer
                        | declarator requires_clause
    '''
    p[0] = Node('init_declarator', '', p[1:])

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
    p[0] = Node('declarator', '', p[1:])

def p_ptr_declarator(p):
    '''
        ptr_declarator : noptr_declarator
                       | ptr_operator ptr_declarator
    '''
    p[0] = Node('ptr_declarator', '', p[1:])

def p_noptr_declarator(p):
    '''
        noptr_declarator : declarator_id attribute_specifier_seq_opt
                         | noptr_declarator parameters_and_qualifiers
                         | noptr_declarator '[' constant_expression_opt ']' attribute_specifier_seq_opt
                         | '(' ptr_declarator ')'
    '''

    p[0] = Node('noptr_declarator', '', p[1:])

def p_parameters_and_qualifiers(p):
    '''
        parameters_and_qualifiers : '(' parameter_declaration_clause ')' cv_qualifier_seq_opt
                                  | ref_qualifier_opt noexcept_specifier_opt attribute_specifier_seq_opt
    '''
    p[0] = Node('parameters_and_qualifiers', '', p[1:])



def p_trailing_return_type(p):
    '''
       trailing_return_type : ARROW type_id
    '''
    p[0] = Node('trailing_return_type', '', p[1:])

def p_ptr_operator(p):
    '''
        ptr_operator : '*' attribute_specifier_seq_opt cv_qualifier_seq_opt
                     | '&' attribute_specifier_seq_opt
                     | LAND attribute_specifier_seq_opt
                     | nested_name_specifier '*' attribute_specifier_seq_opt cv_qualifier_seq_opt
    '''
    p[0] = Node('ptr_operator', '', p[1:])

def p_cv_qualifier_seq(p):
    '''
        cv_qualifier_seq : cv_qualifier cv_qualifier_seq_opt
    '''
    p[0] = Node('cv_qualifier_seq', '', p[1:])

def p_cv_qualifier(p):
    '''
        cv_qualifier : CONST
                     | VOLATILE 
    '''   
    p[0] = Node('cv_qualifier', '', p[1:])

def p_ref_qualifier(p):
    '''
        ref_qualifier : '&'
                      | LAND
    '''
    p[0] = Node('ref_qualifier', '', p[1:])

def p_declarator_id(p):
    '''
        declarator_id : id_expression
                      | ELLIPSIS id_expression  
    '''
    p[0] = Node('declarator_id', '', p[1:])

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

def p_type_id(p):
    '''
        type_id : type_specifier_seq abstract_declarator_opt
    '''
    p[0] = Node('type_id', '', p[1:])

def p_defining_type_id(p):
    '''
        defining_type_id : defining_type_specifier_seq abstract_declarator_opt
    '''
    p[0] = Node('defining_type_id', '', p[1:])

def p_abstract_declarator(p):
    '''
        abstract_declarator : ptr_abstract_declarator
                            | noptr_abstract_declarator_opt parameters_and_qualifiers trailing_return_type
                            | abstract_pack_declarator
    '''
    p[0] = Node('abstract_declarator', '', p[1:])

def p_noptr_abstract_declarator(p):
    '''
        noptr_abstract_declarator : noptr_abstract_declarator_opt parameters_and_qualifiers
                                  | noptr_abstract_declarator_opt '[' constant_expression_opt ']' attribute_specifier_seq_opt
                                  | '(' ptr_abstract_declarator ')'
    '''
    p[0] = Node('noptr_abstract_declarator', '', p[1:])

def p_abstract_pack_declarator(p):
    '''
        abstract_pack_declarator : noptr_abstract_pack_declarator
                                 | ptr_operator abstract_pack_declarator
    '''
    p[0] = Node('abstract_pack_declarator', '', p[1:])
    
def p_noptr_abstract_pack_declarator(p):
    '''
        noptr_abstract_pack_declarator : noptr_abstract_pack_declarator parameters_and_qualifiers
                                       | noptr_abstract_pack_declarator '[' constant_expression_opt ']' attribute_specifier_seq_opt
                                       | ELLIPSIS
    '''
    p[0] = Node('noptr_abstract_pack_declarator', '', p[1:])


# 9.3.3.5 Functions

def p_parameter_declaration(p):
    ''' parameter_declaration : attribute_specifier_seq_opt decl_specifier_seq declarator 
                              | attribute_specifier_seq_opt decl_specifier_seq declarator '=' initializer_clause
                              | attribute_specifier_seq_opt decl_specifier_seq declarator abstract_declarator_opt
                              | attribute_specifier_seq_opt decl_specifier_seq declarator abstract_declarator_opt '=' initializer_clause
    '''

def p_parameter_declaration_clause(p):
    ''' parameter_declaration_clause : parameter_declaration_list_opt ellipsis_opt
                                     | parameter_declaration_list ',' ELLIPSIS '''
def p_parameter_declaration_list(p):
    ''' parameter_declaration_list : parameter_declaration
                                   | parameter_declaration_list ',' parameter_declaration '''

# 9.4 Initializers

def p_initializer(p):
    ''' initializer : brace_or_equal_initializer
                    | '(' expression_list ')' '''
    p[0] = Node('initializer', '', p[1:])

def p_brace_or_equal_initializer(p):
    ''' brace_or_equal_initializer : '=' initializer_clause
                                   | braced_init_list '''
    p[0] = Node('brace_or_equal_initializer', '', p[1:])


def p_initializer_clause(p):
    ''' initializer_clause : assignment_expression
                           | braced_init_list '''
    p[0] = Node('initializer_clause', '', p[1:])



def p_braced_init_list(p):
    ''' braced_init_list : '{' initializer_list comma_opt '}'
                         | '{' designated_initializer_list comma_opt '}'
                         | '{' '}' '''
    p[0] = Node('braced_init_list', '', p[1:])


def p_initializer_list(p):
    ''' initializer_list : initializer_clause ellipsis_opt
                         | initializer_list ',' initializer_clause ellipsis_opt '''
    p[0] = Node('initializer_list', '', p[1:])


def p_designated_initializer_list(p):
    ''' designated_initializer_list : designated_initializer_clause       
                                    | designated_initializer_list ',' designated_initializer_clause '''
    p[0] = Node('designated_initializer_list', '', p[1:])

def p_designated_initializer_clause(p):
    ''' designated_initializer_clause : designator brace_or_equal_initializer '''
    p[0] = Node('designated_initializer_clause', '', p[1:])

def p_designator(p):
    ''' designator : '.' IDENTIFIER '''
    p[0] = Node('designator', '', p[1:])

def p_expr_or_braced_init_list(p):
    ''' expr_or_braced_init_list : expression
                                 | braced_init_list '''
    p[0] = Node('expr_or_braced_init_list', '', p[1:])

# 9.5 Function definitions

# 9.5.1 In general



def p_function_definition(p):
    ''' function_definition : attribute_specifier_seq_opt decl_specifier_seq_opt declarator virt_specifier_seq_opt function_body
                            | attribute_specifier_seq_opt decl_specifier_seq_opt declarator requires_clause function_body '''
    p[0] = Node('function_definition', '', p[1:])


def p_function_body(p):
    ''' function_body : ctor_initializer_opt compound_statement
                      | function_try_block
                      | '=' DEFAULT ';'
                      | '=' DELETE ';' '''
    p[0] = Node('function_body', '', p[1:])
# 9.6 Structured binding declarations

# 9.7 Enumerations

# 9.7.1 Enumeration declarations

def p_enum_name(p):
    ''' enum_name : IDENTIFIER '''
    p[0] = Node('enum_name', '', p[1:])

def p_enum_specifier(p):
    ''' enum_specifier : enum_head '{' enumerator_list_opt '}'
                       | enum_head '{' enumerator_list ',' '}' '''
    p[0] = Node('enum_specifier', '', p[1:])



def p_enum_head(p):
    ''' enum_head : enum_key attribute_specifier_seq_opt enum_head_name_opt enum_base_opt '''
    p[0] = Node('enum_head', '', p[1:])

def p_enum_head_name(p):
    ''' enum_head_name : nested_name_specifier_opt IDENTIFIER '''
    p[0] = Node('enum_head_name', '', p[1:])

def p_opaque_enum_declaration(p):
    ''' opaque_enum_declaration : enum_key attribute_specifier_seq_opt enum_head_name enum_base_opt ';' '''
    p[0] = Node('opaque_enum_declaration', '', p[1:])

def p_enum_key(p):
    ''' enum_key : ENUM
                 | ENUM CLASS
                 | ENUM STRUCT '''
    p[0] = Node('enum_key', '', p[1:])

def p_enum_base(p):
    ''' enum_base : ':' type_specifier_seq '''
    p[0] = Node('enum_base', '', p[1:])

    
def p_enumerator_list(p):
    ''' enumerator_list : enumerator_definition
                        | enumerator_list ',' enumerator_definition '''
    p[0] = Node('enumerator_list', '', p[1:])

def p_enumerator_definition(p):
    ''' enumerator_definition : enumerator
                              | enumerator '=' constant_expression '''
    p[0] = Node('enumerator_definition', '', p[1:])

def p_enumerator(p):
    ''' enumerator : IDENTIFIER attribute_specifier_seq_opt '''
    p[0] = Node('enumerator', '', p[1:])

# 9.7.2 The using enum declaration
 
def p_using_enum_declaration(p):
    ''' using_enum_declaration : USING elaborated_enum_specifier ';' '''
    p[0] = Node('using_enum_declaration', '', p[1:])


# 9.8 Namespaces

# 9.8.1 Namespace definition

def p_namespace_name(p):
    ''' namespace_name : IDENTIFIER
                       | namespace_alias '''
    p[0] = Node('namespace_name', '', p[1:])


def p_namespace_definition(p):
    ''' namespace_definition : named_namespace_definition
                             | unnamed_namespace_definition
                             | nested_namespace_definition '''
    p[0] = Node('namespace_definition', '', p[1:])



def p_named_namespace_definition(p):
    ''' named_namespace_definition : inline_opt NAMESPACE attribute_specifier_seq_opt IDENTIFIER '{' namespace_body '}' '''
    p[0] = Node('named_namespace_definition', '', p[1:])

def p_unnamed_namespace_definition(p):
    ''' unnamed_namespace_definition : inline_opt NAMESPACE attribute_specifier_seq_opt '{' namespace_body '}' '''
    p[0] = Node('unnamed_namespace_definition', '', p[1:])

def p_nested_namespace_definition(p):
    ''' nested_namespace_definition : NAMESPACE enclosing_namespace_specifier DCOLON inline_opt IDENTIFIER '{' namespace_body '}' '''
    p[0] = Node('nested_namespace_definition', '', p[1:])

def p_enclosing_namespace_specifier(p):
    ''' enclosing_namespace_specifier : IDENTIFIER
                                      | enclosing_namespace_specifier DCOLON inline_opt IDENTIFIER'''
    p[0] = Node('enclosing_namespace_specifier', '', p[1:])

def p_namespace_body(p):
    ''' namespace_body : declaration_seq_opt '''
    p[0] = Node('namespace_body', '', p[1:])

# 9.8.2 Namespace alias

def p_namespace_alias(p):
    ''' namespace_alias : IDENTIFIER '''
    p[0] = Node('namespace_alias', '', p[1:])

def p_namespace_alias_definition(p):
    ''' namespace_alias_definition : NAMESPACE IDENTIFIER '=' qualified_namespace_specifier ';' '''
    p[0] = Node('namespace_alias_definition', '', p[1:])



def p_qualified_namespace_specifier(p):
    ''' qualified_namespace_specifier : nested_name_specifier_opt namespace_name '''
    p[0] = Node('qualified_namespace_specifier', '', p[1:])

# 9.8.3 Using namespace directive

def p_using_directive(p):
    ''' using_directive : attribute_specifier_seq_opt USING NAMESPACE nested_name_specifier_opt namespace_name ';' '''
    p[0] = Node('using_directive', '', p[1:])


# 9.9 The using declaration



def p_using_declaration(p):
    ''' using_declaration : USING using_declarator_list ';' '''
    p[0] = Node('using_declaration', '', p[1:])

def p_using_declarator_list(p):
    ''' using_declarator_list : using_declarator ellipsis_opt
                              | using_declarator_list ',' using_declarator ellipsis_opt ''' 
    p[0] = Node('using_declarator_list', '', p[1:])

# 9.10 The asm declaration
def p_asm_declaration(p):
    ''' asm_declaration : attribute_specifier_seq_opt ASM '(' STRING_LITERAL ')' ';' '''
    p[0] = Node('asm_declaration', '', p[1:])

# 9.11 Linkage specifications
def p_linkage_specification(p):
    ''' linkage_specification : EXTERN STRING_LITERAL '{' declaration_seq_opt '}'
                              | EXTERN STRING_LITERAL declaration '''
    p[0] = Node('linkage_specification', '', p[1:])


# 9.12 Attributes

# 9.12.1 Attribute syntax and semantics

def p_attribute_specifier_seq(p):
    ''' attribute_specifier_seq : attribute_specifier_seq_opt attribute_specifier '''
    p[0] = Node('attribute_specifier_seq', '', p[1:])



def p_attribute_specifier(p):
    ''' attribute_specifier : '[' '[' attribute_using_prefix_opt attribute_list ']' ']'
                            | alignment_specifier '''
    p[0] = Node('attribute_specifier', '', p[1:])

def p_alignment_specifier(p):
    ''' alignment_specifier : ALIGNAS '(' type_id ellipsis_opt ')'
                            | ALIGNAS '(' constant_expression ellipsis_opt ')' '''
    p[0] = Node('alignment_specifier', '', p[1:])

def p_attribute_using_prefix(p):
    ''' attribute_using_prefix : USING attribute_namespace ':' '''
    p[0] = Node('attribute_using_prefix', '', p[1:])


def p_attribute_list(p):
    ''' attribute_list : attribute_opt
                       | attribute_list ',' attribute_opt
                       | attribute ELLIPSIS
                       | attribute_list ',' attribute ELLIPSIS '''
    p[0] = Node('attribute_list', '', p[1:])


def p_attribute(p):
    ''' attribute : attribute_token attribute_argument_clause_opt '''
    p[0] = Node('attribute', '', p[1:])

def p_attribute_token(p):
    ''' attribute_token : IDENTIFIER
                        | attribute_scoped_token '''
    p[0] = Node('attribute_token', '', p[1:])

def p_attribute_namespace(p):
    ''' attribute_namespace : IDENTIFIER '''
    p[0] = Node('attribute_namespace', '', p[1:])

def p_attribute_scoped_token(p):
    ''' attribute_scoped_token : attribute_namespace DCOLON IDENTIFIER '''
    p[0] = Node('attribute_scoped_token', '', p[1:])



def p_attribute_argument_clause(p):
    ''' attribute_argument_clause : '(' balanced_token_seq_opt ')' '''
    p[0] = Node('attribute_argument_clause', '', p[1:])

def p_balanced_token_seq(p):
    ''' balanced_token_seq : balanced_token
                           | balanced_token_seq balanced_token '''
    p[0] = Node('balanced_token_seq', '', p[1:])

def p_balanced_token(p):
    ''' balanced_token : '(' balanced_token_seq_opt ')'
                       | '[' balanced_token_seq_opt ']'
                       | '{' balanced_token_seq_opt '}' '''
    #  any token other than a parenthesis, a bracket, or a brace '''  
    # TODO
    p[0] = Node('balanced_token', '', p[1:])


def p_explicit_specialization(p):
    ''' explicit_specialization : TEMPLATE '<' '>' declaration '''