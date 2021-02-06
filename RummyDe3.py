from itertools import combinations

def verificacion(numero,color):
    if(int(numero)>13 or int(numero) <1):
        return False
    if(color=="V"):
        color="verde"
    elif(color=="A"):
        color="azul"
    elif(color=="R"):
        color="rojo"
    elif(color=="N"):
        color="negro"
    else:
        return False
    return (numero,color)

def cargar_tablero():
    tablero = []#lista de listas
    try:
        archivo = open("tablero.txt",'rt')
        for linea in archivo:
            linea = linea[:-1] #Elimina el salto de linea
            jugada = linea.split(',')
            aux=[] #lista de fichas xd
            for ficha in jugada: #x=(1|v)
                valor,color=ficha.split('|')
                valor=valor[1:]
                color=color[-2]
                aux2=verificacion(valor,color)
                if(aux2):
                    aux.append(aux2)
                else:
                    return False
            tablero.append(aux)
        archivo.close()
    except FileNotFoundError:
        print("juego vacio")
    return tablero

def verificar_fichas_v2(tablero): #Equipo ZamoraChavezCristo
    lista_de_todas_las_fichas = []
    for jugada in tablero:
        for ficha in jugada:
            lista_de_todas_las_fichas.append(ficha)
    fichas = set(lista_de_todas_las_fichas)
    for actual in fichas:
        if lista_de_todas_las_fichas.count(actual) > 2:
            return False #configuracion invalida
    return True #configuracion valida

#equipo Cristo de zamora de las casas
def verificar_jugada_FV(jugada):#escalera->E tercia T cuarteto C false esta mal
    x={}
    aux2=len(jugada)
    for ficha in jugada: #Analiza ficha por ficha de la jugada
        x[ficha[1]]=ficha[0] 
    if(aux2<3): #Es una jugada con dos fichas (no valida)
        return False
    if(len(jugada)==len(x)): #Es o tercia o cuarteta 
        return verificar_TC(jugada) 
    elif(len(x)==1): #todas las fichas son del mismo color
        return verificar_corrida2(jugada)
    return False

def verificar_corrida2(jugada):
    for i in range(len(jugada)-1):
        if (((int(jugada[i][0])+1)) != (int(jugada[i+1][0]))): #Compara con su consecutivo
            return False
    return "E" #Es escalera

def verificar_TC(jugada):
    if len(jugada)==3:
        for i in range(len(jugada)-1) :
            if (((int(jugada[i][0]))) != (int(jugada[i+1][0]))): #Compara si la ficha actual es igual a la siguente en valor
                return False #Es un juego de tres fichas pero NO es tercia
        return "T" #Es una tercia
    elif len(jugada)==4:
        for i in range(len(jugada)-1) :
            if (((int(jugada[i][0]))) != (int(jugada[i+1][0]))):
                return False
        return "C"

    return False
#equipo Cristo de zamora de las casas
#AMBOS DOS
def verificacion_chida_del_tablero(tablero):#esta funcion debe ser cambiada con las funciones alternativas
    for jugadas in tablero:
        aux1=verificar_jugada_v1(jugadas)#cambiar por una laternativa
        if(aux1==False):
            return False
        aux2=len(jugadas)
        if(aux2<3):
            return False# verifica que las jugadas sean de 3 o mas fichas
    aux=verificar_fichas_v1(tablero)
    if(aux==False):
        return False
    return True

#CRISTO REDENTOR DE LOS mamadores
def jugada_v2(jugada):
    if (jugada[0])[0] == (jugada[1])[0]:   #Si entra, es una tercia o cuarteta
        print("Es una tercia o cuarteta")
        for x in range(len(jugada)-2):
            if (jugada[x])[1] == (jugada[x+1])[1] or (jugada[x])[1] == (jugada[x+2])[1] or (jugada[x+1])[1] == (jugada[x+2])[1] or (jugada[x])[1] == (jugada[-1])[1]:
                return False # Hay dos del mismo color
            if (jugada[x])[0] != (jugada[x+1])[0] or (jugada[x])[0] != (jugada[x+2])[0]:
                    return False # Él número es diferente

    #Es una corrida
    elif (jugada[0])[1] == (jugada[1])[1] or (jugada[0])[0] != (jugada[1])[0]:
        print("Es una corrida")
        for x in  range(len(jugada)-1):
            if (jugada[x])[1] != (jugada[x+1])[1] or (jugada[x])[0] == (jugada[x+1])[0]:
                return False # Hay una ficha de diferente color o del mismo valor en la corrida
            if int((jugada[x])[0]) > int((jugada[x+1])[0]):
                return False # El orden de las fichas es incorrecto
            if int((jugada[x])[0])+1 != int((jugada[x+1])[0]):
                return False
    return True
    pass
#cRISTO REDENTOR DE LOS MAMADORES

#CRISTO LA CONCHA DE LA LORA
def ingresar_ficha(tablero):
    ficha = False
    while ficha != True:
        numero = input("Ingrese el número de la ficha que deseas ingresar: ")
        print("Colores disponibles:\nVerde = V\nRojo = R\nAzul = A\nNegro = N\n")
        color = input("Ingresa la primera letra del color de tu ficha: ")
        ficha = verificacion(numero,color.upper()) #convertiremos la letra (en caso de ser minúscula) a MAYÚSCULA
        if ficha == False:
            print("Ficha no válida")
    return ficha
#HERIBERTO NO SABE QUE PEDo

#AMBOS DOS
def mover_ficha(ficha_q,jugada_q,antes,ficha_p,jugada_p,tablero):#
    #jugada_p=jugada_p[:]#donde quieras papi
    jugada_p2=jugada_p[:]
    jugada_q2=jugada_q[:]
    ficha=jugada_q2.pop(jugada_q2.index(ficha_q))
    jugada_p2.insert(antes+jugada_p2.index(ficha_p),ficha)
    if verificar_jugada_FV(jugada_q2) and verificar_jugada_FV(jugada_p2):#Cambiar función equipo alfa omega lobo dibamita feorozes mamadores
        jugada_q.remove(ficha_q)
        jugada_p.insert(antes+jugada_p2.index(ficha_p),ficha_q)
        return True
    return False


def ingresar_ficha_al_tablero(tablero):
    tablero_aux=[]
    for jugadas in tablero:
        tablero_aux.append(jugadas[:])
    print("ingresa la informacion de la ficha que quieres introducir al tablero")
    ficha = ingresar_ficha_v2()
    imprimir_tablero(tablero)
    jugada=9999
    while jugada>len(tablero):
        jugada=int(input("pon le numero de jugada en el que deseas poner tu ficha "))
        if(jugada>len(tablero)):
            print("tu estas pendejo o que hijo")
    opcion=4
    while (opcion <1 or opcion >2):
        print("1) colocar tu ficha antes de otra")
        print("2) colocar tu ficha despues de otra")
        opcion=int(input("opcion: "))
    indice=-1
    while indice ==-1:
        print("coloca la informacion de la ficha de posicionamiento")
        ficha_posicion=ingresar_ficha_v2()
        try:
            indice=tablero_aux[jugada-1].index(ficha_posicion)
        except ValueError:
            print("ficha no encontrada")
            indice=-1
        if(opcion ==2):
            indice +=1
        tablero_aux[jugada-1].insert(indice,ficha)
    veri=verificacion_chida_del_tablero(tablero_aux)
    if(veri==True):
        return tablero_aux
    else:
        return False
def imprimir_tablero(tablero):
    contador=0
    print("fichas",end="")
    for x in range(1,14):
        print("            "+str(x),end ="")

    for jugada in tablero:
        print("\n")
        contador +=1
        print("jugada "+str(contador)+":",end="")
        for ficha in jugada:
            print (ficha,end="")

    return

#MORENA
def dividir(jugada, tablero, ingresar_ficha_v2 ,verificar_jugada_FV):
    while True:
        ficha=ingresar_ficha_v2()
        P_jugada=[]
        p = int(input("Quieres agregar ficha:\n0.Antes\n1.Después "))
        F= input("Numero de la ficha:")
        P_jugada=jugada[:]
        P_jugada.insert(p+P_jugada.index((F,P_jugada[0][1])),ficha)
        print(P_jugada)
        a = input("Después de que ficha quieres hacer el corte?")
        try:
            C = P_jugada[P_jugada.index((a,jugada[0][1]))+1:] #[primer lista]
            D = P_jugada[:P_jugada.index((a,jugada[0][1]))+1]
        except ValueError:
            print("ficha no encontrada")
        print(C)
        print(D)
        if verificar_jugada_FV(C) and verificar_jugada_FV(D):#Cambiar funcion
            tablero.pop(tablero.index(jugada))
            tablero.append(C)
            tablero.append(D)
            print(tablero)
            return tablero
        else:
            print("Jugada no valida")
            print(tablero)
#CrisTO MOMENTO 
def recibir_jugada(tablero):
    print("\nQué ficha quieres agregar? (número,color)")
    ficha = (str(input()),str(input()))
    print("Configuración actual del tablero\n")
    num = 1
    for x in tablero:
        print(num,".- ",x)
        num = num+1
    print("\nQué quieres hacer?\na)Agregar ficha\nb)Reordenar el juego")
    respuesta = input()
    if respuesta == 'a':
        print("Dónde quieres agregar la ficha? (indica el número de la lista)")
        jugada = int(input())
        print("Indica la ubicación a colocar (índice dentro de la lista)")
        ubi = int(input())
        jugada_mod = tablero[jugada-1]
        jugada_mod.insert(ubi,ficha)
        if jugada_v2(jugada_mod) == False:
            print("Esa jugada no es válida")
            print(jugada_mod)
            jugada_mod.remove(ficha)
            return jugada_mod
        print("Jugada válida")
        print(jugada_mod)
        return jugada_mod
    if respuesta == 'b':
        print("Dónde quieres realizar el movimiento? (indica el número de la lista)")
        jugada = int(input())
        print("Indica la ubicación de la ficha a mover (índice dentro de la lista)")
        ubi = int(input())
        jugada_mod = tablero[jugada-1]
        ficha_aux = jugada_mod[ubi]
        jugada_mod.remove(ficha_aux)
        print("Dónde quieres colocar la ficha? (indica el número de la lista)")
        jugada = int(input())
        print("Indica la ubicación a colocar (índice dentro de la lista)")
        ubi = int(input())
        jugada_mod = tablero[jugada-1]
        jugada_mod.insert(ubi,ficha_aux)
        if jugada_v2(jugada_mod) == False:
            print("Esa jugada no es válida")
            print(jugada_mod)
            jugada_mod.remove(ficha_aux)
            return jugada_mod
        print("Jugada válida")
        print(jugada_mod)
        return jugada_mod

#TODES
def copiar_tablero(tablero):
    copia_tablero = []
    for jugada in tablero:
        copia_tablero.append(jugada[:])
    return copia_tablero

def posibles_escaleras(jugada,ficha,tablero):
    for x in ficha:

        P_jugada=jugada[:]

        try:
            P_jugada.insert(P_jugada.index(ficha),ficha)
            C = P_jugada[P_jugada.index(ficha)+1:] #[primer lista]
            D = P_jugada[:P_jugada.index(ficha)+1]
        except ValueError:
            print("ficha no encontrada")
        #print(C)
        #print(D)
        if verificar_jugada_FV(C) and verificar_jugada_FV(D):#Cambiar funcion
            tablero.pop(tablero.index(jugada))
            tablero.append(C)
            tablero.append(D)
            #print(tablero)
            return tablero
        else:
            return False

            #print(tablero)
""" por si se ocupa amen
def posible_tercia(tablero,ficha):# devuelve false en caso de que no se pueda fromar una tercia retorna true si por sus webos quito 2 fichas de dos jugadas
    posible_atraco=[] #Fichas que se pueden sacar de su jugada
    for jugadas in tablero:
        for fichas in jugadas:
            if(fichas[0]==ficha[0] and fichas[1]!=ficha[1]):
                posible_atraco.append(fichas)
    print(posible_atraco)
    if(len(posible_atraco)<2)
        return false

    return true
"""
"""
def formadora_escalera():
    pass
"""
def posible_insercion(jugada,fichas): #perdon umu
    for x in fichas: #porque las fichas pueden ser 2, x analizaría una ficha . si solo es una ficha x sería esa ficha
        P_jugada=jugada[:]
        if( verificar_jugada_v1(P_jugada)=="E"): #Escalera
            if(verificar_jugada_v1(P_jugada.append(x))):
                jugada.append(x)
            if(verificar_jugada_v1(P_jugada.insert(0,x))):
                jugada.insert(0,x)
        elif (verificar_jugada_v1(P_jugada)=="T"): #Tercia
            if(verificar_jugada_v1(P_jugada.append(x))): #traca traca la matraca
                jugada.append(x)
        return False#Esto lo sacaria si una sale mal!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Sí!!!!

def posible_robadera(ficha):#si_pero_el_pri_robo_mas
    colores = ["A","R","N","V"]
    posiblesJugadas = []
    if ficha[0] == 1: #CASO ESPECIAL
        posiblesJugadas.append([ficha,(ficha[0]+1,ficha[1]),(ficha[0]+2,ficha[1])]) #Se agregan sus dos consecutivos
        colores.remove(ficha[1]) #Se retira el color de la ficha ingresada
        for parDeColores in combinations(colores,2): #Se generan combinaciones de dos
            posiblesJugadas.append([ficha,(ficha[0],parDeColores[0]),(ficha[0],parDeColores[1])])
        return posiblesJugadas

    if ficha[0] == 13: #CASO ESPECIAL
        posiblesJugadas.append([ficha,(ficha[0]-1,ficha[1]),(ficha[0]-2,ficha[1])]) #Se agregan sus dos anteriores
        colores.remove(ficha[1]) #Se retira el color de la ficha ingresada
        for parDeColores in combinations(colores,2): #Se generan combinaciones de dos
            posiblesJugadas.append([ficha,(ficha[0],parDeColores[0]),(ficha[0],parDeColores[1])])
        return posiblesJugadas

    if ficha[0] == 2: #CASO ESPECIAL
        posiblesJugadas.append([ficha,(ficha[0]+1,ficha[1]),(ficha[0]+2,ficha[1])]) #Se agregan sus dos consecutivos
        posiblesJugadas.append([(ficha[0]-1,ficha[1]),ficha,(ficha[0]+1,ficha[1])])
        colores.remove(ficha[1]) #Se retira el color de la ficha ingresada
        for parDeColores in combinations(colores,2): #Se generan combinaciones de dos
            posiblesJugadas.append([ficha,(ficha[0],parDeColores[0]),(ficha[0],parDeColores[1])])
        return posiblesJugadas

    if ficha[0] == 12: #CASO ESPECIAL
        posiblesJugadas.append([ficha,(ficha[0]-1,ficha[1]),(ficha[0]-2,ficha[1])]) #Se agregan sus dos anteriores
        posiblesJugadas.append([(ficha[0]-1,ficha[1]),ficha,(ficha[0]+1,ficha[1])])
        colores.remove(ficha[1]) #Se retira el color de la ficha ingresada
        for parDeColores in combinations(colores,2): #Se generan combinaciones de dos
            posiblesJugadas.append([ficha,(ficha[0],parDeColores[0]),(ficha[0],parDeColores[1])])
        return posiblesJugadas

    #Para cualquier otro caso
    posiblesJugadas.append([ficha,(ficha[0]+1,ficha[1]),(ficha[0]+2,ficha[1])])
    posiblesJugadas.append([(ficha[0]-1,ficha[1]),ficha,(ficha[0]+1,ficha[1])])
    posiblesJugadas.append([(ficha[0]-2,ficha[1]),(ficha[0]-1,ficha[1]),ficha])#Se agrega su anterior y su consecutivo
    colores.remove(ficha[1])
    for parDeColores in combinations(colores,2):
        posiblesJugadas.append([ficha,(ficha[0],parDeColores[0]),(ficha[0],parDeColores[1])])
    return posiblesJugadas


def convertir_ficha(numero,color):
        if(int(numero)>13 or int(numero) <1):
            return False
        if(color=="verde"):
            color="V"
        elif(color=="azul"):
            color="A"
        elif(color=="rojo"):
            color="R"
        elif(color=="negro"):
            color="N"
        else:
            return False
        return (int(numero),color)
def robadera_para_1_ficha(posibles_juagadas,copia_tablero):
    for ficha in posibles_juagadas:
        copia_tablero.index(ficha)


        lista={[jugada]:"T",[jugada]:"C"}
#def completar_jugadas
#326
def avido(ficha,tablero): #Tampoco yo :( umu unu )
    tablero_generico=copiar_tablero(tablero)#lo mismo pero mas varato xd
    pila_tableros=[tablero_genexrico]
    pila_prohibidas =[]
    while True:
        for jugada in tablero_generico:
            if(posible_insercion(jugada,fichas) or posibles_escaleras(jugada,fichas)):
                return pila_tableros
        if (verificacion_chida_del_tablero(tablero) == False and pila_tableros[:-1]==tablero):
            return "F"  #acdecenar
        if(verificacion_chida_del_tablero(tablero)):

            return pila_tableros #fuck

if __name__ == "__main__":
    prueba = cargar_tablero()
    print(verificar_fichas_v2(prueba))
    #print(prueba)
    #ficha=ingresar_ficha_al_tablero(prueba)
    #dividir(prueba[0], prueba, ingresar_ficha_v2 ,verificar_jugada_FV)
    """
    verificar_fichas_v2()
    print(copiar_tablero(prueba))
    print(prueba)
    posibles_escaleras(prueba[0],("3","verde"),prueba)
    print(prueba)
    """
    #tupla=(3,"V")
    #print(posible_robadera(tupla))
    """
    print("-----------------------prueba2")
    print(verificacion_chida_del_tablero(prueba))
    print(prueba)
    print(ingresar_ficha_al_tablero(prueba))
    print("------------------tablero")
    """
    #print(prueba)
    #mover_ficha(("1","verde"),prueba[0],True,("1","negro"),prueba[5],prueba)
    #print(prueba)
    #mover_ficha(ficha_q,jugada_q,antes,ficha_p,jugada_p,tablero):#
    pass
