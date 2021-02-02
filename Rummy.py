def verificacion(color,numero):
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
                aux2=verificacion(color,valor)
                if(aux2):
                    aux.append(aux2)
                else:
                    return False
            tablero.append(aux)
        archivo.close()
    except FileNotFoundError:
        print("juego vacio")
    return tablero


def verificar_fichas_v1(tablero):#true/bueno /false- malo no nos estamos copiando xd
    matriz={"negro":[],"rojo":[],"verde":[],"azul":[]}
    for x in matriz.keys():
        matriz[x]=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    for jugada in tablero:
        for ficha in jugada:
            matriz[ficha[1]][int(ficha[0])-1] +=1
    for color in matriz.keys():
        matriz[color].sort(reverse=True)
        if(matriz[color][0]>2):
            return False
    return True

def verificar_fichas_v2(tablero):
    lista_de_todas_las_fichas = []
    for jugada in tablero:
        for ficha in jugada:
            lista_de_todas_las_fichas.append(ficha)
    fichas = set(lista_de_todas_las_fichas)
    for actual in fichas:
        if lista_de_todas_las_fichas.count(actual) > 2:
            return False #configuracion invalida
    return True #configuracion valida

def verificar_jugada_v1(jugada):# por numero
    numeros_de_fichas=[]
    colores_de_fichas=[]
    for x in jugada:
        numeros_de_fichas.append(x[0])
        colores_de_fichas.append(x[1])
    con_numeros_de_fichas=set(numeros_de_fichas)
    con_numeros_de_fichas=list(con_numeros_de_fichas)
    colores_de_fichas=set(colores_de_fichas)
    print(con_numeros_de_fichas)
    print(colores_de_fichas)
    if(len(con_numeros_de_fichas)==1 and len(colores_de_fichas)==3 and len(jugada)==3):
        return "T"
    elif(len(con_numeros_de_fichas)==1 and  len(colores_de_fichas)==4 and len(jugada)==4):
        return "C"
    elif(len(jugada)>=3 and len(colores_de_fichas)==1):
        con_numeros_de_fichas.sort()
        if(numeros_de_fichas == con_numeros_de_fichas):
            return "E"
        con_numeros_de_fichas.sort(reverse=True)
        if(numeros_de_fichas == con_numeros_de_fichas):
            return "E"
        return False
    else:
        return False
    pass
 #team el chango loco aka el macaco
#escalera->E tercia T cuarteto C false esta mal


def verificar_jugada_FV(jugada):#escalera->E tercia T cuarteto C false esta mal
    x={}
    for ficha in jugada:
        x[ficha[1]]=ficha[0]
    if(len(jugada)==len(x)):
        return verificar_TC(jugada)
    elif(len(x)==1):
        return verificar_corrida2(jugada)
    return False

def verificar_corrida2(jugada):
    for i in range(len(jugada)-1) :
        if (((int(jugada[i][0])+1)) != (int(jugada[i+1][0]))):
            return False
    return "E"

def verificar_TC(jugada):
    if len(jugada)==3:
        for i in range(len(jugada)-1) :
            if (((int(jugada[i][0]))) != (int(jugada[i+1][0]))):
                return False
        return "T"
    elif len(jugada)==4:
        for i in range(len(jugada)-1) :
            if (((int(jugada[i][0]))) != (int(jugada[i+1][0]))):
                return False
        return "C"
    return False

def verificar_corrida(jugada):
    for actual in range(0,len(jugada)-1):
        if (int(jugada[actual][0])+1 != jugada[actual+1][0] or jugada[actual][1] != jugada[actual+1][1]):
            return False #No es corrida
    return True #Si es corrida

def verificacion_jugada_ver3(jugada):
    if verificar_corrida(jugada):
        return True #Es corrida
    #if verificar_Repeticion(jugada):
    #    return True #Es cuarteta o tercia
    return False #No es ninguna de las dos por lo tanto la jugada es invalida

    pass

def verificacion_chida(tablero):
    for jugadas in tablero:
        aux=len(jugadas)
        if(aux<3):
            return False# verifica que las jugadas sean de 3 o mas fichas
    return True

def jugada_v1(tablero):#devolera cuantas escaleras,cuartetas,tercias

    pass

def jugada_v2(jugada):
    if (jugada[0])[0] == (jugada[1])[0]:   #Si entra, es una tercia o cuarteta
        print("Es una tercia o cuarteta")
        for x in range(len(jugada)-2):
            if (jugada[x])[1] == (jugada[x+1])[1] or (jugada[x])[1] == (jugada[x+2])[1] or (jugada[x+1])[1] == (jugada[x+2])[1]:
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

def ingresar_ficha(tablero):
    ficha = False
    while ficha != True:
        numero = input("Ingrese el número de la ficha que deseas ingresar: ")
        print("Colores disponibles:\nVerde = V\nRojo = R\nAzul = A\nNegro = N\n")
        color = input("Ingresa la primera letra del color de tu ficha: ")
        ficha = verificacion(numero,color.upper()) #convertiremos la letra (en caso de ser minúscula) a MAYÚSCULA
        if ficha == False:
            print("Ficha no válida")



def ingresar_ficha_v2():
    ficha
    while ficha == False:
        numero = input("Ingrese el número de la ficha: ")
        print("Colores posibles:")
        print("V->verde")
        print("R->rojo")
        print("A->azul")
        print("N->color Esclavo")#jaja que racistas xd también quitar esto
        color=input("color: ")
        ficha = verificacion(color.upper(),numero)
        if(ficha==False):
            print("bueno tu estás pendejo o que hijo") #recordar quitar esto, no vaya a ser el diablo
    return ficha

"""
def ingresar_ficha_al_tablero(tablero):
    print("En qué posición deseas colocar la ficha? ")

    return tablero
"""
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
            print (ficha,end="") #ES DUENDE Y NIGGA
    return
def imprimir_tablero_V2(tablero):
    contador=0
    print("fichas",end="")
    for x in range(1,14):
        print("             "+str(x),end ="")

    for jugada in tablero:
        print("\n")
        contador +=1
        print("jugada "+str(contador)+":",end="")
        for ficha in jugada:
            print (f"  {ficha}  ",end="")
    return

    #print(f'{color:6} ---> {numero:3})
    #print(f'{color:6} ---> {numero:3})

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

        #Idea para corridas: Buscar si el numero esta dentro de la corrida, Cortar  la lista en el numero, agregar numero.
        #DIOS ESTA AQUI
        #ESTA AQUIIIIIII!!!!
        #TAN CERCA COMO EL AIRE QUEEEE RESPIROOO
        #TAN CERCA COMO LA MAÑANAAA SE LEVAAAANTAAAA
        #TAN CIERTO COMO QUE ÉSTE CANTO LO PUEDES OÍIIIIRRRRR
        #DIOOOOOOS ESTÁAAAAA AQUIIIIII ESTÁ AQUIIIIIII
        #DIOS ESTA AQUI
        #ESTA AQUIIIIIII!!!!
        #TAN CERCA COMO EL AIRE QUEEEE RESPIROOO
        #TAN CERCA COMO LA MAÑANAAA SE LEVAAAANTAAAAAAAAAAAAAAAAAAAAA
        #TAN CIERTO COMO QUE ÉSTE CANTO LO PUEDES OÍIIIIRRRRR
        #DIOOOOOOS ESTÁAAAAA AQUIIIIII ESTÁ AQUIIIIIII
if __name__ == "__main__":
    prueba = cargar_tablero()
    imprimir_tablero(prueba)
    pass


#Música de atraco
