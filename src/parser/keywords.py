from .myast import InternalNode, ExternalNode

def p_import_keyword(p):
    '''
        import_keyword : IMPORT
    '''
    p[0] = ExternalNode('import_keyword', p[1:])  
def p_export_keyword(p):
    '''
        export_keyword : EXPORT
    '''
    p[0] = ExternalNode('export_keyword', p[1:])  
def p_module_keyword(p):
    '''
        module_keyword : MODULE
    '''
    p[0] = ExternalNode('module_keyword', p[1:])  
