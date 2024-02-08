import os
from ..funciones.mostrar import mcampersinscrito, mpruebainicialaprobado, mbajorendimiento, mtrainerycamper, maprobador
from .menuscruds import vertodostrainers
def menumostrar():
    while(True):
        os.system('cls')
        opc = int(input("1.MOSTRAR CAMPERS ESTADO INSCRITO \n2.MOSTRAR CAMPERS PRUEBA INICIAL \n3.LISTAR TRAINERS \n4.LISTAR ESTUDIANTES BAJO RENDIMIENTO \n5.LISTAR TRAINER Y CAMPERS \n6.MOSTRAR PERDIDOS Y APROBADOS, MODULO, RUTA Y TRAINER \n7.VOLVER \n:"))
        match(opc):
            case 1:
                mcampersinscrito()
            case 2:
                mpruebainicialaprobado()
            case 3:
                vertodostrainers()
            case 4:
                mbajorendimiento()
            case 5:
                mtrainerycamper()
            case 6:
                maprobador()
            case 7:
                break
            case _:
                print("Opcion invalida")
                menumostrar()