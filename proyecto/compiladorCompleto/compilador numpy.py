from ply import lex
from ply import yacc as yacc


reserved = {
    'import': 'IMPORT',
    'as': 'AS',
    'zeros': 'ZEROS',
    'from': 'FROM'
}

tokens = ['EQUALS', 'ARREGLO', 'LPAREN', 'RPAREN', 'FUNCION',
          'NUMBERS', 'OPERADOR', 'NUMPY', 'POINT', 'ARRAY', 'COMA','RCORCHER', 'LCORCHER', 'NP', 'VAR', 'ID', 'DOUBLEPOINT','BOOLEAN'] + list(
    reserved.values())

# Tokens
t_EQUALS = r'='
t_ARREGLO = r'\[([0-9],)*[0-9]\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBERS = r'[0-9]+'
t_OPERADOR = r'\+|\-|\*|\/'
t_POINT = r'\.'
t_COMA = r','
t_LCORCHER = r'\['
t_RCORCHER = r'\]'
t_DOUBLEPOINT = r':'
t_BOOLEAN = r'>|<|==|!='
t_ignore_COMMENT = r'\#.*'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    t.type = reserved.get(t.value,'ID')    # Check for reserved words

    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# para evitr que imprima dos veces el mensaje
global evitar
evitar = False

#errores lexicos
def t_error(t):
    global evitar
    global validadorTok
    validadorTok = True
    if(not evitar):
        print('')
        print("no existe el token '%s'" % t.value)
        print("ERROR LEXICO")
        print('')
    t.lexer.skip(1)
    evitar = True



# Build the lexer
lexer = lex.lex()


def p_statement(p):
    '''statement  : arreglo
                  | ID EQUALS arreglo
                  | VAR EQUALS arreglo
                  | operacion
                  | ID EQUALS operacion
                  | VAR EQUALS operacion
                  | importacion
                  | indexacion
                  | ID EQUALS indexacion
                  | VAR EQUALS indexacion
                  '''
    global contador
    global validadorVariable
    if(len(p) == 2):
        validadorVariable = False
        p[0] = p[1]
    elif len(p)== 4:
        validadorVariable = True
        print(2)
        print(p)
        reserved[p[1]] = 'VAR'
        p[0]=p[1] + p[2] + p[3]
        numArray[p[1]] = contador
        print(contador)

def p_importacion(p):
    '''importacion : IMPORT NUMPY AS ID
                   | IMPORT NUMPY
                   | FROM NUMPY IMPORT ARRAY
                   | FROM NUMPY IMPORT ARRAY AS ID
                   | FROM NUMPY IMPORT ID
                   | FROM NUMPY IMPORT ID AS ID
                   | IMPORT ID AS ID
                   | IMPORT ID
                   | FROM ID IMPORT ID
                   | FROM ID IMPORT ID AS ID'''
    cad = ''
    global error
    global validadorSin
    global validadorTok
    if len(p) == 3:
        if p[2] == 'numpy':
            reserved[p[2]] = 'NUMPY'
            reserved['array'] = 'ARRAY'
            cad = "1"
        else:
            validadorTok = True
            error = "la libreria que importo no existe en el compilador"
        p[0] = p[1] + p[2] + cad
    elif len(p) == 5:
        if p[2] == 'numpy':
            reserved[p[2]] = 'NUMPY'
            reserved['array'] = 'ARRAY'
            if p[3] == 'import':
                reserved['array'] = 'FUNCION'
            cad = "1"
            if p[3] == 'as':
                reserved[p[4]] = 'NP'
        else:
            validadorTok = True
            error = "la libreria que importo no existe en el compilador"
        p[0] = p[1] + p[2] + p[3] + p[4] + cad

    elif len(p) ==7:
        if p[2] == 'numpy':
            reserved[p[2]] = 'NUMPY'
            if (p[4] == 'array'):
                reserved[p[6]] = 'FUNCION'
            else:
                validadorSin = True
                error = 'esa funcion no esta habilitada o no existe en la libreria de numpy ()'
            cad = "1"
        else:
            validadorTok = True
            error = "la libreria que importo no existe en el compilador"
        p[0] = p[1] + p[2] + p[3] + p[4] + cad





def p_variosarreglos(p):
    '''variosarreglos : ARREGLO RPAREN
                      | ARREGLO COMA variosarreglos
                      '''

    global contador
    contador[0] += 1

    if len(p)==3:
        p[0] = p[1] + p[2]
    elif (len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
    if (contador[1]==0):
        contador[1]=len(str(p[1]).split(','))
    elif (contador[1] != len(str(p[1]).split(','))):
        global validadorSe
        validadorSe = True
        global error
        error = "Existe un arreglo de diferente dimension dentro de la matriz de manera horizontal (una lista es de diferente longitud)"

def p_variosarreglos2(p):
    '''variosarreglos2 : ARREGLO RCORCHER
                      | ARREGLO COMA variosarreglos2
                      '''
    global contador
    contador[0] += 1

    if len(p)==3:
        p[0] = p[1] + p[2]
    elif (len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
    if (contador[1]==0):
        contador[1]=len(str(p[1]).split(','))
    elif (contador[1] != len(str(p[1]).split(','))):
        global validadorSe
        validadorSe = True
        global error
        error = "Existe un arreglo de diferente dimension dentro de la matriz de manera horizontal (una lista es de diferente longitud)"

def p_arreglo(p):
    '''arreglo : NP POINT ARRAY LPAREN LPAREN variosarreglos RPAREN
               | NP POINT ARRAY LPAREN LCORCHER variosarreglos2 RPAREN
               | NP POINT ARRAY LPAREN LCORCHER RCORCHER RPAREN
               | NP POINT ARRAY LPAREN LPAREN RPAREN RPAREN
               | NP POINT ARRAY LPAREN ARREGLO RPAREN
               | NP POINT FUNCION LPAREN LPAREN variosarreglos RPAREN
               | NP POINT FUNCION LPAREN LCORCHER variosarreglos2 RPAREN
               | NP POINT FUNCION LPAREN LCORCHER RCORCHER RPAREN
               | NP POINT FUNCION LPAREN LPAREN RPAREN RPAREN
               | NP POINT FUNCION LPAREN ARREGLO RPAREN
               | NP POINT ZEROS LPAREN NUMBERS COMA NUMBERS RPAREN
               | NUMPY POINT ARRAY LPAREN LPAREN variosarreglos RPAREN
               | NUMPY POINT ARRAY LPAREN LCORCHER variosarreglos2 RPAREN
               | NUMPY POINT ARRAY LPAREN LCORCHER RCORCHER RPAREN
               | NUMPY POINT ARRAY LPAREN LPAREN RPAREN RPAREN
               | NUMPY POINT ARRAY LPAREN ARREGLO RPAREN
               | NUMPY POINT FUNCION LPAREN LPAREN variosarreglos RPAREN
               | NUMPY POINT FUNCION LPAREN LCORCHER variosarreglos2 RPAREN
               | NUMPY POINT FUNCION LPAREN LCORCHER RCORCHER RPAREN
               | NUMPY POINT FUNCION LPAREN LPAREN RPAREN RPAREN
               | NUMPY POINT FUNCION LPAREN ARREGLO RPAREN
               | FUNCION LPAREN LPAREN variosarreglos RPAREN
               | FUNCION LPAREN LCORCHER variosarreglos2 RPAREN
               | FUNCION LPAREN LCORCHER RCORCHER RPAREN
               | FUNCION LPAREN LPAREN RPAREN RPAREN
               | FUNCION LPAREN ARREGLO RPAREN
               | NUMPY POINT ZEROS LPAREN NUMBERS COMA NUMBERS RPAREN'''
    cad=''
    global contador
    if (len(p) == 7):
        contador[1] = len(str(p[5]).split(','))
        contador[0] += 1
        p[0]=p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + "2"
    elif (len(p) == 8):
        p[0]=p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + "4"
    elif len(p) == 6 :
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + "4"
    elif len(p) == 5 :
        contador[1] = len(str(p[3]).split(','))
        contador[0] += 1
        p[0] = p[1] + p[2] + p[3] + p[4] + "2"

def p_operacion(p):
    '''operacion : VAR OPERADOR VAR
                 '''
    global error
    global contador
    global validadorSe
    if numArray[p[1]] != numArray[p[3]]:
        if (numArray[p[3]][1] != numArray[p[1]][1]) & (numArray[p[3]][1] != 1) & (numArray[p[1]][1] != 1):
            validadorSe = True
            error = 'Existe un arreglo de diferente dimension horizontal en la operacion ()'
        elif (numArray[p[3]][0] != numArray[p[1]][0]) & (numArray[p[3]][0] != 1) & (numArray[p[1]][0] != 1):
            validadorSe = True
            error = 'Los operandos no podran ser transmitidos junto con formas  (broadcast)'
        if (numArray[p[3]][0] == 1):
            contador = numArray[p[1]]
        elif (numArray[p[1]][0] == 1):
            contador = numArray[p[3]]
    elif numArray[p[1]] == numArray[p[3]]:
        contador = numArray[p[1]]

    p[0] = p[1] + p[2] + p[3] + '3'


def p_slicer(p):
    '''slicer :  NUMBERS DOUBLEPOINT NUMBERS
               | NUMBERS DOUBLEPOINT
               | DOUBLEPOINT NUMBERS
               | DOUBLEPOINT
               '''
    if (len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 2:
        p[0] = p[1]


def p_indice(p):
    '''indice : NUMBERS COMA NUMBERS
              | NUMBERS
              | NUMBERS COMA
              | COMA NUMBERS
              | slicer COMA slicer
              | slicer COMA
              | COMA slicer
              | NUMBERS COMA slicer
              | slicer COMA NUMBERS'''
    if (len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 2:
        p[0] = p[1]


def p_indexacion(p):
    '''indexacion : VAR LCORCHER indice RCORCHER
                  '''

    p[0] = p[1] + p[2] + p[3] + p[4] + "6"





def p_error(p):
    global validadorTok
    global validadorSin
    if not validadorTok :
        print('')
        print("ERROR SINTACTICO!")
        print('')
        validadorSin = True

parser = yacc.yacc()
global validadorTok
global validadorSin
global validadorSe
global validadorVariable
global error


numArray = {}
nuevoAoM = len(numArray)

while True:
    validadorVariable = False
    validadorSe = False
    validadorSin = False
    validadorTok = False
    global contador
    error = ''
    contador = [0,0]
    try:
        s = str(input("-> "))
    except EOFError:
        break
    if not s: continue

    lexer.input(s)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

    result = parser.parse(s)

    if (result != None) & (not validadorSe) & (not validadorSin) & (not validadorTok):

        print('')
        print("CORRECTO")
        if ((len(numArray) != nuevoAoM) and validadorVariable):
            var = str(result).split('=')
            print('')
            print('Se ha creado un/a Array/Matriz ' + var[0] + ' de dimensiones (',numArray[var[0]],' )')
        elif ((len(numArray) != nuevoAoM) and not validadorVariable):
            print('')
            print('Se ha creado un/a Array/Matriz anonimo ')

        print('')

    elif(validadorSe & (not validadorSin)) & (not validadorTok):
        print('')
        print("no es lo que se espero (ERROR SEMANTICO)")
        print(error)
        print('')
    elif validadorTok:
        print('error lexico')



