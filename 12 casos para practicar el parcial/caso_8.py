instrumentos = []
unidades = []

while True:
    print("\n--- Menu Principal ---")
    print("1. Ingresar instrumentos a la lista.")
    print("2. Agregar unidades disponibles para cada instrumento.")
    print("3. Mostrar los instrumentos con sus unidades.")
    print("4. Consultar las unidades de un instrumento.")
    print("5. Mostrar instrumentos que no tengan unidades disponibles.")
    print("6. Agregar un instrumento y sus unidades a la lista.")
    print("7. Actualizar unidades de los instrumentos.")
    print("8. Salir del Menu")

    opcion = input("Ingrese una opcion del Menú por favor: ").strip()
    if not opcion.isdigit():
        print("Error: Por favor ingrese un numero del menu.")
        continue

    match opcion:
        case "1":
            print("\n--- Ingresar instrumentos a la lista ---")
            agregar_instrumentos = input("Ingrese los instrumentos que desea agregar a la lista separados con una coma entre sí: ").strip()
            lista_provisoria = agregar_instrumentos.split(",")
            for nueva_lista in lista_provisoria:
                lista_limpia = nueva_lista.strip()
                instrumentos.append(lista_limpia)
                unidades.append(0)
            print("La lista de instrumentos se agrego con exito!!")
        case "2":
            print("\n--- Agregar unidades disponibles para cada instrumento ---")
            if not instrumentos:
                print("No se registraron instrumentos todavia.")
            else:
                for i in range(len(instrumentos)):
                    ingresar_unidades = input(f"Ingrese la cantidad de unidades para {instrumentos[i]}: ")
                    if ingresar_unidades.isdigit():
                        numero_unidades = int(ingresar_unidades)
                        unidades[i] = numero_unidades
                    else:
                        print(f"Unidades no validas para {instrumentos[i]}, el numero de unidades no cambiara ({unidades[i]})")
                print("\nLas unidades fueron agregadas con exito!!")
        case "3":
            print("\n--- Mostrar instrumentos con sus unidades ---")
            if not instrumentos:
                print("No se han registrado instrumentos todavia.")
            else:
                print("Instrumentos / Unidades")
                for i in range(len(instrumentos)):
                    print(f"- {instrumentos[i]}: {unidades[i]} unidades")
        case "4":
            print("\n--- Consultar unidades de un instrumento ---")
            if not instrumentos:
                print("No hay instrumentos registrados todavia.")
            else:
                instrumento_consulta = input("Ingrese el instrumento al cual quiere consultar sus unidades: ").strip()
                if instrumento_consulta in instrumentos:
                    indice = instrumentos.index(instrumento_consulta)
                    print(f"El instrumento {instrumento_consulta} contiene {unidades[indice]} unidades.")
                else:
                    print(f"El instrumento {instrumento_consulta} no se encontro en la lista.")
        case "5":
            print("\n--- Mostrar instrumentos que no tengan unidades disponibles ---")
            if not instrumentos:
                print("No se han registrado instrumentos todavia.")
            else:
                instrumentos_sin_unidades = False
                for i in range(len(instrumentos)):
                    if unidades[i] == 0:
                        print(f"- {instrumentos[i]}: {unidades[i]} unidades.")
                        instrumentos_sin_unidades = True
                    if not instrumentos_sin_unidades:
                        print("No hay instrumentos registrados que no contengan unidades!")
        case "6":
            print("\n--- Ingresar un nuevo instrumento a la lista con sus unidades disponibles ---")
            nuevo_instrumento = input("Ingrese el nuevo instrumento que desea ingresar a la lista: ").strip()
            nueva_unidades = input(f"Ingrese la cantidad de unidades para el nuevo instrumento agregado ({nuevo_instrumento}): ")
            if nuevo_instrumento and nuevo_instrumento in instrumentos:
                if nueva_unidades.isdigit() and int(nueva_unidades) >= 0:
                    instrumentos.append(nuevo_instrumento)
                    unidades.append(int(nueva_unidades))
                    print("El nuevo instrumento y sus unidades fueron agregadas a la lista de forma exitosa!!")
                else:
                    print("Error: Numero invalido, el numero debe ser positivo o cero.")
            else:
                print("Error: No puede agregarse un espacio vacio, o el nuevo instrumento ya se encuentra registrado en la lista.")
        case "7":
            print("\n--- Actualizar unidades de los instrumentos ---")
            if not instrumentos:
                print("No hay instrumentos registrados todavia.")
            else:
                instrumento_modificar = input("Ingrese el nombre del instrumento al cual le quiera modificar sus unidades: ").strip()
                if instrumento_modificar in instrumentos:
                    indice = instrumentos.index(instrumento_modificar)
                    accion = input("Ingrese R[Retirar] o A[Agregar] para las unidades de los instrumentos: ").strip().lower()
                    if accion == "r":
                        if unidades[indice] > 0:
                            unidades[indice] -= 1
                            print(f"Retiro exitoso, quedan {unidades[indice]} unidades disponibles para: {instrumento_modificar}")
                        else:
                            print(f"Error: No quedan unidades disponibles para: {instrumento_modificar}")
                    elif accion == "a":
                        unidades[indice] += 1
                        print(f"Agregado con exito, quedan {unidades[indice]} unidades disponibles para: {instrumento_modificar}")
                    else:
                        print("Error: Elija una opcion valida por favor.")
                else:
                    print(f"No se encontro {instrumento_modificar} en la lista.")
        case "8":
            print("Saliendo del Menú...")
            break
        case _:
            print("Error: Numero invalido, por favor intente nuevamente.")