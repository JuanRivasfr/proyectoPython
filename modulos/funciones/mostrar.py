import os
import json

def mcampersinscrito():
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    
    for i, value in enumerate(camper):
        if value["Estado"] == "Inscrito":
            print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]} \nEstado: {value["Estado"]}\n---------------------')