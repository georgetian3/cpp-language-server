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
    ''' designator : '.' identifier '''

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