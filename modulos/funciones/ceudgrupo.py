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

    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    with open('trainer.json', 'r') as json_file1:
        trainer = json.load(json_file1)

    with open('rutas.json', 'r') as json_file2:
        ruta = json.load(json_file2)

    inf = { 
        "Identificador" : input("Ingrese el identificador del grupo: ").upper(),
        "Inicio" : input("Ingrese la fecha de inicio(AA/MM/DD): "),
        "Final" : input("Ingrese la fecha de finalizacion(AA/MM/DD): "),
        "Salon" : "",
        "Modulo" : "Fundamentos de Programacion",
        "Estudiantes" : [],
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
                os.system('pause')
                return
    inf["Salon"] = salon
    inf["Trainer"] = nom
    inf["Horario"] = hor
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
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    with open('trainer.json', 'r') as json_file1:
        trainer = json.load(json_file1)

    with open('rutas.json', 'r') as json_file2:
        ruta = json.load(json_file2)
    id = input("Ingrese el identificador del grupo a eliminar: ").upper()
    for i,value in enumerate(grupos):
        if value["Identificador"] == id:
            print(f'Identificador: {value["Identificador"]} \nTrainer: {value["Trainer"]} \nHorario: {value["Horario"]} \nSalon: {value["Salon"]} \nRuta: {value["Ruta"]}')
            se = input("Esta seguro que desea eliminar la ruta?(S/N)").upper()
            if se == "S":
                for i1, val in enumerate(trainer):
                    for i2, va in (val).items():
                        if i2 == "HorariosD":
                            for i3, v in enumerate(va):
                                if v["Horarios"] == value["Horario"]:
                                    trainer[i1]["HorariosD"][i3]["Disponible"] = "Si"
                                    grupos.pop(i)
                                    print("El grupo ha sido eliminado")
                                    savejson()
                                    savejsontrainers()
                                    os.system('pause')
                                    return
            else:
                return
    print("No se encontro el camper con ese id")
    os.system('pause')
#Actualiza Grupos
def actualizargrupos():
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    with open('trainer.json', 'r') as json_file1:
        trainer = json.load(json_file1)

    with open('rutas.json', 'r') as json_file2:
        ruta = json.load(json_file2)
    id = input("Ingrese el identificador del grupo a eliminar: ").upper()
    for i,value in enumerate(grupos):
        if value["Identificador"] == id:
            print(f'Identificador: {value["Identificador"]} \nTrainer: {value["Trainer"]} \nHorario: {value["Horario"]} \nSalon: {value["Salon"]} \nRuta: {value["Ruta"]}')
            se = input("Esta seguro que desea editar la ruta?(S/N)").upper()
            if se == "S":
                for i1, val in enumerate(trainer):
                    for i2, va in (val).items():
                        if i2 == "HorariosD":
                            for i3, v in enumerate(va):
                                if v["Horarios"] == value["Horario"]:
                                    trainer[i1]["HorariosD"][i3]["Disponible"] = "Si"
                                    savejsontrainers()
                                    iux = 3
                                    inf1 = creargrupos(iux)
                                    grupos[i] = inf1
                                    print("El grupo ha sido editado")
                                    savejson()
                                    os.system('pause')
                                    return
            else:
                return
    print("No se encontro el camper con ese id")
    os.system('pause')
#Ver todos los grupos
def vertodosgrupos():
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    with open('trainer.json', 'r') as json_file1:
        trainer = json.load(json_file1)

    with open('rutas.json', 'r') as json_file2:
        ruta = json.load(json_file2)
    for i,value in enumerate(grupos):
        print("-----------------------------------------------------------")
        print(f'Identificador: {value["Identificador"]} \nTrainer: {value["Trainer"]} \nHorario: {value["Horario"]} \nSalon: {value["Salon"]} \nRuta: {value["Ruta"]}')
    os.system('pause')
#Ver una ruta             
def verungrupo():
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    with open('trainer.json', 'r') as json_file1:
        trainer = json.load(json_file1)

    with open('rutas.json', 'r') as json_file2:
        ruta = json.load(json_file2)
    id = input("Ingrese el identificador del grupo a ver: ").upper()
    for i,value in enumerate(grupos):
        if value["Identificador"] == id:
            print(f'Identificador: {value["Identificador"]} \nTrainer: {value["Trainer"]} \nHorario: {value["Horario"]} \nSalon: {value["Salon"]} \nRuta: {value["Ruta"]}')
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