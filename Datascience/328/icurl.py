import ply.lex as lex
import ply.yacc as yacc
import graphviz
import uuid
from graphviz import Digraph
import icurl


tokens = (
    'IDENTIFIER',
    'KEYWORD',
    'NUMBER',
    'OPERATOR',
    'DELIMITER',
    'STRING',
    'COMMENT',
    'IF',
    'ELSE',
    'PRINT',
)


t_ignore = ' \t\n\r' # ignore whitespace and tabs


def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    keywords = {'int', 'if', 'else', 'while', 'print'}
    t.type = 'KEYWORD' if t.value in keywords else 'IDENTIFIER'
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_OPERATOR(t):
    r'[\+\-\*/=<>\!]=?|!='
    return t


def t_DELIMITER(t):
    r'[;,\(\)\[\]\{\}]'
    return t




def t_STRING(t):
    r'"[^"]*"'
    return t


def t_COMMENT(t):
    r'\#.*'
    pass # ignore comments


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# Parser rules
def p_program(p):
    '''program : statement_list'''
    p[0] = ('PROGRAM', p[1])


def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_statement(p):
    '''statement : expression_statement
                 | var_declaration
                 | if_statement
                 | print_statement'''
    p[0] = p[1]


def p_expression_statement(p):
    '''expression_statement : expression DELIMITER'''
    p[0] = ('EXPRESSION_STATEMENT', p[1])


def p_expression(p):
    '''expression : primary_expression
                  | binary_expression'''
    p[0] = p[1]


def p_primary_expression(p):
    '''primary_expression : IDENTIFIER
                          | NUMBER
                          | STRING'''
    p[0] = ('PRIMARY_EXPRESSION', p[1])


def p_if_statement(p):
    '''if_statement : IF expression '{' statement_list '}'
                    | IF expression '{' statement_list '}' ELSE '{' statement_list '}' '''
    if len(p) == 9:
        p[0] = ('IF_ELSE_STATEMENT', p[2], p[4], p[8])
    else:
        p[0] = ('IF_STATEMENT', p[2], p[4])






def p_print_statement(p):
    '''print_statement : PRINT '(' expression ')' DELIMITER'''
    p[0] = ('PRINT_STATEMENT', p[3])




def p_binary_expression(p):
    '''binary_expression : expression OPERATOR expression'''
    p[0] = ('BINARY_EXPRESSION', p[2], p[1], p[3])


def p_var_declaration(p):
    '''var_declaration : KEYWORD IDENTIFIER '=' expression DELIMITER'''
    p[0] = ('VAR_DECLARATION', p[1], p[2], p[4])


def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: unexpected token '{p.value}' of type '{p.type}'")
    else:
        print("Syntax error: unexpected end of input")


parser = yacc.yacc()


# Test the parser
data = '''
#this is a comment
x=5+2+3;
IF (x < 18)
    PRINT("You can`t vote")


ELSE (x==18)
    PRINT("You can Vote")


'''

lexer.input(data)
# for token in lexer:
    # print(token.type, token.value)




result = yacc.parse(data)

