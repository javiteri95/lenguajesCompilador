import ply.lex as lex
import ply.yacc as yacc


reservada = {
    "import" : "IMPORT",
    "as" : "AS",
    "numpy" : "NUMPY",
    "from" : "FROM"
}

tokens = ["ID"] + list(reservada.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservada.get(t.value,'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_expresion_import(p):
    '''expression : IMPORT NUMPY AS ID
                  | IMPORT ID FROM ID
                  '''
    if p[1]=="import":
        p[0]=p[1]+' '+p[2]+' '+p[3]+' '+p[4]
    else:
        p[0]=p[1]




# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def p_empty(p):
    'empty :'
    pass

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input("ingrese")
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
   if result == "import numpy as np":
       print("pasa al siguiente nivel")
       print("")
       break




data="import numpy as np"
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)



