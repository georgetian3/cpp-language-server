from .myast import Node

'''
try_block:
    try compound_statement handler_seq
function_try_block:
    try ctor_initializeropt compound_statement handler_seq
handler_seq:
    handler handler_seqopt
handler:
    catch ( exception_declaration ) compound_statement
exception_declaration:
    attribute_specifier_seqopt type_specifier_seq declarator
    attribute_specifier_seqopt type_specifier_seq abstract_declaratoropt
    ...
noexcept_specifier:
    noexcept ( constant_expression )
    noexcept
'''
def p_try_block(p):
    '''
        try_block : TRY compound_statement handler_seq
    '''
    p[0] = Node('try_block', '', p[1:])  
def p_function_try_block(p):
    '''
        function_try_block : TRY ctor_initializer_opt compound_statement handler_seq
    '''
    p[0] = Node('function_try_block', '', p[1:])  

def p_handler_seq(p):
    '''
        handler_seq : handler handler_seq_opt 
    '''
    p[0] = Node('handler_seq', '', p[1:])  

def p_handler(p):
    '''
        handler : CATCH '(' exception_declaration ')' compound_statement
    '''
    p[0] = Node('handler', '', p[1:])  

def p_exception_declaration(p):
    '''
        exception_declaration : attribute_specifier_seq_opt type_specifier_seq declarator
                              | attribute_specifier_seq_opt type_specifier_seq abstract_declarator_opt
                              | ELLIPSIS
    '''
    p[0] = Node('exception_declaration', '', p[1:])  

def p_noexcept_specifier(p):
    '''
        noexcept_specifier : NOEXCEPT '(' constant_expression ')'
                           | NOEXCEPT
    '''
    p[0] = Node('noexcept_specifier', '', p[1:])  
