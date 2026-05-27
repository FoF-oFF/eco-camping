print("Gestión de Eco-Camping 'Bosque vivo'")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\n=== MENÚ DE CONTROL DE REGISTROS")
    print("1.- Ver sitios disponibles")
    print("2.- Registros de nuevos vehiculos en el sitio(Entrada)")
    print("3.- Registro de salida de vehículos(Salida)")
    print("4.- Estado actual del camping")
    print("5.- Salir")
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Error, seleccione entre 1 y 5")
        continue
    #opcion 1
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] Sitios libres para recibir vehículos: {disponibles}")
    #opcion 2
    elif opcion == 2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if sitios_libres == 0:
            print("Lo sentimos, no quedan espacios disponibles")
        else:
            try:
                ingreso = int(input("¿Cuantos sitios o vehículos van a ingresar?"))
                if ingreso <= 0:
                    print("Error, la cantidad de ingreso sebe ser mayor a 0")
                elif ingreso > sitios_libres:
                    print(f"Solo puede ingresar un máximo de {sitios_libres} sitios")
                else:
                    sitios_ocupados += ingreso
                    print(f"Ingreso registrado, se han ocupado {ingreso} de sitios")
            except ValueError:
                print("Error: debe ingresar un número válido")
    #opcion 3
    elif opcion == 3:
        print(f"\n-- registrar salida (vehículos o sitios ocupados: {sitios_ocupados})")
        if sitios_ocupados == 0:
            print("No hay vehículos registrados en el camping actualmente")
        else:
            try:
                salida = int(input("¿Cuantos vehículos se retiran?"))
                if salida <= 0:
                    print(f"Error: la cantidad a retirar debe ser mayor a 0")
                elif salida > sitios_ocupados:
                    print(f"Error: no se pueden retirar más de {sitios_ocupados} vehículos")
                else:
                    sitios_ocupados -= salida
                    print(f"Salida registrada, se han liberado {salida} sitios")
            except ValueError:
                print("Error: Debe ingresar un número entero válido")
    #opcion 4
    elif opcion == 4:
        porcentaje_ocupacion = (sitios_ocupados / capacidad_maxima) * 100
        print(f"\n[ESTADO] Ocupación actual: {sitios_ocupados}/{capacidad_maxima} sitios")
        print(f"[ESTADO] El camping esta al {porcentaje_ocupacion:.1f}% de su capacidad")
    elif opcion == 5:
        print("Cerrando el sistema")
        ejecutando = False
    else:
        print("Opción fuera de rango")
        