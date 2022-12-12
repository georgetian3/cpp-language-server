from .myast import InternalNode, ExternalNode

def p_pp_include(p):
    ''' pp_include : '#' INCLUDE system_dir
                   | '#' INCLUDE current_dir '''
    p[0] = InternalNode('include', [p[3]])

def p_system_dir(p):
    ''' system_dir : '<' IDENTIFIER '>' '''
    p[2] = ExternalNode('IDENTIFIER',p[2])
    p[0] = InternalNode('system_dir', p[1:])

def p_current_dir(p):
    ''' current_dir : '"' IDENTIFIER '"' '''
    p[2] = ExternalNode('IDENTIFIER',p[2])
    p[0] = InternalNode('current_dir', p[1:])