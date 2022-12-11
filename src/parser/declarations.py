from .myast import Node

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

def p_comma_opt(p):
    ''' comma_opt : ','
                  | empty '''
    p[0] = Node('comma_opt', '', p[1:])

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
    ''' designator : '.' identifier '''
    p[0] = Node('designator', '', p[1:])

def p_expr_or_braced_init_list(p):
    ''' expr_or_braced_init_list : expression
                                 | braced_init_list '''
    p[0] = Node('expr_or_braced_init_list', '', p[1:])

# 9.5 Function definitions

# 9.5.1 In general


def p_decl_specifier_seq_opt(p):
    ''' decl_specifier_seq_opt : decl_specifier_seq
                               | empty '''
    p[0] = Node('decl_specifier_seq_opt', '', p[1:])
def p_virt_specifier_seq_opt(p):
    ''' virt_specifier_seq_opt : virt_specifier_seq
                               | empty '''
    p[0] = Node('virt_specifier_seq_opt', '', p[1:])
def p_function_definition(p):
    ''' function_definition : attribute_specifier_seq_opt decl_specifier_seq_opt declarator virt_specifier_seq_opt function_body
                            | attribute_specifier_seq_opt decl_specifier_seq_opt declarator requires_clause function_body '''
    p[0] = Node('function_definition', '', p[1:])

def p_ctor_initializer_opt(p):
    ''' ctor_initializer_opt : ctor_initializer
                             | empty '''
    p[0] = Node('ctor_initializer_opt', '', p[1:])
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

def p_nested_name_specifier_opt(p):
    ''' nested_name_specifier_opt : nested_name_specifier
                                  | empty '''
    p[0] = Node('nested_name_specifier_opt', '', p[1:])

def p_qualified_namespace_specifier(p):
    ''' qualified_namespace_specifier : nested_name_specifier_opt namespace_name '''
    p[0] = Node('qualified_namespace_specifier', '', p[1:])

# 9.8.3 Using namespace directive

def p_using_directive(p):
    ''' using_directive : attribute_specifier_seq_opt USING NAMESPACE nested_name_specifier_opt namespace_name ';' '''
    p[0] = Node('using_directive', '', p[1:])


# 9.9 The using declaration

def p_ellipsis_opt(p):
    ''' ellipsis_opt : ELLIPSIS
                       | empty '''
    p[0] = Node('ellipsis_opt', '', p[1:])

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

def p_attribute_using_prefix_opt(p):
    ''' attribute_using_prefix_opt : attribute_using_prefix
                                   | empty '''
    p[0] = Node('attribute_using_prefix_opt', '', p[1:])

def p_attribute_specifier(p):
    ''' attribute_specifier : '[' '[' attribute_using_prefix_opt attribute_list ']' ']'
                            | alignment_specifier '''
    p[0] = Node('attribute_specifier', '', p[1:])

def p_alignment_specifier(p):
    ''' alignment_specifier : ALIGNAS '(' type_id ellipsis_opt ')'
                            | ALIGNAS '(' constant_expression ellipsis_opt ')' '''
    p[0] = Node('alignment_specifier', '', p[1:])

def p_attribute_using_prefix(p):
    ''' attribute_using_prefix : using attribute_namespace ':' '''
    p[0] = Node('attribute_using_prefix', '', p[1:])

def attribute_opt(p):
    ''' attribute_opt : attribute
                      | empty '''
    p[0] = Node('attribute_opt', '', p[1:])

def p_attribute_list(p):
    ''' attribute_list : attribute_opt
                       | attribute_list ',' attribute_opt
                       | attribute ELLIPSIS
                       | attribute_list ',' attribute ELLIPSIS '''
    p[0] = Node('attribute_list', '', p[1:])

def p_attribute_argument_clause_opt(p):
    ''' attribute_argument_clause_opt : attribute_argument_clause
                                      | empty '''
    p[0] = Node('attribute_argument_clause_opt', '', p[1:])

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


def p_balanced_token_seq_opt(p):
    ''' balanced_token_seq_opt : balanced_token_seq
                               | empty '''
    p[0] = Node('balanced_token_seq_opt', '', p[1:])

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
