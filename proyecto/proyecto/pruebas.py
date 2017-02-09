import ply.lex as lex

tokens = (
    'IMPORT', 'AS',
    'NUMPY', 'VARIABLE', 'EQUALS', 'ARRAY',
    'LPAREN', 'RPAREN','NUMBERS','PLUS','ZEROS','BOOLEAN',
    'SHAPE','RESHAPE','SIZE'
)

# Tokens
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IMPORT = r'import'
t_AS = r'as'
t_NUMPY = r'numpy|np'
t_EQUALS = r'='
t_ARRAY = r'\[([0-9],)*[0-9]\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBERS = r'[0-9]+'
t_PLUS = r'\+'
t_ZEROS = r'zeros'
t_BOOLEAN = r'>|<|==|!='
t_SHAPE = r'shape'
t_RESHAPE = r'reshape'
t_SIZE = r'size'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
import numpy as np
a = [4,5,5]
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

