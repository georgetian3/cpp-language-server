from .myast import InternalNode, ExternalNode
def p_translation_unit(p):
    ''' translation_unit : declaration_seq_opt '''
                         #| global_module_fragment_opt module_declaration declaration_seq_opt private_module_fragment_opt'''
    p[0] = InternalNode('translation_unit', p[1:])