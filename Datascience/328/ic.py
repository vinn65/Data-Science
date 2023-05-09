import ply.lex as lex
import ply.yacc as yacc
import graphviz
import uuid
from graphviz import Digraph


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


# Symbol table
symbol_table = {}


# Quadruples
quadruples = []


# Helper functions for quadruples
def new_temporary():
    return f't{len(symbol_table)}'


def add_quadruple(operator, operand1, operand2, result):
    quadruples.append((operator, operand1, operand2, result))


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
    p[0] = p[1]


def p_expression(p):
    '''expression : primary_expression
                  | binary_expression'''
    p[0] = p[1]


def p_primary_expression(p):
    '''primary_expression : IDENTIFIER
                          | NUMBER
                          | STRING'''
    if isinstance(p[1], str) and p[1] in symbol_table:
        p[0] = ('SYMBOL', p[1])
    else:
        p[0] = ('PRIMARY_EXPRESSION', p[1])

def p_binary_expression(p):
    '''binary_expression : expression OPERATOR expression'''
    temp = new_temporary()
    add_quadruple(p[2], p[1], p[3], temp)
    p[0] = ('SYMBOL', temp)

def p_var_declaration(p):
    '''var_declaration : KEYWORD IDENTIFIER DELIMITER'''
    symbol_table[p[2]] = None
    p[0] = ('VAR_DECLARATION', p[2])

def p_if_statement(p):
    '''if_statement : IF expression statement_list'''
    label_false = f'L{uuid.uuid4().hex[:6]}'
    add_quadruple('JPF', p[2], label_false, None)
    p[0] = ('IF_STATEMENT', p[2], p[3], label_false)

def p_print_statement(p):
    '''print_statement : PRINT expression DELIMITER'''
    add_quadruple('PRINT', p[2], None, None)
    p[0] = ('PRINT_STATEMENT', p[2])

def p_error(p):
    print(f'Syntax error: {p}')
    exit(1)

parser = yacc.yacc()

code = '''
int x;
int y;
x = 1 + 2;
y = x * 3;
if (y > 5) {
    print "Hello, world!";
} else {
    print "Goodbye, world!";
}
'''

ast = parser.parse(code)
print(ast)
print(quadruples)

graph = Digraph(comment='Quadruples')
for i, quad in enumerate(quadruples):
    graph.node(str(i), str(quad))
    if quad[1] is not None:
        graph.edge(str(i), str(quad[1]))
    if quad[2] is not None:
        graph.edge(str(i), str(quad[2]))
    if quad[3] is not None:
        graph.edge(str(i), str(quad[3]))
graph.render('quadruples', view=True)
