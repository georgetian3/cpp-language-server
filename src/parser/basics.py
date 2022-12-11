from .myast import Node
def p_translation_unit(p):
    ''' translation_unit : declaration_seq_opt
                         | global_module_fragment_opt module_declaration declaration_seq_opt private_module_fragment_opt '''