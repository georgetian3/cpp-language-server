from .myast import InternalNode, ExternalNode

def p_pp_include(p):
    ''' pp_include : '#' INCLUDE system_dir
                   | '#' INCLUDE current_dir '''
    p[0] = InternalNode('include', [p[3]])

def p_system_dir(p):
    ''' system_dir : '<' IDENTIFIER '>' '''
    p[0] = ExternalNode('system_dir', p[2])

def p_current_dir(p):
    ''' current_dir : '"' IDENTIFIER '"' '''
    p[0] = ExternalNode('current_dir', p[2])
