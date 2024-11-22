#será necesario para el numero del ticket
import random
import os
##########################################################


#Programa inicial sin registros, usuario nuevo en el que solo se podrá registrarse, iniciar sesion o salir.


def menu():
    while True:


        #definimmos nuestro menu inicial
        print("Bienvenido, que desea realizar hoy?: \n 1.Registrarme como cliente \n 2.Iniciar sesión \n 3.Salir")


        elegir=int(input("Seleccione una opción valida: "))
        if elegir== 1:
            registro()
            break
        elif elegir== 2:
            iniciarsesion()
            break
        elif elegir ==3:
            salir()
            break
        else:
            print("Escoja una opción valida")
######################################################
#opcion 1 en el menu()


#Campo de registro
def registro():
    nombre= input("Introduzca su nombre completo: ")
    dni= input("Introduzca su DNI: ")
    while len(dni) !=9:
        print("Incorrecto, intentelo de nuevo ")
        dni= input("Introduzca su DNI: ")
    with open("registro.txt", "r") as registro:
        for linea in registro:
            if dni in linea:
                print("Incorrecto, este usuario ya existe")
                print("**********************************")
                menu()
    registrocliente(nombre, dni)
#------------------------------------------------------------
#para cuando el cliente ya se encuentre registrado
def registrocliente(nombre,dni):
    with open("registro.txt", "a")as registro:
        registro.write(f"{nombre} con DNI: {dni}\n")
    print("Ya está registrado, bienvenido!")
    print("**********************************")
    menu_registrado(nombre, dni)
###########################################################
#opcion 2 en el menu()


#Inicio de sesión
def iniciarsesion():
    nombre=(input("Introduzca su nombre: "))
    dni= input("Introduzca su DNI: ")
    with open("registro.txt", "r")as registro:
        for linea in registro:
           nomregistro , dniregistro =linea.strip() .split(", ")
           if dniregistro== dni and nomregistro == nombre:
               print("**********************************")
               print(f"Bienvenido {nombre}")
               menu_registrado(nombre, dni)
        else:
            print("**********************************")
            print("Incorrecto, registrese antes.")
            menu()


###############################################################
# opcion 3 en el menu() y opcion 4 en menu_registrado()


#para salir y parar el programa
def salir():
    print("Gracias por utilizar nuestros servicios. \n Nos vemos pronto!")
#################################################################
#Segundo menu.


#menu para despues de haber iniciado sesion o despues de haberse rgistrado
def menu_registrado(nombre, dni):
    while True:
        print("Bienvenido, que desea realizar hoy?: \n 1.Visualizar clientes \n 2.Realizar una compra \n 3.Comprobar mi compra \n 4.Salir")
        elegir=int(input("Seleccione una opción valida: "))


        if elegir==1:
            clientes()
        elif elegir==2:
            comprar(nombre, dni)
        elif elegir== 3:
            buscarcompra()
        elif elegir ==4:
            salir()
            break
        else:
            print("Error introduzca una opción valida")


##################################################################
#opcion 1 en nuestro menu_registrado()
#para ver los clientes registrados, tanto en lista como solos
def clientes():
    print("Que consulta desea realizar? \n 1.Consultar todos los clientes registrados \n 2.Buscar un cliente registrado")
    elegir= int(input("Selecciona una opción valida: "))
    if elegir==1:
        with open("registro.txt", "r")as registro:
            contenido= registro.read()
            print(contenido)
    else:
        buscarcliente()
#------------------------------------------------------------
#para poder buscar a los clientes para la segunda opcion de clientes()
def buscarcliente():
    encontrar= False
    dniencontrar= input("Introduzca el DNI del cliente a buscar: ")
    with open("registro.txt", "r") as busqueda:
        for linea in busqueda:
            nombusca, dnibusca= linea.strip() .split( )
            if dniencontrar== dnibusca:
                encontrar=True
                print(f"Encontrado, cliente {nombusca}, con DNI: {dnibusca}")
    if encontrar== False:
        print("No se ha encontrado a dicho cliente en nuestra base de datos.")




#################################################################
#opcion 2 en nuestro menu_registrado()


#para realizar la compra
def comprar(nombre, dni):
    compra= False
    carrito= []
    productos= {1:"Grand theft auto V", 2: "FIFA 25", 3:"The last of us", 4: "Assassin's creed", 5:"Plantas VS Zombies"}


    while True:
        print(f"Elige entre nuestros productos!! \n {productos}")
        juego= int(input("Introduzca el numero del producto que desea comprar. \n O intruduzca 0 para finalizar la compra: "))

        if juego==0:
            break

        if juego in range (1-6):
            compra=True
            carrito.append(productos[juego]) #añadimos el juego al carrito
            print(f"CARRITO: {productos[juego]}")


        else:
            print("error, introduzca un valor valido")
    if compra== True:
        print("**********************************")
        print("Gracias por comprar con nosotros")
        tiket(nombre, dni,carrito)


#--------------------------------------------------


#creamos el ticket
def tiket(nombre, dni, carrito):
    numcompra = random.randint(1,1000)
    if not os.path.exists("compra.txt"):
        open("compra.txt", "w").close()
    with open("compra.txt", "r")as compralista:
        for linea in compralista:
            numero,_,_,_ =linea.strip() .split(", ")
            numero = int(numero)#lo convertimos ya que al salir de la lista es un str


            while numcompra == numero:
                numcompra = numcompra+1 #para que el siguiente numero no sea igual


    print(f"Su numero de compra es: {numcompra}")
    registrocompra(numcompra, nombre, dni, carrito)


#----------------------------------------------------


#registramos la compra recien validada
def registrocompra(numcompra, nombre, dni, carrito):
    carrito_str = ", ".join(carrito)
    with open("compra.txt", "a") as compraregistrada:
        compra= (f"{numcompra}, {nombre}, {dni},{carrito_str}\n")
        compraregistrada.write(compra)
    imprimir(numcompra)


#------------------------------------------------------


#para nuestros tickets de compra
def imprimir(numcompra):


    sicompra= False
    #buscamos dentro de nuestro archivo guardado
    with open("compra.txt", "r")as compratiket:
        for linea in compratiket:

            numtiket, nomtiket, dnitiket, carritotiket = linea.strip().split(", ")
            numtiket= int(numtiket)
            #imprimimos el ticket si es validado con el numero del ticket
            if numcompra == numtiket:
                sicompra= True
                print(f"Su ticket de compra: \n NUMERO DE COMPRA: {numcompra}\n NOMBRE: {nomtiket} \n DNI: {dnitiket} \n PRODUCTO(S): {carritotiket}")


        #en caso de que no existiese el numero dentro de nuestra lista
    if not sicompra:
        print("Error no se ha encontrado ninguna compra asisgnada al numero introducido.")


########################################################################
#opcion 3 en nuestro menu_registrado()


#para buscar la compra que un cliente solicite
def buscarcompra():
    numcompra= int(input("Introduzca el numero de la compra a buscar: "))
    print(f"Aqui tiene su ticket de compra:")
    imprimir(numcompra)


#########################################################################
#inicializamos el sistema
menu()
