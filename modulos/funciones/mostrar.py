import os
import json
#Muestra los campers inscritos
def mcampersinscrito():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    
    for i, value in enumerate(camper):
        if value["Estado"] == "Inscrito":
            print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \nEstado: {value["Estado"]}\n---------------------')
    os.system('pause')
#Muestra los campers que aprobaron la prueba inicial
def mpruebainicialaprobado():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)

    for i, value in enumerate(camper):
        for i1, valu in enumerate(camper[i]["Notas"]):
            for i2, val in (camper[i]["Notas"][i1]).items():
                if i2 == "Prueba inicial" and val >= 60:
                    print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \nEstado: {value["Estado"]}\n---------------------')
    os.system('pause')
#Muestra los campers en bajo rendimiento
def mbajorendimiento():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)

    for i, value in enumerate(camper):
        if value["Estado"] == "Bajo rendimiento":
                    print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \nEstado: {value["Estado"]}\n---------------------')
    os.system('pause')
#Muestra los trainer y los campers
def mtrainerycamper():
    os.system('cls')
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    for i, value in enumerate(grupos):
        print(f'Trainer: {value["Trainer"]} \nRuta: {value["Ruta"]}')
        print("Estudiantes:")
        for i1, valu in enumerate(grupos[i]["Estudiantes"]):
            print(f'Id: {valu["Id"]} \nNombre: {valu["Nombre"]} \nApellido: {valu["Apellido"]}')
            print("-----------------------")
        print("\n")
    os.system('pause')
#Muestra el trainer, campers y si estan aprobados o no
def maprobador():
    os.system('cls')
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)
    
    id = input("Ingrese el identificador del grupo a consultar: ").upper()
    for i, value in enumerate(grupos):
        if value["Identificador"] == id:
            print("---------------------------")
            print(f'Trainer: {value["Trainer"]} \nRuta: {value["Ruta"]}')
            print("Estudiantes:")
            for i2, valu in enumerate(grupos[i]["Estudiantes"]):
                print(f'Id: {valu["Id"]} \nEstudiante: {valu["Nombre"]} {valu["Apellido"]}')
                for i3, val in enumerate(grupos[i]["Estudiantes"][i2]["Notas"]):
                    if val["notas mod"] >= 60:
                        estado = "Aprobado"
                    else:
                        estado = "Desaprobado"
                    print(f'Modulo: {val["modulo"]} \nEstado: {estado}')
            
    os.system('pause')