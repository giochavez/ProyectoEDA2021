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
        matriz
    
def verificar_fichas_v2(tablero): #true - bueno / false - malo
    count
    
    pass
    
def verificacion_chida(tablero):
    verificar_fichas_v1
if __name__ == "__main__":
    prueba = cargar_tablero()
    print(prueba)
    pass


#Música de atraco
