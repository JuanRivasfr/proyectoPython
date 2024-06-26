import os
import json

#Crea trainer
def creartrainer(iaux = None):
    os.system('cls')
    with open('trainer.json', 'r') as json_file:
        trainer = json.load(json_file)

    def horariostrainer():
            arrayaux = []
            print("En que horarios tiene disponibilidad el trainer?")
            while True:
                opc = int(input("1. 6-9AM \n2. 10-12AM \n3. 2-5PM \n4. 6-10PM \n: "))
                if opc == 1:
                    horario = "6-9AM"
                elif opc == 2:
                    horario = "10-12AM"
                elif opc == 3:
                    horario = "2-5PM"
                elif opc == 4:
                    horario = "6-10PM"
                elif opc > 4:
                    horariostrainer()
                hora = {
                    "Horarios" : horario,
                    "Disponible" : "Si"
                }
                arrayaux.append(hora)
                if (input("Desea agregar otro horario?(S/N)")) == "N":
                    break
            return arrayaux

    if iaux == None:
        inf = { 
            "Id" : int(input("Ingrese el id del trainer: ")),
            "Rutas" : [],
        }
        for i, value in enumerate(trainer):
                if value["Id"] == inf["Id"]:
                    print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
                    os.system('pause')
                    return
        inf["Nombre"] = input("Ingrese el nombre del trainer: ")
        inf["Apellido"] = input("Ingrese el apellido del trainer: ")
        inf["Edad"] = int(input("Ingrese la edad del trainer: "))
        inf["HorariosD"] = horariostrainer()
        inf["Telefono"] = [
                {
                    f"{'Fijo' if(int(input('0. Celular 1. Fijo : '))) else 'Celular'}":
                    int(input(f'Numero de contacto {x+1}: '))
                }
                for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
            ],
        trainer.append(inf)
        print("El trainer ha sido creado")
        savejson(trainer)
        os.system('pause')
        
    else :
        inf = { 
            "Id" : iaux,
            "Nombre": input("Ingrese el nombre del trainer: "),
            "Apellido" : input("Ingrese el apellido del trainer: "),
            "Edad" : int(input("Ingrese la edad del trainer: ")),
            "HorariosD" : horariostrainer(),
            "Telefono" : [
                {
                    f"{'Fijo' if(int(input('0. Celular 1. Fijo : '))) else 'Celular'}":
                    int(input(f'Numero de contacto {x+1}: '))
                }
                for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
            ],
            "Rutas" : [],
        }
        return inf
#Elimina trainer
def eliminartrainer():
    os.system('cls')
    with open('trainer.json', 'r') as json_file:
        trainer = json.load(json_file)
    id = int(input("Ingrese el id del camper a trainer: "))
    for i,value in enumerate(trainer):
        if value["Id"] == id:
            print(f'Id: {value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            se = input("Esta seguro que desea eliminar el trainer?(S/N)").upper()
            if se == "S":
                trainer.pop(i)
                print("El trainer ha sido eliminado")
                savejson(trainer)
                os.system('pause')
                return
            else:
                return
    print("No se encontro el trainer con ese id")
    os.system('pause')
#Actualiza trainer
def actualizartrainer():
    os.system('cls')
    with open('trainer.json', 'r') as json_file:
        trainer = json.load(json_file)
    os.system('cls')
    id = int(input("Digite el id del trainer a modificar: "))
    for i, value in enumerate(trainer):
        if value["Id"] == id:
            print(f'Nombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            se = input("Esta seguro que desea editar el trainer?(S/N)")
            if se == "S":
                infaux = creartrainer(id)
                trainer[i] = infaux
                print("El trainer se ha modificado")
                savejson(trainer)
                os.system('pause')
                return
            else:
                return
    print("No se encontro un camper con ese registro")
    os.system('pause')
#Ver todos los trainer
def vertodostrainers():
    os.system('cls')
    with open('trainer.json', 'r') as json_file:
        trainer = json.load(json_file)
    for i, value in enumerate(trainer):
        print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
        print("Horarios: ")
        for i2, valu in enumerate(trainer[i]["HorariosD"]):
            print(trainer[i]["HorariosD"][i2]["Horarios"])
        print("Grupos: ")
        for i2, valu in enumerate(trainer[i]["Rutas"]):
            print(trainer[i]["Rutas"][i2])
        print("----------------------------")
    os.system('pause')
#Ver un solo trainer               
def veruntrainer():
    os.system('cls')
    with open('trainer.json', 'r') as json_file:
        trainer = json.load(json_file)
    id = int(input("Ingrese el id del trainer a buscar: "))
    for i, value in enumerate(trainer):
        if value["Id"] == id:
            print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            os.system('pause')
            return
    print("No se encontro ningun trainer con ese id")
    os.system('pause')
#Guarda el json
def savejson(trainer): 
    with open('trainer.json', 'w') as json_file:
        json.dump(trainer, json_file, indent=4)