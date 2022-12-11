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
def p_function_try_block(p):
    '''
        function_try_block : TRY ctor_initializer_opt compound_statement handler_seq
    '''
def p_handler_seq(p):
    '''
        handler_seq : handler handler_seq_opt 
    '''
def p_handler(p):
    '''
        handler : CATCH '(' exception_declaration ')' compound_statement
    '''
def p_exception_declaration(p):
    '''
        exception_declaration : attribute_specifier_seq_opt type_specifier_seq declarator
                              | attribute_specifier_seq_opt type_specifier_seq abstract_declarator_opt
                              | ELLIPSIS
    '''
def p_noexcept_specifier(p):
    '''
        noexcept_specifier : NOEXCEPT '(' constant_expression ')'
                           | NOEXCEPT
    '''
