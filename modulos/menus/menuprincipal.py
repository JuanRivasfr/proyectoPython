import os
import json
from .menuscruds import menucr,menugestion

def menu():
    

    
    while(True):
        os.system('cls')
        print("""+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++""")
        try:
            opc = int(input("1.ADMINISTRACION DE TRAINERS, CAMPERS Y RUTAS \n2.GESTION DE NOTAS Y GRUPOS \n3.MOSTRAR REGISTROS \n4.SALIR \n:"))
            match(opc):
                case 1:
                    menucr()
                case 2:
                    with open('camper.json', 'r') as json_file:
                        camper = json.load(json_file)

                    with open('trainer.json', 'r') as json_file1:
                        trainer = json.load(json_file1)

                    with open('rutas.json', 'r') as json_file2:
                        ruta = json.load(json_file2)
                        
                    if len(camper) == 0 or len(trainer) == 0 or len(ruta) == 0:
                        print("Primero debe crear una ruta, camper y trainer")
                        os.system('pause')
                    else:        
                        menugestion()
                case 3:
                    pass
                case 4:
                    break
                case _:
                    print("Opcion invalida")
                    menu()
        except ValueError:
            print("La opcion no esta habilitada")
            os.system('pause')
        