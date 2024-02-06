import os
from .menuscruds import menucr,menugestion

def menu():
    while(True):
        os.system('cls')
        print("""+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++""")
        try:
            opc = int(input("1.CRUDS \n2.GESTOR DE MATRICULAS \n3.MOSTRAR R \n4.SALIR \n:"))
            match(opc):
                case 1:
                    menucr()
                case 2:
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
        