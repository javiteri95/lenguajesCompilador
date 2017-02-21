import ply.lex as lex
import ply.yacc as yacc
import warnings

reserved = {
    'import': 'IMPORT',
    'as': 'AS',
    'numpy': 'NUMPY',
    'array': 'ARRAY',
    'zeros': 'ZEROS',
    'shape': 'SHAPE',
    'reshape': 'RESHAPE',
    'size': 'SIZE',
    'from': 'FROM',
}

tokens = ['EQUALS', 'ARREGLO', 'ARREGLO_BI', 'LPAREN', 'RPAREN',
          'NUMBERS', 'OPERADOR', 'BOOLEAN', 'POINT', 'COMA', 'RCORCHER', 'LCORCHER', 'DOUBLEPOINT', 'ID'] + list(
    reserved.values())

# Tokens
t_EQUALS = r'='
t_ARREGLO = r'\[([0-9],)*[0-9]\]'
t_ARREGLO_BI = r'\[(\[([0-9],)*[0-9]\],)*\[([0-9],)*[0-9]\]\]'
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


def nivel1():
    print("*" * 20 + "NIVEL 1" + "*" * 20)
    print(" "*4+"Importacion de la libreria Numpy")

    global validador
    validador = True

    variable=""
    #------------------------------parte sintactica--------------------------------------


    def p_expresion_import(p):
        '''expression : IMPORT NUMPY AS ID
                      | IMPORT ID FROM ID
                       '''

        if p[1] == "import":
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4]
        else:
            p[0] = p[1]

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!!")


    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("Ingrese sentencia: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones, Pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")


def nivel2():
    print("*" * 20 + "NIVEL 2" + "*" * 20)
    print(" "*4+"Creacion de arreglos")



    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expresion_arreglo(p):
        '''expression : ID EQUALS ID POINT ARRAY LPAREN ARREGLO RPAREN
                      | ID POINT ARRAY LPAREN ARREGLO RPAREN
                       '''
        p[0] = ""
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!")

    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("Ingrese sentencia: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones, pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")

def nivel3():
    print("*" * 20 + "NIVEL 3" + "*" * 20)
    print(" "*4+"Operaciones aritmeticas")

    global validador
    validador = True
    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expresion_operando(p):
        '''
        expression : ID OPERADOR ID
                   | ID EQUALS ID OPERADOR ID
        '''

        p[0] = ""
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!")

    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("Ingrese sentencia ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones. Pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")

def nivel4():
    print("*" * 20 + "NIVEL 4" + "*" * 20)
    print(" "*4+"Creacion de arreglos bidimensionales")

    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expresion_arregloBi(p):
        '''expression : ID EQUALS ID POINT ARRAY  LPAREN ARREGLO_BI RPAREN
                      | ID POINT ARRAY  LPAREN ARREGLO_BI RPAREN
                       '''

        p[0] = ""
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!")

    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("Ingrese sentencia: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones, pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")

def nivel6():
    print("*" * 20 + "NIVEL 6" + "*" * 20)
    print(" "*4+"Indexacion sobre matrices")



    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expresion_indexacion(p):
        '''
            expression : ID ARREGLO
                       | ID ARREGLO ARREGLO
                       | ID EQUALS ID ARREGLO
                       | ID EQUALS ID ARREGLO ARREGLO
                       | ID LCORCHER NUMBERS RCORCHER
                       | ID LCORCHER NUMBERS COMA NUMBERS RCORCHER
                       | ID LCORCHER NUMBERS RCORCHER LCORCHER NUMBERS RCORCHER

                       | ID EQUALS ID LCORCHER NUMBERS RCORCHER
                       | ID EQUALS ID LCORCHER NUMBERS COMA NUMBERS RCORCHER
                       | ID EQUALS ID LCORCHER NUMBERS RCORCHER LCORCHER NUMBERS RCORCHER
        '''
        p[0] = ""
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!")

    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("Ingrese sentencia: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones, pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")

def nivel7():
    print("*" * 20 + "NIVEL 7" + "*" * 20)
    print(" "*4+"Uso de funcion ZEROS")



    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
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
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!!")

    parser = yacc.yacc()

    while True:
        try:
            s = input("Ingrese sentencia: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitacioes, pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")


def nivel8():
    print("*" * 20 + "  NIVEL 8  " + "*" * 20)
    print(" "*4+"Creacion de matriz booleana")



    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expression_boolean(p):
        '''
            expression : ID EQUALS ID BOOLEAN ID
                       | ID BOOLEAN ID

        '''
        p[0] = ""
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:
            print("Error SINTACTICO!")

    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("ingrese: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones, pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")

def nivel9():
    print("*" * 20 + "  NIVEL 9  " + "*" * 20)
    print(" "*4+"Funciones comunes (shape,reshape,size)")



    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expression_funciones(p):
        '''
            expression : ID POINT SHAPE
                       | ID POINT SIZE
                       | ID POINT RESHAPE LPAREN NUMBERS COMA NUMBERS RPAREN
                       | ID EQUALS ID POINT SHAPE
                       | ID EQUALS ID POINT SIZE
                       | ID EQUALS ID POINT RESHAPE LPAREN NUMBERS COMA NUMBERS RPAREN
        '''

        p[0] = ""
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!")

    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("Ingrese sentencia: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones, pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")

def nivel11():
    print("*" * 20 + "  NIVEL 11  " + "*" * 20)
    print(" "*4+"Slicing")



    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expression_slicing(p):
        '''
            expression : ID LCORCHER NUMBERS DOUBLEPOINT RCORCHER
                       | ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS RCORCHER
                       | ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS DOUBLEPOINT RCORCHER
                       | ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS DOUBLEPOINT NUMBERS RCORCHER
                       | ID EQUALS ID LCORCHER NUMBERS DOUBLEPOINT RCORCHER
                       | ID EQUALS ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS RCORCHER
                       | ID EQUALS ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS DOUBLEPOINT RCORCHER
                       | ID EQUALS ID LCORCHER NUMBERS DOUBLEPOINT NUMBERS DOUBLEPOINT NUMBERS RCORCHER
        '''
        p[0] = ""
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("Error LEXICO!")
        else:

            print("Error SINTACTICO!")

    parser = yacc.yacc()

    while True:
        try:
            s = raw_input("Ingrese sentencia: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        if validador:
            print("Felicitaciones. Pasa al siguiente nivel!")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("Error. Intente de nuevo!")





global validador
bandera=True
while(bandera):
    opcion=""
    correcta=False
    while (not correcta):
        print("=" * 20 + "  BIENVENIDOS  " + "=" * 20)
        print("1.- Empezar entrenamiento")
        print("2.- Salir")
        opcion=str(raw_input("Ingrese una opcion: "))
        numeros=["1","2","3"]
        if(opcion.strip() in numeros):
            correcta=True
        else:
            print('')
            print("ingrese una opcion valida")
            print("")
    print("")
    if opcion=="1":

        level1=nivel1()
        level2=nivel2()
        level3=nivel3()
        level4 = nivel4()
        level6 = nivel6()
        level7 = nivel7()
        level8 = nivel8()
        level9 = nivel9()
        level11 = nivel11()
        print("Felicidades! Usted ha completado el juego!")
        print("******************************************************************")
        print("\n")
    elif opcion=="2":
        bandera = False
        print("")
        print("El programa de entrenamiento se ha cerrado.")
