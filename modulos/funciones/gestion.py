import os
import json

#Asignar estudiantes a los salones
def asignarestudiantes():
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)
    id = int(input("Digite el id del camper a matricular: "))
    for index1, valor in enumerate(camper):
        if valor["Id"] == id:
            if camper[index1]["Estado"] != "Pre-inscrito":
                print("El estado del camper no esta en Pre-inscrito, por lo que no es posible matricularlo")
                return
    for i2, value1 in enumerate(grupos):
        for i3, value2 in enumerate(grupos[i2]["Estudiantes"]):
            if grupos[i2]["Estudiantes"][i3]["Id"] == id:
                print("El camper ya esta registrado en un grupo")
                os.system('pause')
                return
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id: {value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
            opc = input("Esta seguro que desea agregar el camper al grupor?(S/N): ").upper()
            idestudiante = value.get("Id")
            nombreestudiante = value.get("Nombre")
            apellidoestudiante = value.get("Apellido")
            inf = {
                "Id" : idestudiante,
                "Nombre" : nombreestudiante,
                "Apellido" : apellidoestudiante
            }
            if opc == "N":
                return
    for i,value in enumerate(grupos):
        print("-----------------------------------------------------------")
        print(f'Identificador: {value["Identificador"]} \nTrainer: {value["Trainer"]} \nHorario: {value["Horario"]} \nSalon: {value["Salon"]} \nRuta: {value["Ruta"]}')
    gr = input("En que grupo desea agregar al camper? \n: ").upper()
    for i, value in enumerate(grupos):
        if value["Identificador"] == gr:
            if len(grupos[i]["Estudiantes"]) < 34:
                grupos[i]["Estudiantes"].append(inf)
                for index, value in enumerate(camper):
                    if camper[index]["Id"] == id:
                        camper[index]["Grupo"] = grupos[i]["Identificador"]
                        camper[index]["Ruta"] = grupos[i]["Ruta"]
                savejson(camper)
                savejson1(grupos)
                print("Se ha añadido el camper")
                os.system('pause')
            else: 
                print("El grupo esta lleno")
                os.system('pause')
                return
    
    opc1 = input("Dese agregar otro camper?(S/N): ").upper()
    if opc1 == "S":
        asignarestudiantes()
#Guarda el json

def savejson(camper): 
    with open('camper.json', 'w') as json_file:
        json.dump(camper, json_file, indent=4)

def savejson1(grupos): 
    with open('grupos.json', 'w') as json_file1:
        json.dump(grupos, json_file1, indent=4)