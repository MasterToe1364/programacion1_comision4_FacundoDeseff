platos = []
porciones = []
while True:
    print("\n--- Menu ---")
    print("1. Ingresar lista de platos.")
    print("2. Ingresar porciones disponibles.")
    print("3. Mostrar lista con platos y porciones")
    print("4. Consultar porciones de un plato.")
    print("5. Mostrar platos sin porciones.")
    print("6. Agregar un plato a la lista.")
    print("7. Gestionar Venta y Devolucion de porciones.")
    print("8. Salir del Menu")

    opcion = input("Ingrese una opcion del menu para realizar una accion: ")
    if not opcion.isdigit():
        print("Error: ingrese un opcion valida que se visualice en el menu.")
        continue
    match opcion:
        case "1":
            print("\n--- Ingresar lista de platos ---")
            lista_ingresada = input("Ingrese la lista de platos dividiendo cada item con una coma de por medio: ").strip()
            lista_temporal = lista_ingresada.split(",")
            for lista_nueva in lista_temporal:
                lista_limpia = lista_nueva.strip()
                platos.append(lista_limpia)
                porciones.append(0)
                print("La lista de platos fue agregada exitosamente.")
        case "2":
            print("\n--- Ingresar porciones disponibles ---")
            if not platos:
                print("No hay platos registrados en la lista.")
            else:
                for i in range(len(platos)):
                    cantidad_porciones = input(f"Ingrese la cantidad de porciones para {platos[i]}: ")
                    if cantidad_porciones.isdigit():
                        numero_porciones = int(cantidad_porciones)
                        porciones[i] = numero_porciones
                    else:
                        print(f"Entrada no valida para {platos[i]}. Se mantendra el valor anterior {porciones[i]}.")
                print("\nTodas las porciones fueron agregadas exitosamente")
        case "3":
            print("\n--- Mostrar platos y porciones ---")
            if not platos:
                print("No hay platos registrados.")
            else:
                print("Platos y Porciones")
                for i in range(len(platos)):
                    print(f"- {platos[i]}: {porciones[i]} porciones")
        case "4":
            print("\n--- Consultar porciones de un plato ---")
            if not platos:
                print("No hay platos registrados.")
            else:
                plato_consulta = input("Ingrese el plato a consultar la cantidad de porciones: ").strip()
                if plato_consulta in platos:
                    indice = platos.index(plato_consulta)
                    print(f"El plato {plato_consulta} tiene {porciones[indice]} porciones.")
                else:
                    print("ERROR: El plato ingresado no se encontró en la lista.")
        case "5":
            print("\n--- Mostrar platos sin porciones ---")
            if not platos:
                print("No hay platos registrados.")
            else:
                platos_sin_porciones = False
                for i in range(len(platos)):
                    if porciones[i] == 0:
                        print(f"- {platos[i]}")
                        platos_sin_porciones = True
                if not platos_sin_porciones:
                    print("No hay platos registrados que no tengan porciones.")
        case "6":
            print("\n--- Agregar un plato a la lista ---")
            nuevo_plato = input("Ingrese el nuevo plato que quiere agregar a la lista: ").strip()
            numero_porciones = input(f"Ingrese la cantidad de porciones para agregarle a {nuevo_plato}: ")
            if nuevo_plato and nuevo_plato not in platos:
                if numero_porciones.isdigit() and int(numero_porciones) >= 0:
                    platos.append(nuevo_plato)
                    porciones.append(int(numero_porciones))
                    print(f"El nuevo plato ({nuevo_plato}) fue agregado a la lista de platos con exito.")
                else:
                    print("ERROR: El numero de porciones ingresado debe ser positivo o cero.")
            else:
                print("ERROR: El nuevo plato no puede estar vacio o ya esta en la lista de platos.")

        case "7":
            print("\n--- Gestion de venta y devoluciones de platos ---")
            if not platos:
                print("No hay platos registrados.")
            else:
                plato_modificar = input("Ingrese el nombre del plato a modificar sus porciones: ").strip()
                if plato_modificar in platos:
                    indice = platos.index(plato_modificar)
                    accion = input(f"Use V[Vender] o D[Devolucion] para {plato_modificar}: ").strip().lower()
                    if accion == "v":
                        if porciones[indice] > 0:
                            porciones[indice] -= 1
                            print(f"Venta exitosa, quedan {porciones[indice]} porciones para {plato_modificar}.")
                        else:
                            print(f"ERROR: No quedan porciones disponibles para {plato_modificar}")
                    elif accion == "d":
                        porciones[indice] += 1
                        print(f"La devolucion de la parcion fue exitosa. Quedaron {porciones[indice]} porciones disponibles para {plato_modificar}")
                    else:
                        print("ERROR: Opcion no valida, por favor ingrese (V / D)")
                else:
                    print(f"El plato {plato_modificar} no se encontro en la lista de platos.")
        case "8":
            print("\n--- Saliendo del menu ---")
            break
        case _:
            print("Error: opcion no valida, por favor ingrese un numero valido.")

