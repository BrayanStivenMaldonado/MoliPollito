import json
from os import system

def abrirMenu():
    Menu=[]
    with open('Menu.json','r',encoding='utf-8') as openfile:
        Menu = json.load(openfile)  
    return Menu
def guardarMenu(miMenu): 
    with open("Menu.json","w",encoding='utf-8') as outfile:
        json.dump(miMenu,outfile,indent=4) 



boolGeneral = True

while boolGeneral == True:
    eleccion = int(input("BIENVENIDO A MOLIPOLLITO\n\n1.Crear Pedidos  \n2.  \n3."))
    system("cls")

    if eleccion == 1:
        print("CREACION DE PEDIDOS\n")
        Menu = abrirMenu()
        Pedido = []

        boolPedido = True
        while boolPedido == True:

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

            Pedido.append(
                {
                    "Tipo" : Menu["Menu"][eleccionMenu-1]["Tipo"],
                    "Nombre" : Menu["Menu"][eleccionMenu-1]["Productos"][EleccionProducto-1]["Nombre"],
                    "Precio" : Menu["Menu"][eleccionMenu-1]["Productos"][EleccionProducto-1]["Precio"]
                }
            )

            AgregarOtro = int(input("¿Deseas agregar otro producto? 1/Si   2/No        ")) 
            
            if AgregarOtro == 1:
                system("cls")
                continue
            elif AgregarOtro == 2: 
                print("Tu pedido es:\n")
                print("Tipo | Nombre | Precio\n")
                for i in Pedido:
                    print(i["Tipo"],"|",i["Nombre"],"|",i["Precio"])
                input("\nPresione ENTER para continuar")
                boolPedido = False
            else: 
                input("Esta no es una opción válida, presione ENTER para continuar")
                system("cls")
        
        

    elif eleccion == 2: 
        print("")
    
    elif eleccion == 3:
        print("")
    
    else:
        input("Esta no es una opción válida, presione ENTER para continuar\n")
        system("cls")