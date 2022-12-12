from .myast import InternalNode, ExternalNode

def p_pp_include(p):
    '''
        pp_include : INCLUDE
    '''
    p[0] = ExternalNode('include', p[1])

def p_system_dir(p):
    ''' system_dir : '<' LITERAL '>' '''
    p[2] = ExternalNode('LITERAL',p[2])
    p[0] = InternalNode('system_dir', p[1:])

def p_current_dir(p):
    ''' current_dir : '"' LITERAL '"' '''
    p[2] = ExternalNode('LITERAL',p[2])
    p[0] = InternalNode('current_dir', p[1:])