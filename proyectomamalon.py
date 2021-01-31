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

def verificacion_chida(tablero):
    for jugadas in tablero:
        aux=len(jugadas)
        if(aux<3):
            return False
    return True
    pass

def jugada_v1(tablero):#devolera cuantas escaleras,cuartetas,tercias

    pass
def jugada_v2(tablero):
    pass
if __name__ == "__main__":
    prueba = cargar_tablero()
    print(verificacion_chida(prueba))
    pass


#Música de atraco
