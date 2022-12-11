from .myast import Node

'''
class declaration 

class_name:
    identifier
    simple_template_id
class_specifier:
    class_head { member_specificationopt }
class_head:
    class_key attribute_specifier_seqopt class_head_name class_virt_specifieropt base_clauseopt
    class_key attribute_specifier_seqopt base_clauseopt
class_head_name:
    nested_name_specifieropt class_name
class_virt_specifier:
    "final"
class_key:
    "class"
    "struct"
    "union"
member_specification:
    member_declaration member_specificationopt
    access_specifier ':' member_specificationopt
member_declaration:
    attribute_specifier_seqopt decl_specifier_seqopt member_declarator_listopt ;
    function_definition
    using_declaration
    using_enum_declaration
    static_assert_declaration
    template_declaration
    explicit_specialization
    deduction_guide
    alias_declaration
    opaque_enum_declaration
    empty_declaration
member_declarator_list:
    member_declarator
    member_declarator_list ',' member_declarator
member_declarator:
    declarator virt_specifier_seqopt pure_specifieropt
    declarator requires_clause
    declarator brace_or_equal_initializeropt
    identifieropt attribute_specifier_seqopt ':' constant_expression brace_or_equal_initializeropt
virt_specifier_seq:
    virt_specifier
    virt_specifier_seq virt_specifier
virt_specifier:
    "override"
    "final"
pure_specifier:
    '=' '0'
conversion_function_id:
    operator conversion_type_id
conversion_type_id:
    type_specifier_seq conversion_declaratoropt
conversion_declarator:
    ptr_operator conversion_declaratoropt
base_clause:
    ':' base_specifier_list
base_specifier_list:
    base_specifier "..."opt
    base_specifier_list ',' base_specifier "..."opt
base_specifier:
    attribute_specifier_seqopt class_or_decltype
    attribute_specifier_seqopt virtual access_specifieropt class_or_decltype
    attribute_specifier_seqopt access_specifier virtualopt class_or_decltype
class_or_decltype:
    nested_name_specifieropt type_name
    nested_name_specifier template simple_template_id
    decltype_specifier
access_specifier:
    "private"
    "protected"
    "public"
ctor_initializer:
    ':' mem_initializer_list
mem_initializer_list:
    mem_initializer "..."opt
    mem_initializer_list ',' mem_initializer "..."opt
mem_initializer:
    mem_initializer_id '(' expression_listopt ')'
    mem_initializer_id braced_init_list
mem_initializer_id:
    class_or_decltype
    identifier
'''

def p_class_name(p):
    '''
    class_name : IDENTIFIER
               | simple_template_id
    '''
    p[0] = Node('class_name', '', p[1:])



def p_class_specifier(p):
    '''
    class_specifier : class_head '{' member_specification_opt '}'
    '''
    p[0] = Node('class_specifier', '', p[1:])



def p_class_head(p):
    '''
    class_head : class_key attribute_specifier_seq_opt class_head_name class_virt_specifier_opt base_clause_opt
               | class_key attribute_specifier_seq_opt base_clause_opt
        
    '''
    p[0] = Node('class_head', '', p[1:])



def p_class_head_name(p):
    '''
    class_head_name : nested_name_specifier_opt class_name
    '''
    p[0] = Node('class_head_name', '', p[1:])

def p_class_virt_specifier(p):
    '''
    class_virt_specifier : FINAL
    '''
    p[0] = Node('class_virt_specifier', '', p[1:])

def p_class_key(p):
    '''
    class_key : CLASS
              | STRUCT
              | UNION
    '''
    p[0] = Node('class_key', '', p[1:])



def p_member_specification(p):
    '''
    member_specification : member_declaration member_specification_opt
                         | access_specifier ':' member_specification_opt
    '''
    p[0] = Node('member_specification', '', p[1:])



def p_member_declaration(p):
    '''
    member_declaration : attribute_specifier_seq_opt decl_specifier_seq_opt member_declarator_list_opt ';'
                       | function_definition
                       | using_declaration
                       | using_enum_declaration
                       | static_assert_declaration
                       | template_declaration
                       | explicit_specialization
                       | deduction_guide
                       | alias_declaration
                       | opaque_enum_declaration
                       | empty_declaration
    '''
    p[0] = Node('member_declaration', '', p[1:])

def p_member_declarator_list(p):
    '''
    member_declarator_list : member_declarator
                           | member_declarator_list ',' member_declarator
    '''
    p[0] = Node('member_declarator_list', '', p[1:])





def p_member_declarator(p):
    '''
    member_declarator : declarator virt_specifier_seq_opt pure_specifier_opt
                      | declarator requires_clause
                      | declarator brace_or_equal_initializer_opt
                      | identifier_opt attribute_specifier_seq_opt ':' constant_expression brace_or_equal_initializer_opt
    '''
    p[0] = Node('member_declarator', '', p[1:])

# note left end recursion

def p_virt_specifier_seq(p):
    '''
    virt_specifier_seq : virt_specifier
                       | virt_specifier_seq virt_specifier
    '''
    p[0] = Node('virt_specifier_seq', '', p[1:])

def p_virt_specifier(p):
    '''
    virt_specifier : OVERRIDE
                   | FINAL
    '''
    p[0] = Node('virt_specifier', '', p[1:])

def p_pure_specifier(p):
    '''
    pure_specifier : '=' '0'
    '''
    p[0] = Node('p_pure_specifier', '', p[1:])

def p_conversion_function_id(p):
    '''
    conversion_function_id : OPERATOR conversion_type_id
    '''
    p[0] = Node('conversion_function_id', '', p[1:])



def p_conversion_type_id(p):
    '''
    conversion_type_id : type_specifier_seq conversion_declarator_opt
    '''
    p[0] = Node('conversion_type_id', '', p[1:])

def p_conversion_declarator(p):
    '''
    conversion_declarator : ptr_operator conversion_declarator_opt
    '''
    p[0] = Node('conversion_declarator', '', p[1:])

def p_base_clause(p):
    '''
    base_clause : ':' base_specifier_list
    '''
    p[0] = Node('base_clause', '', p[1:])



def p_base_specifier_list(p):
    '''
    base_specifier_list : base_specifier ellipsis_opt
                        | base_specifier_list ',' base_specifier ellipsis_opt
    '''
    p[0] = Node('base_specifer_list', '', p[1:])



def p_base_specifier(p):
    '''
    base_specifier : attribute_specifier_seq_opt class_or_decltype
                   | attribute_specifier_seq_opt VIRTUAL access_specifier_opt class_or_decltype
                   | attribute_specifier_seq_opt access_specifier virtual_opt class_or_decltype
    '''
    p[0] = Node('base_specifier', '', p[1:])

def p_class_or_decltype(p):
    '''
    class_or_decltype : nested_name_specifier_opt type_name
                      | nested_name_specifier TEMPLATE simple_template_id
                      | decltype_specifier
    '''
    p[0] = Node('class_or_decltype', '', p[1:])

def p_access_specifier(p):
    '''
    access_specifier : PRIVATE
                     | PROTECTED
                     | PUBLIC
    '''
    p[0] = Node('access_specifier', '', p[1:])

def p_ctor_initializer(p):
    '''
    ctor_initializer : ':' mem_initializer_list
    '''
    p[0] = Node('ctor_initializer', '', p[1:])

def p_mem_initializer_list(p):
    '''
    mem_initializer_list : mem_initializer ellipsis_opt
                         | mem_initializer_list ',' mem_initializer ellipsis_opt
    '''
    p[0] = Node('member_initializer_list', '', p[1:])




def p_mem_initializer(p):
    '''
    mem_initializer : mem_initializer_id '(' expression_list_opt ')'
                    | mem_initializer_id braced_init_list
    '''
    p[0] = Node('mem_initializer', '', p[1:])

def p_mem_initializer_id(p):
    '''
    mem_initializer_id : class_or_decltype
                       | IDENTIFIER
    '''
    p[0] = Node('mem_initializer_id', '', p[1:])