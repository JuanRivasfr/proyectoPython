import os
import json
#Registro prueba inicial
def registropruebainicial():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    id = int(input("Ingrese el id del camper a registrar la prueba inicial: "))
    for i, value in enumerate(camper):
        if value["Estado"] == "":
            if value["Id"] == id:
                print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
                opc = input("Desea registrar la nota a este camper?(S/N)").upper()
                if opc == "N":
                    return
                nteorica = int(input("Ingrese la calificacion de la nota teorica: "))
                npractica = int(input("Ingrese la calificacion de la nota practica: "))
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
                return
    print("No es posible registrar la prueba inicial debido al estado del camper")
    os.system('pause')

#Registro prueba fpoo
def registropruebafpoo():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
    id = int(input("Ingrese el id del camper a registrar la prueba fpoo: "))
    for i, value in enumerate(camper):
        if value["Estado"] == "Pre-inscrito":
            if value["Id"] == id:
                print(f'Id :{value["Id"]} \nNombre: {value["Nombre"]} \nApellido: {value["Apellido"]} \nEdad: {value["Edad"]}')
                opc = input("Desea registrar la nota a este camper?(S/N)").upper()
                if opc == "N":
                    return
                nteorica = int(input("Ingrese la calificacion de la nota teorica: "))
                npractica = int(input("Ingrese la calificacion de la nota practica: "))
                prom = (nteorica+npractica)/2
                if prom >= 60:
                    print("El camper aprobo la prueba de fundamentos de programacion, por lo su estado es inscrito")
                    camper[i]["Estado"] = "Inscrito"
                    os.system('pause')
                else:
                    print("El camper no aprobo la prueba de fundamentos de programacion")
                    camper[i]["Estado"] = "Inscrito"
                    os.system('pause')
                nota = {
                    "Prueba fpoo" : prom
                }
                camper[i]["Notas"].append(nota) 
                savejsoncamper(camper)
                return
    print("No es posible registrar la prueba inicial debido al estado del camper")
    os.system('pause')

#Registro modulos
def registromodulos():
    os.system('cls')
    with open('camper.json', 'r') as json_file:
        camper = json.load(json_file)
        
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)

    id= int(input("Digite el id del camper a registrar la nota: "))
    for index, valor in enumerate(camper):
        if valor["Id"] == id:
                if valor["Estado"] != "No aprobado" and valor["Estado"] != "Bajo rendimiento" and valor["Estado"] != "":
                    print(f'Id :{valor["Id"]} \nNombre: {valor["Nombre"]} \nApellido: {valor["Apellido"]} \nEdad: {valor["Edad"]}')
                else:
                    print("No es posible registrar al camper debido a su estado")
                    os.system('pause')
                    return
                opct = input("Esta seguro que es el camper correcto?(S/N): ").upper()
                if opct == "N":
                    return
                else:
                    for i, value in enumerate(grupos):
                        for i2, val in enumerate(grupos[i]["Estudiantes"]):
                            if grupos[i]["Estudiantes"][i2]["Id"] == id:
                                mod = grupos[i]["Modulo"]
                                for index1, valorn in enumerate(grupos[i]["Estudiantes"][i2]["Notas"]):
                                    if grupos[i]["Estudiantes"][i2]["Notas"][index1]["modulo"] == mod:
                                        print("El camper ya tiene notas registradas de este modulo")
                                        os.system('pause')
                                        return
                                print(f'Notas a agregar en el modulo {mod}: ')
                                pteorica = int(input("Ingrese la nota de la prueba teorica: "))
                                ppractica = int(input("Ingrese la nota de la prueba practica: "))
                                qyt = int(0)
                                cont = int(0)
                                promqyt = int(0)
                                while True:
                                    qyt = int(input("Ingrese la nota de quices y trabajos: "))
                                    cont += 1
                                    promqyt += qyt
                                    opc = input("Desea agregar otra nota dentro quices y trabajos?(S/N): ").upper()
                                    if opc == "N":
                                        break
                                promqyt = promqyt / cont
                                notasmod = (pteorica * 0.3) + (ppractica*0.6) + (promqyt*0.1)
                                inf = {
                                    "modulo" : mod,
                                    "notas mod" : notasmod
                                }
                                grupos[i]["Estudiantes"][i2]["Notas"].append(inf)
                                if notasmod < 60:
                                    for i3, valor1 in enumerate(camper):
                                        if valor1["Id"] == id:
                                            if valor1["Estado"] == "En riesgo":
                                                camper[i3]["Estado"] = "Bajo rendimiento"
                                            else:
                                                camper[i3]["Estado"] = "En riesgo"
                                    print(f'El camper no aprobo el modulo de {mod}')
                                    os.system('pause')
                                else: 
                                    print(f'El camper aprobo el modulo de {mod}')
                                    os.system('pause')
                                
    #Cambia de FPOO A PWEB
    contador = int(0)
    for i, value in enumerate(grupos):
        for i2, valu in enumerate(grupos[i]["Estudiantes"]):
            for i3, val in enumerate(grupos[i]["Estudiantes"][i2]["Notas"]):
                if grupos[i]["Estudiantes"][i2]["Notas"][i3]["modulo"] == "FPOO":
                    contador += 1
                    if contador == len(grupos[i]["Estudiantes"]):
                        grupos[i]["Modulo"] = "PWEB"
    #Cambia de PWEB a PFORMAL
    contador = int(0)
    for i, value in enumerate(grupos):
        for i2, valu in enumerate(grupos[i]["Estudiantes"]):
            for i3, val in enumerate(grupos[i]["Estudiantes"][i2]["Notas"]):
                if grupos[i]["Estudiantes"][i2]["Notas"][i3]["modulo"] == "PWEB":
                    contador += 1
                    if contador == len(grupos[i]["Estudiantes"]):
                        grupos[i]["Modulo"] = "PFORMAL"
    #Cambia de PFORMAL A BD
    contador = int(0)
    for i, value in enumerate(grupos):
        for i2, valu in enumerate(grupos[i]["Estudiantes"]):
            for i3, val in enumerate(grupos[i]["Estudiantes"][i2]["Notas"]):
                if grupos[i]["Estudiantes"][i2]["Notas"][i3]["modulo"] == "PFORMAL":
                    contador += 1
                    if contador == len(grupos[i]["Estudiantes"]):
                        grupos[i]["Modulo"] = "BD"
    #Cambia de BD a BEND
    contador = int(0)
    for i, value in enumerate(grupos):
        for i2, valu in enumerate(grupos[i]["Estudiantes"]):
            for i3, val in enumerate(grupos[i]["Estudiantes"][i2]["Notas"]):
                if grupos[i]["Estudiantes"][i2]["Notas"][i3]["modulo"] == "BD":
                    contador += 1
                    if contador == len(grupos[i]["Estudiantes"][i2]["Notas"]):
                        grupos[i]["Modulo"] = "BEND"
    #Eliminar los que tienen estado bajo rendimiento
    for inde, valo in enumerate(grupos):
        for ind, valora in enumerate(grupos[inde]["Estudiantes"]):
            for ai, valf in enumerate(camper):
                if grupos[inde]["Estudiantes"][ind]["Id"] == id and valf["Id"] == id and valf["Estado"] == "Bajo rendimiento":
                    grupos[inde]["Estudiantes"].pop(ind)
                    print("El camper quedo en estado bajo rendimiento, por lo que fue eliminado del grupo")
                    os.system('pause')
                    savejsoncamper(camper)
                    savejsongrupos(grupos)
                    return
    savejsoncamper(camper)
    savejsongrupos(grupos)
        

def savejsoncamper(camper): 
    with open('camper.json', 'w') as json_file:
        json.dump(camper, json_file, indent=4)

def savejsongrupos(grupos):
    with open('grupos.json', 'w') as json_file:
        json.dump(grupos, json_file, indent=4)