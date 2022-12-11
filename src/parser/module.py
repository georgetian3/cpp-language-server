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
    module_declaration  :   export_keyword module_keyword module_name module_partition attribute_specifier_seq
                        |   export_keyword module_keyword module_name module_partition
                        |   export_keyword module_keyword module_name attribute_specifier_seq
                        |   export_keyword module_keyword module_name
                        |   module_keyword module_name module_partition attribute_specifier_seq
                        |   module_keyword module_name module_partition
                        |   export_keywordopt module_keyword module_name attribute_specifier_seq
                        |   export_keywordopt module_keyword module_name
    '''

def p_module_name(p):
    '''
    module_name :   module_name_qualifier identifier
                |   identifier
    '''

def p_module_partition(p):
    '''
    module_partition    :   ':' module_name_qualifier identifier
                        |   ':' identifier
    '''

def p_module_name_qualifier(p):
    '''
    module_name_qualifier   :   identifier '.'
                            |   module_name_qualifier identifier '.'
    '''

def p_export_declaration(p):
    '''
        export_declaration  :   "export" declaration
                            |   "export" '{' declaration_seq '}'
                            |   "export" '{' '}'
                            |   export_keyword module_import_declaration
    '''

def p_module_import_declaration(p):
    '''
        module_import_declaration   :   import_keyword module_name attribute_specifier_seq ';'
                                    |   import_keyword module_name ';'
                                    |   import_keyword module_partition attribute_specifier_seq ';'
                                    |   import_keyword module_partition ';'
                                    |   import_keyword header_name attribute_specifier_seq ';'
                                    |   import_keyword header_name ';'
    '''

def p_global_module_fragment(p):
    '''
        global_module_fragment  :   module_keyword ';' declaration_seq
                                |   module_keyword ';'
    '''

def p_private_module_fragment(p):
    '''
        private_module_fragment :   module_keyword ':' "private" ';' declaration_seq
                                |   module_keyword ':' "private" ';'
            
    '''