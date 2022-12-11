from .myast import Node

'''
modules declaration

module-declaration:
    export-keywordopt module-keyword module-name module-partitionopt attribute-specifier-seqopt ;
module-name:
    module-name-qualifieropt identifier
module-partition:
    : module-name-qualifieropt identifier
module-name-qualifier:
    identifier .
    module-name-qualifier identifier .
export-declaration:
    export declaration
    export { declaration-seqopt }
    export-keyword module-import-declaration
module-import-declaration:
    import-keyword module-name attribute-specifier-seqopt ;
    import-keyword module-partition attribute-specifier-seqopt ;
    import-keyword header-name attribute-specifier-seqopt ;
global-module-fragment:
    module-keyword ; declaration-seqopt
private-module-fragment:
    module-keyword : private ; declaration-seqopt
'''

def p_module_declaration(p):
    '''
    module_declaration : export_keyword module_keyword module_name module_partition attribute_specifier_seq
                       | export_keyword module_keyword module_name module_partition
                       | export_keyword module_keyword module_name
                       | module_keyword module_name module_partition attribute_specifier_seq
                       | module_keyword module_name module_partition
                       | module_keyword module_name attribute_specifier_seq
                       | export_keyword module_keyword module_name attribute_specifier_seq
                       | module_keyword module_name
    '''
    p[0] = Node('module_declaration', '', p[1:])

def p_module_name(p):
    '''
    module_name : module_name_qualifier IDENTIFIER
                | IDENTIFIER
    '''
    p[0] = Node('module_name', '', p[1:])

def p_module_partition(p):
    '''
    module_partition : ':' module_name_qualifier IDENTIFIER
                     | ':' IDENTIFIER
    '''
    p[0] = Node('module_partition', '', p[1:])

def p_module_name_qualifier(p):
    '''
    module_name_qualifier : IDENTIFIER '.'
                          | module_name_qualifier IDENTIFIER '.'
    '''
    p[0] = Node('module_name_qualifier', '', p[1:])

def p_export_declaration(p):
    '''
    export_declaration : EXPORT declaration
                       | EXPORT '{' declaration_seq '}'
                       | EXPORT '{' '}'
                       | export_keyword module_import_declaration
    '''
    p[0] = Node('export_declaration', '', p[1:])

def p_module_import_declaration(p):
    '''
    module_import_declaration : import_keyword module_name attribute_specifier_seq ';'
                              | import_keyword module_name ';'
                              | import_keyword module_partition attribute_specifier_seq ';'
                              | import_keyword module_partition ';'
                              | import_keyword header_name attribute_specifier_seq ';'
                              | import_keyword header_name ';'
    '''
    p[0] = Node('module_import_declaration', '', p[1:])

def p_global_module_fragment(p):
    '''
    global_module_fragment : module_keyword ';' declaration_seq
                           | module_keyword ';'
    '''
    p[0] = Node('global_module_fragment', '', p[1:])

def p_private_module_fragment(p):
    '''
    private_module_fragment : module_keyword ':' PRIVATE ';' declaration_seq
                            | module_keyword ':' PRIVATE ';'
    '''
    p[0] = Node('private_module_fragment', '', p[1:])