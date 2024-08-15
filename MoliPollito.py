import json
from os import system
from datetime import date


#Funciones para abrir y guardar los datos del json de Menu
def abrirMenu():
    Menu=[]
    with open('Menu.json','r',encoding='utf-8') as openfile:
        Menu = json.load(openfile)  
    return Menu
def guardarMenu(miMenu): 
    with open("Menu.json","w",encoding='utf-8') as outfile:
        json.dump(miMenu,outfile,indent=4) 

#Funciones para abrir y guardar los datos del json de Pedidos
def abrirPedidos():
    Pedidos=[]
    with open('Pedidos.json','r',encoding='utf-8') as openfile:
        Pedidos = json.load(openfile)  
    return Pedidos
def guardarPedido(miPedido): 
    with open("Pedidos.json","w",encoding='utf-8') as outfile:
        json.dump(miPedido,outfile,indent=4)

#Funciones para abrir y guardar los datos del json de Pagos
def abrirPagos():
    Pagos=[]
    with open('Pagos.json','r',encoding='utf-8') as openfile:
        Pagos = json.load(openfile)  
    return Pagos
def guardarPagos(miPago): 
    with open("Pagos.json","w",encoding='utf-8') as outfile:
        json.dump(miPago,outfile,indent=4) 


boolGeneral = True

while boolGeneral == True:
    eleccion = int(input("BIENVENIDO A MOLIPOLLITO\n\n1.Crear Pedidos  \n2.Listar pedidos  \n3.Registrar Pagos  \n"))
    system("cls")

    if eleccion == 1:
        print("CREACION DE PEDIDOS\n")
        Menu = abrirMenu()
        items = []

        NombreCliente = str(input("Ingrese el nombre del cliente que va a hacer el pedido: "))
        boolPedido = True
        while boolPedido == True:
            system("cls")

            contador  = 1 
            for i in Menu["Menu"]:
                print(contador,i["Tipo"])
                contador += 1
            eleccionMenu = int(input("\n¿A qué grupo de items deseas acceder?: "))
            system("cls")

            print(Menu["Menu"][eleccionMenu-1]["Tipo"],"\n")
            contador = 1
            for i in Menu["Menu"][eleccionMenu-1]["Productos"]:
                print(contador,i["Nombre"])
                contador += 1
            EleccionProducto = int(input("\n¿Qué producto desea añadir a su compra?"))

            items.append(
                {
                    "Tipo" : Menu["Menu"][eleccionMenu-1]["Tipo"],
                    "Nombre" : Menu["Menu"][eleccionMenu-1]["Productos"][EleccionProducto-1]["Nombre"],
                    "Precio" : Menu["Menu"][eleccionMenu-1]["Productos"][EleccionProducto-1]["Precio"]
                }
            )
            AgregarOtro = int(input("¿Deseas agregar otro producto? 1/Si   2/No        "))
            system("cls")
            
            if AgregarOtro == 1:
                system("cls")
                continue
            elif AgregarOtro == 2: 

                print("Su pedido es: ")
                for i in items:
                    print(i["Tipo"],i["Nombre"],i["Precio"])

                EleAgregar = int(input("\nDesea guardar su orden? 1/Si   2/No        "))
                system("cls")
                if EleAgregar == 1:
                    Pedidos = abrirPedidos()
                    Pedidos.append(
                    {
                        "Cliente" : NombreCliente,
                        "items" : items,
                        "Estado" : "Creado"
                    }
                )  
                    guardarPedido(Pedidos)
                    input("\nPresione ENTER para continuar")
                    boolPedido = False
                elif EleAgregar == 2:
                    input("Saliendo del módulo de compras, presione ENTER para continuar")
                    boolPedido = False
                    system("cls")
                else:
                    input("Esta no es una opción válida, presione ENTER para continuar")
                    system("cls")
            else: 
                input("Esta no es una opción válida, presione ENTER para continuar")
                system("cls")
        
    elif eleccion == 2: 
        print("VISUALIZACIÓN DE PEDIDOS")
        Pedidos = abrirPedidos()
        contador = 1
        for i in Pedidos:
            print(contador,i["Cliente"])
            contador += 1
        eleccionRevisar = int(input("\nSeleccione al cliente que le desea revisar el pedido: "))
        system("cls")

        print("Tipo | Nombre | Precio\n")
        for i in Pedidos[eleccionRevisar-1]["items"]:
            print(i["Tipo"],"|",i["Nombre"],"|",i["Precio"])
            print("")
    
    elif eleccion == 3:
        print("REGISTRAR PAGOS")
        Pedidos = abrirPedidos()
        contador = 1
        for i in Pedidos:
            print(contador,i["Cliente"])
            contador += 1
        eleccionPago = int(input("Seleccione al cliente que le desea registrar el pago"))
        system("cls")
        TotalCompra = 0
        for i in Pedidos[eleccionPago-1]["items"]:  
            TotalCompra += i["Precio"]
        print("El total del pedido de ",Pedidos[eleccionPago-1]["Cliente"]," es: ",TotalCompra)
        print("")
        PagoCuenta = int(input("\nDesea pagar la cuenta? 1/Si   2/No        "))
        if PagoCuenta == 1:
            print("Pago de cuenta\n")
            Fecha = date.today()
            FechaPago = Fecha.isoformat()

            Pagos = abrirPagos()
            Pagos.append(
                {
                    "Cliente" : Pedidos[eleccionPago-1]["Cliente"],
                    "Total" : TotalCompra,
                    "FechaPago" : FechaPago
                }
            )
            guardarPagos(Pagos)

            input("\nPago registrado con éxito :D, presione ENTER para continuar")
            system("cls")

        elif PagoCuenta == 2: 
            input("Saliendo del módulo de registro de pagos, presione ENTER para continuar")
            system("cls")

    else:
        input("Esta no es una opción válida, presione ENTER para continuar\n")
        system("cls")