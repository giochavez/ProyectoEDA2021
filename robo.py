def leer_tablero(Archivo_nombre):
    tuplaFichas=()
    listatuplas=[]
    tablero=[]
    try:
        archivo=open(Archivo_nombre,'rt') 
        print(f"leyendo tablero del archivo de texto {Archivo_nombre} loading........." )
        for tupla in archivo:
            tupla= tupla.split('|')
            for ficha in tupla:
                ficha= ficha.split(',')
                color, numero = ficha
                numero= int(numero)
                tuplaFichas=(color,numero) 
                listatuplas.append(tuplaFichas)
            tablero.append(listatuplas)
            listatuplas=[]  
        archivo.close()
        print("Tablero Leido del archivo....\n")
    except FileNotFoundError:
        print("Tablero Vacio error en el archivo verificar ruta y nombre....") 
    return tablero

def imprime_tablero(tablero):
    for n in tablero:
        print(f"{n}")   
    pass   

def corrida(tablero):
    for c in tablero:
        i=0
        for n in range(0,len(c)-1):
            if (c[n][0] ==c[n+1][0])and((c[n][1]+1) ==c[n+1][1]):
                i=i+1
        if i ==len(c)-1 and(len(c)>=3):
            i=0
            c.insert(0,'Corrida')
    pass


def tercia(tablero):   
    for c in tablero:
        i=0 
        for n in range(0,len(c)-1):
            if (c[n][0] != c[n+1][0])and(c[n][1] ==c[n+1][1]):
                i=i+1
        if i ==len(c)-1 and(len(c)==3):
            i=0
            c.insert(0,'Tercia')
    pass 

def cuarteta(tablero):
    for c in tablero:
        i=0 
        for n in range(0,len(c)-1):
            if (c[n][0] != c[n+1][0])and(c[n][1] ==c[n+1][1]):
                i=i+1
        if i ==len(c)-1 and(len(c)==4):
            i=0
            c.insert(0,'Cuarteta')
    pass 

def verificacion_final(tablero):
    i=0
    for c in tablero:
        if c[0]=='Corrida' or  c[0]=='Cuarteta' or  c[0]=='Tercia':
            i=i+1
    if i== len(tablero):
        return True
    else:
        return False 


def verificacion(tablero):
    cuarteta(tablero)
    corrida(tablero)
    tercia(tablero)
    v=verificacion_final(tablero)
    
    if v==True:   
        print("la configuracion actual del tablero es valida \n")
        imprime_tablero(tablero)
    else:
        print("la configuracion actual del tablero es incorrecta\n")
    pass
     

def menu(): 
    ops = ['Agregar ficha', 'Reordenar juego'] 
    while True:
        print("\nBienvenido a tu agenda, elige una opicón: \n ")
        for i in range(len(ops)):
            print( i+1, ") ", ops[i] )
        seleccion = int(input("Opción "))
        if seleccion>=1 and seleccion<=2:
            return seleccion
        print("Opción inválida!!")

def insertarFicha(op2,ao,ficha,tablero):
    if ao== '1':
        tablero[op2].insert(1,ficha)
    if ao== '2':
        tablero[op2].append(ficha)
    pass       

def intenta_corrida(lista):
    i=0
    for n in range(0,len(lista)-1):
        if (lista[n][0] ==lista[n+1][0])and((lista[n][1]+1) ==lista[n+1][1]):
            i=i+1
        if i ==len(lista)-1 and(len(lista)>=3):
            i=0
            lista.insert(0,'Corrida')
    pass


def intenta_cuarteta(lista):
    i=0 
    for n in range(0,len(lista)-1):
        if (lista[n][0] != lista[n+1][0]) and(lista[n][1] ==lista[n+1][1]):
            i=i+1
        if i ==len(lista)-1 and(len(lista)==4):
            i=0
            lista.insert(0,'Cuarteta')
    pass 

def intenta_tercia(lista):
    i=0 
    for n in range(0,len(lista)-1):
        if (lista[n][0] != lista[n+1][0]) and(lista[n][1] ==lista[n+1][1]):
            i=i+1
        if i ==len(lista)-1 and(len(lista)==3):
            i=0
            lista.insert(0,'Tercia')
    pass

def intentarMovimiento(tablero,ao2,origen,destino,fichaMove):
    ficha2=tablero[origen][fichaMove]
    tablero[origen].remove(ficha2)
    insertarFicha(destino,ao2,ficha2,tablero)
            
    if tablero[destino][0]=='Corrida':
        tablero[destino].pop(0)
        intenta_corrida(tablero[destino])

    if tablero[destino][0]=='Tercia':
        tablero[destino].pop(0)
        intenta_cuarteta(tablero[destino])
    intenta_tercia(tablero[destino])
    verificacion(tablero)    
    pass       

if __name__=="main_":
    ficha=()
    tablero=leer_tablero('tableroprofe.txt')
    imprime_tablero(tablero)
    print(" ")
    verificacion(tablero)
    op= menu()

    while True:
        eleccion = menu()
        if eleccion == 1:
            color, numero = input(" ingresa el color y el valor de la ficha separados por comas: color,numero: ").split(',')
            numero=int(numero)
            ficha=(color,numero)
            print(" donde quiere colocar la ficha ")
            n=0
            for p in tablero:
                n=n+1 
                print(f"{n} ) {p}")    
            op2=int(input(" ingresa el numero de la lista donde ingresaras la ficha: "))-1
            print("donde la colocaras al pricipio o al final de la lsita")
            print("1) principio ")
            print("2) final ")
            ao= input("ingresa el numero de tu opcion: ")
            insertarFicha(op2,ao,ficha,tablero)
            imprime_tablero(tablero)
            break
        elif eleccion == 2:
            print(" que movimiento desea hacer ")
            print(" del siguiente tablero indique origen,destino y ficha que desea mover")
            n=0
            for p in tablero:
                n=n+1 
                print(f"{n} ) {p}")   
            origen=int(input("ingrese numero de la lista de origen: "))-1
            destino=int(input("ingrese numero de la lista destino: "))-1
            n=0
            for p in tablero[origen]:
                n=n+1 
                print(f"{n} ) {p}")
            fichaMove=int(input(" indica el numero de  la ficha que deseas mover: "))-1       
            print("donde la colocaras al pricipio o al final de la lista destino: ")
            print("1) principio ")
            print("2) final ")
            ao2= input("ingresa el numero de tu opcion: ")
            intentarMovimiento(tablero,ao2,origen,destino,fichaMove)
