import os
import json
#Importa el json

#Crea grupos
def creargrupos(iaux = None):
    os.system('cls')
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    with open('trainer.json', 'r') as json_file1:
        trainer = json.load(json_file1)

    with open('rutas.json', 'r') as json_file2:
        ruta = json.load(json_file2)
    if iaux == None:
        inf = { 
            "Identificador" : input("Ingrese el identificador del grupo: ").upper(),
            "Salon" : "",
            "Modulo" : "FPOO",
            "Estudiantes" : [],
            "Ruta" : ""
        }
        for i, value in enumerate(grupos):
                if value["Identificador"] == inf["Identificador"]:
                    print("Ya hay un registro creado con el mismo identificador, por favor intente con otro")
                    os.system('pause')
                    return
        inf["Inicio"] = input("Ingrese la fecha de inicio(AA/MM/DD): ")
        inf["Final"] = input("Ingrese la fecha de finalizacion(AA/MM/DD): ")
        print("Que trainer desde agregar al grupo?")
        for i, value in enumerate(trainer):
            print(f'{i+1}. {value["Nombre"]}')
        auxx = int(input(":"))
        contador = int(0)
        for i, value in enumerate(trainer):
            if (i + 1) == auxx:
                for i1, val in enumerate(value["HorariosD"]):
                    if val["Disponible"] == "No":
                        contador += 1
                        if contador == len(value["HorariosD"]):
                            print("El trainer no tiene horarios disponibles")
                            os.system('pause')
                            return
        for i, value in enumerate(trainer):
            if (i + 1) == auxx:
                nom = value["Nombre"]
                print("Horarios")
                for i1, val in enumerate(value["HorariosD"]):
                    if val["Disponible"] == "Si":
                        print(f'{i1+1}. {val["Horarios"]}')
                    else:
                        print(f'{i1+1}. {val["Horarios"]} (OCUPADO)')
                trainer[i]["Rutas"].append(inf["Identificador"])
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

        grupos.append(inf)
        print("El grupo ha sido creado")
        savejson(grupos)
        savejsontrainers(trainer)
        os.system('pause')
    else :
        inf = { 
            "Identificador" : iaux,
            "Salon" : "",
            "Modulo" : "FPOO",
            "Estudiantes" : [],
            "Ruta" : ""
        }
        inf["Inicio"] = input("Ingrese la fecha de inicio(AA/MM/DD): ")
        inf["Final"] = input("Ingrese la fecha de finalizacion(AA/MM/DD): ")
        print("Que trainer desde agregar al grupo?")
        for i, value in enumerate(trainer):
            print(f'{i+1}. {value["Nombre"]}')
        auxx = int(input(":"))
        contador = int(0)
        for i, value in enumerate(trainer):
            if (i + 1) == auxx:
                for i1, val in enumerate(value["HorariosD"]):
                    if val["Disponible"] == "No":
                        contador += 1
                        if contador == len(value["HorariosD"]):
                            print("El trainer no tiene horarios disponibles")
                            os.system('pause')
                            return
        for i, value in enumerate(trainer):
            if (i + 1) == auxx:
                nom = value["Nombre"]
                print("Horarios")
                for i1, val in enumerate(value["HorariosD"]):
                    if val["Disponible"] == "Si":
                        print(f'{i1+1}. {val["Horarios"]}')
                    else:
                        print(f'{i1+1}. {val["Horarios"]} (OCUPADO)')
                trainer[i]["Rutas"].append(inf["Identificador"])
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

        return inf
#Elimina Grupos
def eliminargrupos():
    os.system('cls')
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
                                    savejson(grupos)
                                    savejsontrainers(trainer)
                                    os.system('pause')
                                    return
            else:
                return
    print("No se encontro un grupo con ese identificador")
    os.system('pause')
#Actualiza Grupos
def actualizargrupos():
    os.system('cls')
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
                                    savejsontrainers(trainer)
                                    inf1 = creargrupos(id)
                                    grupos[i] = inf1
                                    print("El grupo ha sido editado")
                                    savejson(grupos)
                                    os.system('pause')
                                    return
            else:
                return
    print("No se encontro el camper con ese id")
    os.system('pause')
#Ver todos los grupos
def vertodosgrupos():
    os.system('cls')
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
    os.system('cls')
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
    print("No se encontro ningun grupo con ese identificador")
    os.system('pause')
#Guarda el json
def savejson(grupos): 
    with open('grupos.json', 'w') as json_file:
        json.dump(grupos, json_file, indent=4)

def savejsontrainers(trainer):
    with open('trainer.json', 'w') as json_file1:
        json.dump(trainer, json_file1, indent=4)