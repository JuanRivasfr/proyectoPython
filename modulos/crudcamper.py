import os
camper = list()

def crearcamper(i = None):
    
    def acudiente(edad):
        nece = input("¿El camper tiene alguna necesidad especial?(S/N) \n").upper()
        if edad < 18 or nece == "S":
            infaux = {
                "Nombre" : input("Ingrese el nombre del acudiente: "),
                "Id" : input("Ingrese el id del acudiente: ")
            }
            return infaux
        
    inf = { 
        "Id" : int(input("Ingrese el id del camper: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: ")),
        "Estado" : "",
        "Ruta" : "",
        "Area" : "",
        "Grupo" : "" 
    }
    inf["Direccion"] = input("Ingrese la direccion del camper: ")
    inf["Telefono"] = [
            {
                f"{'Fijo' if(int(input('0. Celular 1. Fijo : '))) else 'Celular'}":
                int(input(f'Numero de contacto {x+1}: '))
            }
            for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
        ],
    inf["Acudiente"] = acudiente(inf["Edad"])
    for i, value in enumerate(camper):
            if value["Id"] == inf["Id"]:
                print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
                os.system('pause')
                return
    if inf["Acudiente"] == None:
        del inf["Acudiente"]
    
    if i == None:
        camper.append(inf)
        print(camper)
        os.system('pause')
        return
    else :
        return(inf)
    
#Elimina Camper
def eliminarcamper():
    id = int(input("Ingrese el id del camper a eliminar: "))
    for i,value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id: {value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            se = input("Esta seguro que desea eliminar el camper?(S/N)").upper()
            if se == "S":
                camper.pop(i)
                print("El camper ha sido eliminado")
                os.system('pause')
                return
            else:
                return
    print("No se encontro el camper con ese id")
    os.system('pause')
#Actualiza Camper
def actualizarCamper():
    os.system('cls')
    id = int(input("Digite el id del camper a modificar: "))
    for i, value in camper():
        if value["Id"] == id:
            print(f'Nombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            se = input("Esta seguro que desea editar el camper?(S/N)")
            if se == "S":
                infaux = crearcamper(i)
                camper[value] = infaux
                print("El camper se ha modificado")
                print(camper)
                os.system('pause')
                return
            else:
                return
    print("No se encontro un camper con ese registro")
    os.system('pause')
                