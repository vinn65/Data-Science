import ply.lex as lex
import ply.yacc as yacc
import icurl
tokens = (
    "IDENTIFIER",
    "KEYWORD",
    "NUMBER",
    "OPERATOR",
    "DELIMITER",
    "STRING",
    "COMMENT",
    "IF",
    "ELSE",
    "PRINT",
)

t_ignore = " \t\n\r"  # ignore whitespace and tabs


def t_IDENTIFIER(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    keywords = {"int", "if", "else", "while", "print"}
    t.type = "KEYWORD" if t.value in keywords else "IDENTIFIER"
    return t


def t_NUMBER(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t


def t_OPERATOR(t):
    r"[\+\-\*/=<>\!]=?|!="
    return t


def t_DELIMITER(t):
    r"[;,\(\)\[\]\{\}]"
    return t


def t_STRING(t):
    r'"[^"]*"'
    return t


def t_COMMENT(t):
    r"\#.*"
    pass  # ignore comments


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# ICG rules
quadruples = []
temp_counter = 0


def new_temp():
    global temp_counter
    temp_counter += 1
    return f"t{temp_counter}"


def p_program(p):
    """program : statement_list"""
    global quadruples
    p[0] = ("PROGRAM", p[1])
    quadruples.append(("END", None, None, None))


def p_statement_list(p):
    """statement_list : statement
    | statement statement_list"""
    p[0] = p[1]


def p_statement(p):
    """statement : expression_statement
    | var_declaration
    | if_statement
    | print_statement"""
    p[0] = p[1]


def p_expression_statement(p):
    """expression_statement : expression DELIMITER"""
    p[0] = p[1]


def p_expression(p):
    """expression : primary_expression
    | binary_expression"""
    p[0] = p[1]


def p_primary_expression(p):
    """primary_expression : IDENTIFIER
    | NUMBER
    | STRING"""
    p[0] = p[1]


def p_if_statement(p):
    """if_statement : IF expression '{' statement_list '}'
    | IF expression '{' statement_list '}' ELSE '{' statement_list '}'"""
    global quadruples
    if len(p) == 6:
        quad = ("IF_FALSE", p[2], None, None)
        quadruples.append(quad)
        for statement in p[4]:
            quadruples.append(statement)
        quadruples.append(("IF_END", None, None, None))
    else:
        quad1 = ("IF_FALSE", p[2], None, None)
        quadruples.append(quad1)
    for statement in p[4]:
        quadruples.append(statement)
        quad2 = ("GOTO", None, None, None)
        quadruples.append(quad2)
        if len(p) == 9:
            quad3 = ("LABEL", None, None, None)
            quadruples.append(quad3)
    for statement in p[7]:
        quadruples.append(statement)
        quad4 = ("LABEL", None, None, None)
        quadruples.append(quad4)
    return ("IF_ELSE_STATEMENT", p[2], p[4], p[7])


def p_print_statement(p):
    """print_statement : PRINT '(' expression ')' DELIMITER"""
    quadruples.append(("PRINT", p[3], None, None))
    p[0] = ("PRINT_STATEMENT", p[3])


def p_binary_expression(p):
    """binary_expression : expression OPERATOR expression"""
    temp = new_temp()
    quadruples.append((p[2], p[1], p[3], temp))
    p[0] = ("BINARY_EXPRESSION", p[2], p[1], p[3])


def p_var_declaration(p):
    """var_declaration : KEYWORD IDENTIFIER '=' expression DELIMITER"""
    quadruples.append(("=", p[4], None, p[2]))
    p[0] = ("VAR_DECLARATION", p[1], p[2], p[4])


def p_error(p):
    if p:
        print(
            f"Syntax error at line {p.lineno}, position {p.lexpos}:\nunexpected token '{p.value}' of type '{p.type}'"
        )
    else:
        print("Syntax error: unexpected end of input")


parser = yacc.yacc()

# Test the parser
data = """
#this is a comment
x=5+2+3;

"""

print("----------------tokens---------------------")
lexer.input(data)
for token in lexer:
    print(token.type, token.value)

quadruples = []
result = yacc.parse(data)

print("----------------quadruples---------------------")
for quadruple in quadruples:
    print(quadruple)
