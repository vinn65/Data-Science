import ply.lex as lex
import ply.yacc as yacc

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

# ...

# Quadruple generator
class QuadrupleGenerator:
    def __init__(self):
        self.quadruples = []
        self.temp_count = 0

    def new_temp(self):
        temp = f'T{self.temp_count}'
        self.temp_count += 1
        return temp

    def gen_quad(self, op, arg1, arg2, result):
        self.quadruples.append((op, arg1, arg2, result))

# ...

# Parser rules
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

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
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF expression '{' statement_list '}'
                    | IF expression '{' statement_list '}' ELSE '{' statement_list '}' '''
    quad_gen = p.parser.quad_gen
    if len(p) == 9:
        # If-else statement
        else_label = quad_gen.new_temp()
        end_label = quad_gen.new_temp()
        # Generate the condition code
        cond_code = ('COND', p[2], else_label)
        # Generate the code for the if block
        if_code = ('CODE', p[4], end_label)
        # Generate the code for the else block
        else_code = ('LABEL', else_label, ':')
        else_code += ('CODE', p[8], end_label)
        # Generate the code for the end of the if statement
        end_code = ('LABEL', end_label, ':')
        # Combine the code into a list of quadruples
        p[0] = [cond_code, if_code, else_code, end_code]
    else:
        # If statement
        end_label = quad_gen.new_temp()
        # Generate the condition code
        cond_code = ('COND', p[2], end_label)
        # Generate the code for the if block
        if_code = ('CODE', p[4], end_label)
        # Generate the code for the end
        end_code = ('LABEL', end_label, ':')
        # Combine the code into a list of quadruples
        p[0] = [cond_code, if_code, end_code]

def p_print_statement(p):
    '''print_statement : PRINT expression DELIMITER'''
    quad_gen = p.parser.quad_gen
    temp = quad_gen.new_temp()
    quad_gen.gen_quad('PRINT', p[2], temp, None)
    p[0] = [('PRINT', temp, None, None)]

# ...

# Lexer and parser initialization
lexer = lex.lex()
parser = yacc.yacc()

# Main program loop
while True:
    try:
        # Read input
        text = input('tape> ')
        if not text:
            continue
        # Parse input and generate quadruples
        ast = parser.parse(text, lexer=lexer)
        quad_gen = QuadrupleGenerator()
        for statement in ast:
            quad_gen.quadruples += statement
        # Print quadruples
        for quad in quad_gen.quadruples:
            print(quad)
    except KeyboardInterrupt:
        break
class QuadrupleGenerator:
    def __init__(self):
        self.quadruples = []
        self.temp_count = 0

    def new_temp(self):
        temp = f'T{self.temp_count}'
        self.temp_count += 1
        return temp

    def gen_quad(self, op, arg1, arg2, result):
        self.quadruples.append((op, arg1, arg2, result))

# Parser rules
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

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
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF expression '{' statement_list '}'
    | IF expression '{' statement_list '}' ELSE '{' statement_list '}' '''
    quad_gen = p.parser.quad_gen
    if len(p) == 9:
        # If-else statement
        else_label = quad_gen.new_temp()
        end_label = quad_gen.new_temp()
        # Generate the condition code
        cond_code = ('COND', p[2], else_label)
        # Generate the code for the if block
        if_code = ('CODE', p[4], end_label)
        # Generate the code for the else block
        else_code = ('LABEL', else_label, ':')
        else_code += ('CODE', p[8], end_label)
        # Generate the code for the end of the if statement
        end_code = ('LABEL', end_label, ':')
        # Combine the code into a list of quadruples
        p[0] = [cond_code, if_code, else_code, end_code]
    else:
        # If statement
        end_label = quad_gen.new_temp()
        # Generate the condition code
        cond_code = ('COND', p[2], end_label)
        # Generate the code for the if block
        if_code = ('CODE', p[4], end_label)
        # Generate the code for the end
        end_code = ('LABEL', end_label, ':')
        # Combine the code into a list of quadruples
        p[0] = [cond_code, if_code, end_code]

def p_print_statement(p):
    '''print_statement : PRINT expression DELIMITER'''
    quad_gen = p.parser.quad_gen
    temp = quad_gen.new_temp()
    quad_gen.gen_quad('PRINT', p[2], None, temp)
    p[0] = [('PRINT', temp, None, None)]

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f'Syntax error at token {p.type} ({p.value})')
    else:
        print('Syntax error at EOF')

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Main program loop
while True:
    try

