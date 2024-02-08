import os
import json

def mcampersinscrito():
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    
    for i, value in enumerate(camper):
        if value["Estado"] == "Inscrito":
            print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \nEstado: {value["Estado"]}\n---------------------')
    os.system('pause')

def mpruebainicialaprobado():
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)

    for i, value in enumerate(camper):
        for i1, valu in enumerate(camper[i]["Notas"]):
            for i2, val in (camper[i]["Notas"][i1]).items():
                if i2 == "Prueba inicial" and val >= 60:
                    print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \nEstado: {value["Estado"]}\n---------------------')
    os.system('pause')

def mbajorendimiento():
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)

    for i, value in enumerate(camper):
        if value["Estado"] == "Bajo rendimiento":
                    print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \nEstado: {value["Estado"]}\n---------------------')
    os.system('pause')

def mtrainerycamper():
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

def maprobador():
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)
    
    id = input("Ingrese el identificador del grupo a consultar: ")
    for i, value in enumerate(grupos):
        if value["Identificador"] == id:
            print(f'Trainer: {value["Trainer"]} \nRuta: {value["Ruta"]}')
            print("Estudiantes:")
            contadoraprob = int(0)
            contadordesaprob = int(0)
            for i2, valu in enumerate(grupos[i]["Estudiantes"]):
                for i3, val in enumerate(grupos[i]["Estudiantes"][i2]["Notas"]):
                    if val["modulo"] == "FPOO":
                        if val["notas mod"] >= 60:
                            contadoraprob += 1
                        else:
                            contadordesaprob += 1
            print(f'La cantidad de campers aprobados del modulo {val["modulo"]} son {contadoraprob}')
            print(f'La cantidad de campers desaprobados del modulo {val["modulo"]} son {contadordesaprob}')
            contadoraprob = int(0)
            contadordesaprob = int(0)
            for i4, valU in enumerate(grupos[i]["Estudiantes"]):
                for i3, val4 in enumerate(grupos[i]["Estudiantes"][i4]["Notas"]):
                    if val4["modulo"] == "PWEB":
                        if val4["notas mod"] >= 60:
                            contadoraprob += 1
                        else:
                            contadordesaprob += 1
            print(f'La cantidad de campers aprobados del modulo {val4["modulo"]} son {contadoraprob}')
            print(f'La cantidad de campers desaprobados del modulo {val4["modulo"]} son {contadordesaprob}')
            contadoraprob = int(0)
            contadordesaprob = int(0)
            for i5, valU in enumerate(grupos[i]["Estudiantes"]):
                for i3, val5 in enumerate(grupos[i]["Estudiantes"][i5]["Notas"]):
                    if val5["modulo"] == "PFORMAL":
                        if val5["notas mod"] >= 60:
                            contadoraprob += 1
                        else:
                            contadordesaprob += 1
            print(f'La cantidad de campers aprobados del modulo {val5["modulo"]} son {contadoraprob}')
            print(f'La cantidad de campers desaprobados del modulo {val5["modulo"]} son {contadordesaprob}')
            contadoraprob = int(0)
            contadordesaprob = int(0)
            for i6, valU in enumerate(grupos[i]["Estudiantes"]):
                for i3, val6 in enumerate(grupos[i]["Estudiantes"][i6]["Notas"]):
                    if val6["modulo"] == "BD":
                        if val6["notas mod"] >= 60:
                            contadoraprob += 1
                        else:
                            contadordesaprob += 1
            print(f'La cantidad de campers aprobados del modulo {val6["modulo"]} son {contadoraprob}')
            print(f'La cantidad de campers desaprobados del modulo {val6["modulo"]} son {contadordesaprob}')
            contadoraprob = int(0)
            contadordesaprob = int(0)
            for i7, valU in enumerate(grupos[i]["Estudiantes"]):
                for i3, val7 in enumerate(grupos[i]["Estudiantes"][i7]["Notas"]):
                    if val7["modulo"] == "BEND":
                        if val7["notas mod"] >= 60:
                            contadoraprob += 1
                        else:
                            contadordesaprob += 1
            print(f'La cantidad de campers aprobados del modulo {val7["modulo"]} son {contadoraprob}')
            print(f'La cantidad de campers desaprobados del modulo {val7["modulo"]} son {contadordesaprob}')
            
    os.system('pause')