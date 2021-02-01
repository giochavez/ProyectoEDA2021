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
            linea = linea[:-1]
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
def verificar_jugada_v2(jugada):
    x={}
    for ficha in jugada:
        x[ficha[1]]=ficha[0]
    if(len(jugada)==len(x)):
        print("Posible tercia o cuarteta")
    elif(len(jugada)==1):
        if verificar_corrida(jugada):
            return "Corrida"

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

"""
def verificar_jugada_vclown(jugada):
    # DESCARTEN ESTA MIERDA, NO SE VA A PODER
    # cartas = jugada.items()
    # print(cartas) -> [(verde,1),(verde,2),(verde,3),(verde,4)]
    cartas = jugada.items()
    ver = set(jugada)
    if len(cartas) == 3:
        tercia = set(jugada)
        pass
    if len(cartas) == 4:
        pass
    pass
"""
def verificacion_chida(tablero):
    for jugadas in tablero:
        aux=len(jugadas)
        if(aux<3):
            return False# verifica que las jugadas sean de 3 o mas fichas
    return True

def jugada_v1(tablero):#devolera cuantas escaleras,cuartetas,tercias

    pass

def jugada_v2(tablero):
    pass

if __name__ == "__main__":
    prueba = cargar_tablero()
    print(prueba[0])
    print(verificacion_jugada_ver3(prueba[0]))
    pass


#Música de atraco
