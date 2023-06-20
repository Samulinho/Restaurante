def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut: "))
            if rut >= 1000000 and rut >= 9000000:
                return
            else:
                print("ERROR! El rut debe estar entre 1000000 y 9000000") 
        except:
            print("ERROR! Ingrese un numero entero")

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ") 
        if len(nombre.strip())>=3 and nombre.isalpha():
                return
        else:
             print("ERROR! el nombre debe tener al menos 3 caracteres!")

def validar_correo():
    while True:
        correo = input("Ingrese su correo: ")
        if "@" in correo:
            return
        else:
            print("ERROE! Correo incorrecto")

def vañidar_cantidad_personas():
    while True:
        try:
            cantidad_personas = int(input("Ingrese cantidad de personas que asistiran: "))
            if cantidad_personas >= 1 and cantidad_personas <= 6:
                return
            else:
                print("ERROR! Debe asistir al menos 1 persona y no mas de 6")
        except:
            print("ERROR! Debe ingresar un numero entero")

def validar_mesas():
    for x in range(3):
            print(f"Fila {x+1}:\t" , end="")
            for y in range(3):
                print(validar_mesas[x][y], end=" ")
            print()
    print("        1 2 3 ")
    print("         Mesas")
