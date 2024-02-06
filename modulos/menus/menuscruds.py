import os
from ..funciones.crudcamper import crearcamper,eliminarcamper,actualizarcamper, vertodoscampers, veruncamper
from ..funciones.crudtrainer import creartrainer,eliminartrainer,actualizartrainer,vertodostrainers,veruntrainer
from ..funciones.crudruta import crearruta, eliminarruta, actualizarruta, vertodasrutas, verunaruta
from ..funciones.ceudgrupo import creargrupos, eliminargrupos, actualizargrupos
#Menu Camper
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
                actualizarcamper()
            case 4:
                opc1 = int(input("1.LISTAR TODOS LOS CAMPERS \n2.LISTAR UN CAMPER \n3. VOLVER \n:"))
                match(opc1):
                    case 1:
                        vertodoscampers()
                    case 2:
                        veruncamper()
                    case 3:
                        break
            case 5:
                break
            case _:
                print("Opcion invalida")
                mcamper()
#Menu Trainer
def mctrainer():
    while(True):
        os.system('cls')
        opc = int(input("1.CREAR TRAINER \n2.ELIMAR TRAINER \n3.EDITAR TRAINER \n4.BUSCAR TRAINER \n5.VOLVER \n:"))
        match(opc):
            case 1:
                creartrainer()
            case 2:
                eliminartrainer()
            case 3:
                actualizartrainer()
            case 4:
                opc1 = int(input("1.LISTAR TODOS LOS TRAINERS \n2.LISTAR UN TRAINER \n3. VOLVER \n:"))
                match(opc1):
                    case 1:
                        vertodostrainers()
                    case 2:
                        veruntrainer()
                    case 3:
                        break
            case 5:
                break
            case _:
                print("Opcion invalida")
                mctrainer()
#Menu Rutas
def mrutas():
    while(True):
        os.system('cls')
        opc = int(input("1.CREAR RUTAS \n2.ELIMAR RUTAS \n3.EDITAR RUTAS \n4.BUSCAR RUTAS \n5.VOLVER \n:"))
        match(opc):
            case 1:
                crearruta()
            case 2:
                eliminarruta()
            case 3:
                actualizarruta()
            case 4:
                opc1 = int(input("1.LISTAR TODAS LAS RUTAS \n2.LISTAR UNA RUTA \n3. VOLVER \n:"))
                match(opc1):
                    case 1:
                        vertodasrutas()
                    case 2:
                        verunaruta()
                    case 3:
                        break
            case 5:
                break
            case _:
                print("Opcion invalida")
                mrutas()
#Menu Grupos
def mgrupo():
    while(True):
        os.system('cls')
        opc = int(input("1.CREAR GRUPO \n2.ELIMAR GRUPO \n3.EDITAR GRUPO \n4.BUSCAR GRUPO \n5.VOLVER \n:"))
        match(opc):
            case 1:
                creargrupos()
            case 2:
                eliminargrupos()
            case 3:
                actualizargrupos()
            case 4:
                opc1 = int(input("1.LISTAR TODOS LOS GRUPOS \n2.LISTAR UN GRUPO \n3. VOLVER \n:"))
                match(opc1):
                    case 1:
                        vertodosgrupos()
                    case 2:
                        verungrupo()
                    case 3:
                        break
            case 5:
                break
            case _:
                print("Opcion invalida")
                mgrupo()
#Menu Principal
def menucr():
    os.system('cls')
    while(True):
        opc = int(input("1.CRUD CAMPER \n2.CRUD TRAINER \n3.CRUD RUTAS \n4.VOLVER \n:"))
        match(opc):
            case 1:
                mcamper()
            case 2:
                mctrainer()
            case 3:
                mrutas()
            case 4:
                break
            case _:
                print("Opcion invalida")
                menucr()
        