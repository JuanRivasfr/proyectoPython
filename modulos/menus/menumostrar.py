import os
from ..funciones.mostrar import mcampersinscrito
def menumostrar():
    while(True):
        os.system('cls')
        opc = int(input("1.MOSTRAR CAMPERS ESTADO INSCRITO \n2.MOSTRAR CAMPERS PRUEBA INICIAL \n3.LISTAR TRAINERS \n4.LISTAR ESTUDIANTES BAJO RENDIMIENTO \n5.LISTAR TRAINER Y CAMPERS \n6.MOSTRAR PERDIDOS Y APROBADOS, MODULO, RUTA Y TRAINER \n:"))
        match(opc):
            case 1:
                mcampersinscrito()
            case 2:
                pass
            case 3:
                pass
            case _:
                print("Opcion invalida")
                menumostrar()