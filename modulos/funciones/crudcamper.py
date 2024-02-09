import os
import json

#Crea camper
def crearcamper(iaux = None):
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    if iaux == None:

        def acudiente(edad):
            nece = input("¿El camper tiene alguna necesidad especial?(S/N) \n").upper()
            if edad < 18 or nece == "S":
                infaux = {
                    "Nombre" : input("Ingrese el nombre del acudiente: "),
                    "Id" : input("Ingrese el id del acudiente: ")
                }
                return infaux
            return None
            
        inf = { 
            "Id" : int(input("Ingrese el id del camper: ")),
            "Estado" : "",
            "Ruta" : "",
            "Grupo" : "",
            "Notas" : [] 
        }
        for i, value in enumerate(camper):
                if value["Id"] == inf["Id"]:
                    print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
                    os.system('pause')
                    return
        inf["Nombre"] = input("Ingrese el nombre del camper: ")
        inf["Apellido"] = input("Ingrese el apellido del camper: ")
        inf["Edad"] = int(input("Ingrese la edad del camper: "))
        inf["Telefono"] = [
                {
                    f"{'Fijo' if(int(input('0. Celular 1. Fijo : '))) else 'Celular'}":
                    int(input(f'Numero de contacto {x+1}: '))
                }
                for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
            ],
        inf["Acudiente"] = acudiente(inf["Edad"])
        if inf["Acudiente"] == None:
            del inf["Acudiente"]
        camper.append(inf)
        print("El camper ha sido creado")
        savejson(camper)
        os.system('pause')
        return
    else :
        def acudiente(edad):
            nece = input("¿El camper tiene alguna necesidad especial?(S/N) \n").upper()
            if edad < 18 or nece == "S":
                infaux = {
                    "Nombre" : input("Ingrese el nombre del acudiente: "),
                    "Id" : input("Ingrese el id del acudiente: ")
                }
                return infaux
            return None
            
        inf = { 
            "Id" : iaux,
            "Nombre": input("Ingrese el nombre del camper: "),
            "Apellido" : input("Ingrese el apellido del camper: "),
            "Edad" : int(input("Ingrese la edad del camper: ")),
            "Estado" : "",
            "Ruta" : "",
            "Grupo" : "",
            "Notas" : [] 
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
        if inf["Acudiente"] == None:
            del inf["Acudiente"]
        return inf
#Elimina Camper
def eliminarcamper():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    id = int(input("Ingrese el id del camper a eliminar: "))
    for i,value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id: {value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            se = input("Esta seguro que desea eliminar el camper?(S/N)").upper()
            if se == "S":
                camper.pop(i)
                print("El camper ha sido eliminado")
                savejson(camper)
                os.system('pause')
                return
            else:
                return
    print("No se encontro el camper con ese id")
    os.system('pause')
#Actualiza Camper
def actualizarcamper():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    os.system('cls')
    id = int(input("Digite el id del camper a modificar: "))
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Nombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            se = input("Esta seguro que desea editar el camper?(S/N)")
            if se == "S":
                infaux = crearcamper(id)
                camper[i] = infaux
                print("El camper se ha modificado")
                savejson(camper)
                os.system('pause')
                return
            else:
                return
    print("No se encontro un camper con ese registro")
    os.system('pause')
#Ver todos los campers
def vertodoscampers():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    for i, value in enumerate(camper):
        print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \n---------------------')
    os.system('pause')
#Ver un solo camper               
def veruncamper():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    id = int(input("Ingrese el id del camper a buscar: "))
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            os.system('pause')
            return
    print("No se encontro ningun camper con ese id")
    os.system('pause')
#Guarda el json
def savejson(camper): 
    with open('camper.json', 'w') as json_file:
        json.dump(camper, json_file, indent=4)