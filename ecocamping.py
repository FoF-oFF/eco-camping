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
    else:
        print("Opción fuera de rango")