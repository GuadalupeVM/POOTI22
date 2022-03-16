class Sokoban:
    #0 - Muñeco
    #1 - Espacio
    #2 - Caja
    #3 - Paredes
    #4 - Metas

    # Controles
    # a - Izquirda
    # d - Derecha
    # w - Arriba
    # s - Abajo

    
    mapa = [3,1,1,1,0,1,1,1,3] #Define el mapa del juego
    posicion_x = 4 #posicion inicial del personaje

    def __init__(self):
        pass

    def imprimirMapa(self): #Metodo para imprimir mapa 
        for i in self.mapa: #Recorre cda caracter el juego
            if i == 1: #Si encuentra un numero 1 - espacio
                print(chr(8212), end = "") #Cambia un 1 por un " "
            elif i == 3: #3 - Pared
                print(chr(8962), end = "") #Cambia a tres por un simbolo
            else:
                print(chr(128512), end = "")
        print()# imprime una linea vacia

    def moverDerecha(self): #Metodo para mover el persoanje a la derecha
        self.posicion_x += 1 #Calcula la nueva posicion del muñeco
        self.mapa[self.posicion_x] = 0 #Coloca el muñeco en la nueva posicion
        self.mapa[self.posicion_x - 1]= 1 # Colocael espacio donde estaba el muñeco

    def moverIzquierda(self): #Metodo para mover el persoanje a la izquirda 
        self.posicion_x -= 1 #Calcula la nueva posicion del muñeco
        self.mapa[self.posicion_x] = 0 #Coloca el muñeco en la nueva posicion
        self.mapa[self.posicion_x + 1] = 1 # Colocael espacio donde estaba el muñeco

juego = Sokoban() #Crea un objeto para jugar

juego.imprimirMapa() # imprime el mapa

while True: #Blucle para jugar N veces
    instrucciones = "d-Derecha\na-Izquierda" # Instruciines el juego
    print(instrucciones)  #Imprime las istrucciones del juego
    movimientos = input("mover a: ") #lee el moviemto del juego
    if movimientos == "d":  # si es d - mover a la derecha
        juego.moverDerecha() #Mueve el muñeco a la derecha
        juego.imprimirMapa() # imprime el mapa 
    elif movimientos == "a": # si es a mover  a la derecha
        juego.moverIzquierda() 
        juego.imprimirMapa()
    elif movimientos == "q":
        print("Saliste del juego")
        break 
