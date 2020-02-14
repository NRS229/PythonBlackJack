import random

class carta:
    nombre = ""
    valor = 0

    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

def pedirCarta():
    num = random.randrange(0,11)
    tip = tipoCarta[random.randrange(0,4)]
    if (num == 0):
        val = -1
        while (val < 0):
            print("Sacó un A, puede valer 1 u 11, cuál elige?")
            print("1)1")
            print("2)11")
            op = input()
            if op == "1":
                val = 1
            elif op == "2":
                val = 11
            else:
                print("Por favor digite un valor válido")
    elif (num > 8):
        val = 11
    else:
        val = num + 1
    cartaActual = carta(str(numeroCarta[num]) + " de " + str(tip), val)
    return cartaActual


#Tuplas
tipoCarta = ("Corazones", "Diamantes", "Tréboles", "Espadas")
numeroCarta = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K")
#Listas
listaUsuario = []
listaComputadora = []
#Variable asignable
margenError = 16
opcionMenu = 0
while(opcionMenu != 2):
    #Variables de juego
    juegoUsuario = 0
    juegoComputadora = 0
    print("")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("         Juego 21")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Por favor digite una opción:")
    print("1)Empezar juego")
    print("2)Salir")
    opcionMenu = input()

    if opcionMenu == "1":
        deseaOtra = True
        while (deseaOtra):
            
            #Carta para usuario
            cartaPedida = pedirCarta()
            print("Su carta es: " + cartaPedida.nombre + ", valor: " + str(cartaPedida.valor))
            listaUsuario.append(cartaPedida.nombre)
            juegoUsuario += cartaPedida.valor
            #Carta para computadora
            cartaPedida = pedirCarta()
            listaComputadora.append(cartaPedida.nombre)
            juegoComputadora += cartaPedida.valor
            print("Desea otra?")
            print("1)Sí")
            print("2)No")
            opcionPedirCarta = input()
            if opcionPedirCarta == "1":
                deseaOtra = True
            else:
                deseaOtra = False
            if(juegoComputadora < margenError):
                #Carta para computadora
                cartaPedida = pedirCarta()
                listaComputadora.append(cartaPedida.nombre)
                juegoComputadora += cartaPedida.valor
            
            #Detectar que los juegos no sean mayor a 21
            if (juegoUsuario > 21):
                print("Su juego es mayor a 21, por lo tanto perdió")
                deseaOtra = False
            elif (juegoComputadora > 21):
                print("El juego de la computadora es mayor a 21, por lo tanto ganó")
                deseaOtra = False
            
        #Termina el juego
        print("Sus cartas son: " + str(listaUsuario))
        print("Equivalen a: " + str(juegoUsuario))
        print("Las cartas de la computadora son: " + str(listaComputadora))
        print("Equivalen a: " + str(juegoComputadora))
        if(juegoComputadora > juegoUsuario):
            print("Por lo tanto gana la computadora")
        elif(juegoComputadora == juegoUsuario):
            print("Los dos jugadores tienen un empate")
            cartaUsuario = pedirCarta()
            cartaComputadora = pedirCarta()
            print("Su carta para el desempate es: " + cartaUsuario.nombre)  
            print("La carta de la computadora para el desempate es: " + cartaComputadora.nombre) 
            if(cartaComputadora.valor > cartaUsuario.valor):
                print("Por lo tanto gana la computadora")
            else:
                print("Por lo tanto ganas tú")
        else:
            print("Por lo tanto ganas tú")
        
        

    elif opcionMenu == "2":
        print("Hasta luego!")
        #Cerrar la aplicación
    else:
        print("Por favor digite un valor válido")




