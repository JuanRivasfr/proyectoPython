import os
from .crudcamper import crearcamper,eliminarcamper

def mcamper():
    while(True):
        os.system('cls')
        opc = int(input("1.CREAR CAMPER \n2.ELIMAR CAMPER \n3.EDITAR CAMPER \n4.BUSCAR CAMPER \n5.VOLVER \n:"))
        match(opc):
            case 1:
                crearcamper()
            case 2:
                eliminarcamper()
            case 3:
                pass
            case 4:
                pass
            case 5:
                break
            case _:
                print("Opcion invalida")
                mcamper()
        

def menucr():
    os.system('cls')
    while(True):
        opc = int(input("1.CRUD CAMPER \n2.CRUD TRAINER \n3.CRUD RUTAS \n:"))
        match(opc):
            case 1:
                mcamper()
            case 2:
                pass
            case 3:
                pass
            case 4:
                break
            case _:
                print("Opcion invalida")
                menucr()
        