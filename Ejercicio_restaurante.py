
import Funciones as fn


while True:
    print("""Menu
    1.Ver Restaurante
    2.Reservar Mesa
    3.Carta
    4.Pagar
    5.Cancelar
    6.Salir""")
    opcion = int(input("Ingrese una opcion: "))

    if opcion==1:
        fn.validar_mesas()
    elif opcion==2:
        fn.validar_rut()
        fn.validar_nombre()
        fn.validar_correo()
        fn.vañidar_cantidad_personas()
    elif opcion==3:
        fn.validar_rut()
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        break






