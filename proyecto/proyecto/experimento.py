import ply.lex as lex
import ply.yacc as yacc




def nivel1():
    print("*" * 20 + "NIVEL 1" + "*" * 20)
    print(" "*4+"Importación de la librería de numpy")

    global validador
    validador = True

    variable=""

    #------------- parte lexica --------------------------------------------------------------------


    reserved = {
        'import': 'IMPORT',
        'as': 'AS',
        'numpy': 'NUMPY',
        'from' : 'FROM'
    }

    tokens = ['ID'] + list(
        reserved.values())

    # Define a rule so we can track line numbers

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'ID')  # Check for reserved words
        return t

    # Build the lexer
    lexer = lex.lex()


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
            print("error lexico !")
        else:

            print(type(p))
            print("error sintactico!!")






    parser = yacc.yacc()

    while True:
        try:
            s = input("ingrese: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)
        if validador:
            print("pasa al siguiente nivel")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("error intente de nuevo!!")


def nivel2():
    print("*" * 20 + "NIVEL 2" + "*" * 20)
    print(" "*4+"creacion de un arreglo")



    global validador
    validador = True

    variable=""

    #------------- parte lexica -------------------------------------------------------------------------------


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

    tokens = ['EQUALS', 'ARREGLO', 'LPAREN', 'RPAREN',
              'NUMBERS', 'OPERADOR', 'BOOLEAN', 'POINT', 'COMA', 'RCORCHER', 'LCORCHER', 'DOUBLEPOINT', 'ID'] + list(
        reserved.values())

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

    # Build the lexer
    lexer = lex.lex()


    #------------------------ parte sintactica---------------------------------------------------------
    def p_expresion_arreglo(p):
        '''expression : ID EQUALS ID POINT ARRAY LPAREN ARREGLO RPAREN
                       '''

        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])

    # ---------------------------------- reglas generales -------------------------------------------
    def p_error(p):
        global validador
        validador = False
        if type(p).__name__ == "NoneType":
            print("error lexico !")
        else:

            print(type(p))
            print("error sintactico!!")

    parser = yacc.yacc()

    while True:
        try:
            s = input("ingrese: ")
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)
        if validador:
            print("pasa al siguiente nivel")
            print("")
            variable="paso"
            return True
        else:
            validador = True
            print("error intente de nuevo!!")


global validador
bandera=True
while(bandera):
    opcion=""
    correcta=False
    while (not correcta):
        print("=" * 20 + "bienvenidos" + "=" * 20)
        print("1.- Empezar entrenamiento")
        print("2.- Scoreboard")
        print("3.- Salir")
        opcion=str(input("ingrese una opcion:"))
        numeros=["1","2","3"]
        if(opcion in numeros):
            correcta=True
        else:
            print('')
            print("ingrese una opcion valida")
            print("")
    print("")
    if opcion=="1":

        level1=nivel1()
        if level1==True:
            nivel2()
    elif opcion=="3":
        bandera = False
        print("")
        print("el programa de entrenamiento se ha cerrado")
