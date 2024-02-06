import os
import json
#Importa el json
with open('grupos.json', 'r') as json_file:
    grupos = json.load(json_file)

with open('trainer.json', 'r') as json_file1:
    trainer = json.load(json_file1)

with open('rutas.json', 'r') as json_file2:
    ruta = json.load(json_file2)

#Crea grupos
def creargrupos(iaux = None):

    inf = { 
        "Identificador" : input("Ingrese el identificador del grupo: ").upper(),
        "Inicio" : input("Ingrese la fecha de inicio(AA/MM/DD): "),
        "Final" : input("Ingrese la fecha de finalizacion(AA/MM/DD): "),
        "Salon" : "",
        "Modulo" : "Fundamentos de Programacion",
        "Estudiantes" : "",
        "Ruta" : ""
    }
    print("Que trainer desde agregar a la ruta?")
    for i, value in enumerate(trainer):
        print(f'{i+1}. {value["Nombre"]}')
    auxx = int(input(":"))
    for i, value in enumerate(trainer):
        if (i + 1) == auxx:
            nom = value["Nombre"]
            print("Horarios")
            for i1, val in enumerate(value["HorariosD"]):
                if val["Disponible"] == "Si":
                    print(f'{i1+1}. {val["Horarios"]}')
                else:
                    print(f'{i1+1}. {val["Horarios"]} (OCUPADO)')
    opc = int(input("¿Que horario desea agregar?\n:"))
    for i, value in enumerate(trainer):
        if (i + 1) == auxx:
            for i1, val in enumerate(value["HorariosD"]):
                if (i1 + 1) == opc:
                    hor = val["Horarios"]
                    val["Disponible"] = "No"
    inf["Trainer"] = nom
    inf["Horario"] = hor
    #Agregar Salon
    auxsalon = input("Que salon desea agregar? \n1. Artemis \n2. Apolo \n3. Sputnik \n:")
    if auxsalon == "1":
        salon = "Artemis"
    if auxsalon == "2":
        salon = "Apolo"
    if auxsalon == "3":
        salon = "Sputnik"
    if (grupos) != None:
        for i, value in enumerate(grupos):
            if value["Salon"] == salon and value["Horario"] == hor:
                print("El salon esta ocupado en ese horario")
                return
    inf["Salon"] = salon
    #Agregar ruta
    print("Que ruta desea agregar al grupo")
    for i,value in enumerate(ruta):
        print(f'{i+1}.{value["Nombre"]}')
    rut = int(input(": "))
    for i, value in enumerate(ruta):
        if rut-1 == i:
            inf["Ruta"] = value["Nombre"]

    for i, value in enumerate(grupos):
            if value["Identificador"] == inf["Identificador"]:
                print("Ya hay un registro creado con el mismo identificador, por favor intente con otro")
                os.system('pause')
                return
            
    if iaux == None:
        grupos.append(inf)
        print("El grupo ha sido creado")
        savejson()
        savejsontrainers()
        os.system('pause')
        return
    else :
        return inf
#Elimina Grupos
def eliminargrupos():
    id = input("Ingrese el identificador del grupo a eliminar: ").upper()
    for i,value in enumerate(grupos):
        if value["Identificador"] == id:
            print(f'Identificador: {value["Identificador"]} \nTrainer: {value["Trainer"]} \nHorario: {value["Horario"]} \nSalon: {value["Salon"]} \nRuta: {value["Ruta"]}')
            se = input("Esta seguro que desea eliminar la ruta?(S/N)").upper()
            if se == "S":
                for i1, val in enumerate(trainer):
                    if val == "HorariosD":
                        for i2, v in enumerate(val):
                            if v["Horarios"] == value["Horario"]:
                                val["Disponible"] = "Si"
                                grupos.pop(i)
                                print("La ruta ha sido eliminado")
                savejson()
                savejsontrainers()
                os.system('pause')
                return
            else:
                return
    print("No se encontro el camper con ese id")
    os.system('pause')
#Actualiza la ruta
def actualizarruta():
    os.system('cls')
    id = int(input("Digite el id del camper a modificar: "))
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Nombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            se = input("Esta seguro que desea editar el camper?(S/N)")
            if se == "S":
                iaux = 1
                infaux = crearcamper(iaux)
                camper[i] = infaux
                print("El camper se ha modificado")
                print(camper)
                savejson()
                os.system('pause')
                return
            else:
                return
    print("No se encontro un camper con ese registro")
    os.system('pause')
#Ver todos los campers
def vertodoscampers():
    for i, value in enumerate(camper):
        print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \n---------------------')
    os.system('pause')
#Ver un solo camper               
def veruncamper():
    id = int(input("Ingrese el id del camper a buscar: "))
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            os.system('pause')
            return
    print("No se encontro ningun camper con ese id")
    os.system('pause')
#Guarda el json
def savejson(): 
    with open('grupos.json', 'w') as json_file:
        json.dump(grupos, json_file, indent=4)

def savejsontrainers():
    with open('trainer.json', 'w') as json_file1:
        json.dump(trainer, json_file1, indent=4)