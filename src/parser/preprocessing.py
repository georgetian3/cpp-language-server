'''
preprocessing_file :
    groupopt
    module_file
module_file:
    pp_global_module_fragmentopt pp_module groupopt pp_private_module_fragmentopt
pp_global_module_fragment:
    module ; new_line groupopt
pp_private_module_fragment:
    module : private ; new_line groupopt
group:
    group_part
    group group_part
group_part:
    control_line
    if_section
    text_line
    # conditionally_supported_directive
'''
def p_preprocessing_file(p):
    '''
        preprocessing_file : group_opt
                           | module_file
    '''
def p_module_file(p):
    '''
        module_file : pp_global_module_fragment_opt pp_module group_opt pp_private_module_fragment_opt
    '''
def p_pp_global_module_fragment(p):
    '''
        pp_global_module_fragment : MODULE ';' new_line group_opt
    '''
def p_pp_private_module_fragment(p):
    '''
        pp_private_module_fragment : MODULE PRIVATE ';' new_line group_opt
    '''    
def p_group(p):
    '''
        group : group_part
              | group group_part
    '''
def p_group_part(p):
    '''
        group_part : control_line
                   | if_section
                   | text_line
                   | '#' conditionally_supported_directive       
    '''
'''
control_line:
    # include pp_tokens new_line
    pp_import
    # define identifier replacement_list new_line
    # define identifier lparen identifier_listopt ) replacement_list new_line
    # define identifier lparen ... ) replacement_list new_line
    # define identifier lparen identifier_list , ... ) replacement_list new_line
    # undef identifier new_line
    # line pp_tokens new_line
    # error pp_tokensopt new_line
    # pragma pp_tokensopt new_line
    # new_line
if_section:
    if_group elif_groupsopt else_groupopt endif_line
if_group:
    # if constant_expression new_line groupopt
    # ifdef identifier new_line groupopt
    # ifndef identifier new_line groupopt
'''
def p_control_line(p):
    '''
        control_line : '#' INCLUDE pp_tokens new_line
                     | pp_import
                     | '#' DEFINE IDENTIFIER replacement_list new_line
                     | '#' DEFINE IDENTIFIER lparen identifier_list_opt ')' replacement_list new_line
                     | '#' DEFINE IDENTIFIER lparen ELLIPSIS ')' replacement_list new_line
                     | '#' DEFINE IDENTIFIER lparen identifier_list ',' ELLIPSIS ')' replacement_list new_line
                     | '#' UNDEF IDENTIFIER new_line
                     | '#' LINE pp_tokens new_line
                     | '#' ERROR pp_tokens_opt new_line
                     | '#' PRAGMA pp_tokens_opt new_line
                     | '#' new_line
    '''
def p_if_section(p):
    '''
        if_section : if_group elif_groups_opt else_group_opt endif_line
    '''
def p_if_group(p):
    '''
        if_group : '#' IF constant_expression new_line group_opt
                 | '#' IFDEF IDENTIFIER new_line group_opt
                 | '#' IFNDEF IDENTIFIER new_line group_opt
    '''
'''
elif_groups:
    elif_group
    elif_groups elif_group
elif_group:
    # elif constant_expression new_line groupopt
else_group:
    # else new_line groupopt
endif_line:
    # endif new_line
text_line:
    pp_tokensopt new_line
conditionally_supported_directive :
    pp_tokens new_line
lparen:
    a ( character not immediately preceded by white_space
identifier_list:
    identifier
    identifier_list , identifier
replacement_list:
    pp_tokensopt
pp_tokens:
    preprocessing_token
    pp_tokens preprocessing_token
'''
def p_elif_groups(p):
    '''
        elif_groups : elif_group
                    | elif_groups elif_group
    '''
def p_elif_group(p):
    '''
        elif_group : '#' ELIF constant_expression new_line group_opt
    '''
def p_else_group(p):
    '''
        else_group : "#" ELSE new_line group_opt
    '''
def p_lparen(p):
    '''
        lparen : '('
    '''
def p_endif_line(p):
    '''
        endif_line : '#' ENDIF new_line
    '''
def p_text_line(p):
    '''
        text_line : pp_tokens_opt new_line
    '''
def p_conditionally_supported_directive(p):
    '''
        conditionally_supported_directive : pp_tokens new_line
    '''
def p_identifier_list(p):
    '''
        identifier_list : IDENTIFIER
                        | identifier_list ',' IDENTIFIER   
    '''

def p_replacement_list(p):
    '''
        replacement_list : pp_tokens_opt
    '''
def p_pp_tokens(p):
    '''
        pp_tokens : preprocessing_token
                  | pp_tokens preprocessing_token
    '''

'''
new_line:
    the new_line character
defined_macro_expression:
    defined identifier
    defined ( identifier )
h_preprocessing_token:
    any preprocessing_token other than >
h_pp_tokens:
    h_preprocessing_token
    h_pp_tokens h_preprocessing_token
header_name_tokens:
    string_literal
    < h_pp_tokens >
has_include_expression:
    __has_include ( header_name )
    __has_include ( header_name_tokens )
has_attribute_expression:
    __has_cpp_attribute ( pp_tokens )
pp_module:
    exportopt module pp_tokensopt ; new_line
pp_import:
    exportopt import header_name pp_tokensopt ; new_line
    exportopt import header_name_tokens pp_tokensopt ; new_line
    exportopt import pp_tokens ; new_line
va_opt_replacement:
    __VA_OPT__ ( pp_tokensopt )
'''
def p_new_line(p):
    '''
        new_line :
    '''
def p_defined_macro_expression(p):
    '''
        defined_macro_expression : DEFINED IDENTIFIER
                                 | DEFINED '(' IDENTIFIER ')'
    '''
