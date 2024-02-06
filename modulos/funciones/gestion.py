import os
import json

with open('camper.json', 'r') as json_file:
    camper = json.load(json_file)

def asignarestudiantes():
    id = int(input("Digite el id del estudiante a matricular: "))
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id: {value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]}')
#Guarda el json
def savejson(): 
    with open('camper.json', 'w') as json_file:
        json.dump(camper, json_file, indent=4)