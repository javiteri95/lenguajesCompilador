import ply.lex as lex
import ply.yacc as yacc





reserved = {
    'import' : 'IMPORT',
    'as' : 'AS',
    'numpy' : 'NUMPY',
    'array' : 'ARRAY',
    'zeros' : 'ZEROS',
    'shape' : 'SHAPE',
    'reshape' : 'RESHAPE',
    'size' : 'SIZE',
    'from' : 'FROM',
}

tokens = ['EQUALS','ARREGLO','LPAREN', 'RPAREN',
    'NUMBERS','OPERADOR','BOOLEAN','POINT','COMA','RCORCHER','LCORCHER','DOUBLEPOINT','ID'] + list(reserved.values())



# Tokens
t_EQUALS = r'='
t_ARREGLO = r'\[([0-9],)*[0-9]\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBERS = r'[0-9]+'
t_OPERADOR = r'\+|\-|\*|\/'
t_BOOLEAN = r'>|<|==|!='
t_POINT = r'\.'
t_COMA = r','
t_LCORCHER = r'\['
t_RCORCHER = r'\]'
t_DOUBLEPOINT = r':'



# Define a rule so we can track line numbers

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


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

#----------------------------- nivel 1 -----------------------------------------------------
def p_expresion_import(p):
    '''expression : IMPORT NUMPY AS ID
                  | IMPORT ID FROM ID
                   '''

    if p[1] == "import":
      p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4]
    else:
        p[0] = p[1]

#------------------------------ nivel 2 -----------------------------------------------------
def p_expresion_arreglo(p):
    '''expression : ID EQUALS ID POINT ARRAY LPAREN ARREGLO RPAREN
                   '''

    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])


#--------------------------------- nivel 3----------------------------------------------------

def p_expresion_operando(p):
    '''
    expression : ID OPERADOR ID
               | ID EQUALS ID OPERADOR ID
    '''

    p[0]=""
    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])

#------------------------nivel 4 ------------------------------------------------
def p_expresion_arregloBi(p):
    '''expression : ID EQUALS ID POINT ARRAY  LPAREN LCORCHER ARREGLO COMA ARREGLO RCORCHER RPAREN
                   '''

    p[0] = ""
    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])


#-------------------------nivel 6 --------------------------------------------
def p_expresion_indexacion(p):
    '''
        expression : ID ARREGLO
                   | ID ARREGLO ARREGLO
    '''
    p[0] = ""
    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])


#------------------------nivel 7 -----------------------------------

def p_expression_zeros(p):
    '''
        expression : ID EQUALS ID POINT ZEROS LPAREN NUMBERS RPAREN
                   | ID EQUALS ID POINT ZEROS LPAREN LPAREN NUMBERS COMA RPAREN RPAREN
                   | ID EQUALS ID POINT ZEROS LPAREN LPAREN NUMBERS COMA NUMBERS RPAREN RPAREN
                   | ID POINT ZEROS LPAREN NUMBERS RPAREN
                   | ID POINT ZEROS LPAREN LPAREN NUMBERS COMA RPAREN RPAREN
                   | ID POINT ZEROS LPAREN LPAREN NUMBERS COMA NUMBERS RPAREN RPAREN

    '''
    p[0] = ""
    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])

#----------------------nivel 8---------------------------------------
def p_expression_boolean(p):
    '''
        expression : ID EQUALS ID BOOLEAN ID
                   | ID BOOLEAN ID

    '''
    p[0] = ""
    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])

#--------------------nivel 9-----------------------------------------

def p_expression_funciones(p):
    '''
        expression : ID POINT SHAPE
                   | ID POINT SIZE
                   | ID POINT RESHAPE LPAREN NUMBERS COMA NUMBERS RPAREN
    '''

    p[0] = ""
    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])


#---------------------------nivel 11 -------------------------------
def p_expression_slicing(p):
    '''
        expression : ID LCORCHER NUMBERS DOUBLEPOINT RCORCHER
                   | ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS RCORCHER
                   | ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS DOUBLEPOINT RCORCHER
                   | ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS DOUBLEPOINT NUMBERS RCORCHER
    '''
    p[0] = ""
    for i in range(1,len(p)):
        p[0] += p[i]
    print(p[0])


#---------------------------------- reglas generales -------------------------------------------
def p_error(p):
    if type(p).__name__ == "NoneType":
        print("error lexico !")
    else:
        print(type(p))
        print("error sintactico!!" )

def p_empty(p):
    '''
    empty :
    '''
    pass

parser = yacc.yacc()



while True:
    try:
        s = input('numpy > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
