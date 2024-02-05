import os
import json
#Importa el json
with open('rutas.json', 'r') as json_file:
    ruta = json.load(json_file)
#Crea ruta
def crearruta(iaux = None):

    def fpoo():
        arrayauxfpoo = []
        while True:
            tema = input("Ingrese el tema a ver en Fundamentos de Programacion: ").upper()
            arrayauxfpoo.append(tema)
            cont = input("Desea agregar otro tema?(S/N)\n : ").upper()
            if cont == "N":
                return arrayauxfpoo
    
    def pweb():
        arrayauxpweb = []
        while True:
            tema = input("Ingrese el tema a ver en Programacion Web: ").upper()
            arrayauxpweb.append(tema)
            cont = input("Desea agregar otro tema?(S/N)\n : ").upper()
            if cont == "N":
                return arrayauxpweb
    
    def pformal():
        arrayauxpformal = []
        while True:
            tema = input("Ingrese el tema a ver en Programacion Formal: ").upper()
            arrayauxpformal.append(tema)
            cont = input("Desea agregar otro tema?(S/N)\n : ").upper()
            if cont == "N":
                return arrayauxpformal

    def bd():
        arrayauxbd = {
            "BDP": input("Ingrese la base de datos principal: ").upper(),
            "BDS": input("Ingrese la base de datos secundaria: ").upper()
        }
        return arrayauxbd

    def bend():
        arrayauxbend = []
        print("Que temas desea agregar al apartado Backend?")
        while True:
            opc = int(input("1.NetCore \n2.Spring Boot \n3.NodeJS \n4.Express \n5.Otro \n: "))
            match(opc):
                case 1:
                    arrayauxbend.append("NETCORE")
                case 2:
                    arrayauxbend.append("SPRING BOOT")
                case 3:
                    arrayauxbend.append("NODEJS")
                case 4:
                    arrayauxbend.append("EXPRESS")
                case 5:
                    arrayauxbend.append(input("Ingrese el tema que desea agregar: ").upper())
                case _:
                    print("Opcion no valida")
            sel = input("Desea agregar otro tema?(S/N): ")
            if sel == "N":
                return arrayauxbend
                

    inf = { 
        "Nombre": input("Ingrese el nombre de la ruta: ")
        }
    comun = input("Desea agregar el comun core?(S/N)\n : ").upper()
    if comun == "S":
        inf["FPOO"] = ["INTRODUCCION A LA ALGORITMIA", "PSEINT", "PYTHON"]
        inf["PWEB"] = ["HTML", "CSS", "BOOTSTRAP"]
        inf["PFORMAL"] = ["JAVA", "JAVASCRIPT", "C#"]
    elif comun == "N":    
        inf["FPOO"] = fpoo()
        inf["PWEB"] = pweb()
        inf["PFORMAL"] = pformal()
    else: 
        print("OPCION NO VALIDA")
        os.system('pause')
        crearruta()
    inf["BD"] = bd()
    inf["BEND"] = bend()

    for i, value in enumerate(ruta):
            if value["Nombre"] == inf["Nombre"]:
                print("Ya hay una ruta creada con el mismo nombre, por favor intente con otro")
                os.system('pause')
                return
            
    if iaux == None:
        ruta.append(inf)
        print(ruta)
        print("La ruta ha sido creada")
        savejson()
        os.system('pause')
        return
    else :
        return inf
#Elimina ruta
def eliminarruta():
    nombre = input("Ingrese el nombre de la ruta a eliminar: ")
    for i,value in enumerate(ruta):
        if value["Nombre"] == nombre:
            print(f'\nNombre: \n---------------------- \n{value["Nombre"]}')
            print("----------------------")
            for i1, val in (value).items():
                if i1 != "Nombre":
                    print(f'{i1}:')
                    print("----------------------")
                    for i2, val2 in enumerate(val):
                        print(val2)
                    print("----------------------")
            se = input("Esta seguro que desea eliminar la rurta?(S/N): ").upper()
            if se == "S":
                ruta.pop(i)
                print("La ruta ha sido eliminada")
                savejson()
                os.system('pause')
                return
            else:
                return
    print("No se encontro el camper con ese id")
    os.system('pause')
#Actualiza Camper
def actualizarcamper():
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
    with open('rutas.json', 'w') as json_file:
        json.dump(ruta, json_file, indent=4)