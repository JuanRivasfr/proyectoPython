import os
import json

def registropruebainicial():
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    id = int(input("Ingrese el id del camper a registrar la prueba inicial: "))
    for i, value in enumerate(camper):
        if value["Id"] == id:
            if value["Estado"] == "":
                print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            else:
                print("El camper ya cuenta con el registro de prueba inicial")
                os.system('pause')
                return
            opc = input("Desea registrar la nota a este camper?(S/N)").upper()
            if opc == "N":
                return
            nteorica = int(input("Ingrese la calificacion de la nota teorica: "))
            npractica = int(input("Ingrese la calificacion de la nota teorica: "))
            prom = (nteorica+npractica)/2
            if prom >= 60:
                print("El camper aprobo la prueba inicial, por lo su estado es pre-inscrito")
                camper[i]["Estado"] = "Pre-inscrito"
                os.system('pause')
            else:
                print("El camper no aprobo la prueba inicial")
                camper[i]["Estado"] = "No aprobado"
                os.system('pause')
            nota = {
                "Prueba inicial" : prom
            }
            camper[i]["Notas"].append(nota) 
            savejsoncamper(camper)

def savejsoncamper(camper): 
    with open('camper.json', 'w') as json_file:
        json.dump(camper, json_file, indent=4)