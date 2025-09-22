show = []
entradas = []

while True:
    print("\n--- Menu Principal ---")
    print("1. Ingresar shows.")
    print("2. Ingresar entradas por show.")
    print("3. Mostrar shows y sus entradas.")
    print("4. Consultar entrada de un show.")
    print("5. Listar los shows con entradas agotadas.")
    print("6. Agregar un show con sus entradas.")
    print("7. Gestionar ventas y devoluciones de entradas.")
    print("8. Salir del menu.")

    opcion = input("Ingrese una opcion del menu: ").strip()
    if not opcion.isdigit():
        print("Por favor intente de nuevo.")
        continue

    match opcion:
        case "1":
            print("\n--- Ingresar shows ---")
            ingreso_show = input("Ingrese los shows que quiera agregar separados entre comas: ").strip()
            lista_temporal = ingreso_show.split(",")
            for nueva_lista in lista_temporal:
                lista_limpia = nueva_lista.strip()
                show.append(lista_limpia)
                entradas.append(0)
            print("Los shows fueron agregados a la lista exitosamente!!")

        case "2":
            print("\n--- Ingresar las entradas de cada show ---")
            if not show:
                print("No hay shows registrados en la lista.")
            else:
                for i in range(len(show)):
                    entradas_ingresadas = input(f"Ingrese el numero de entradas para el show de ({show[i]}): ")
                    if entradas_ingresadas.isdigit():
                        numero_entradas = int(entradas_ingresadas)
                        entradas[i] = numero_entradas
                    else:
                        print(f"Entradas no valida para {show[i]}, el valor de las entradas no cambiará ({entradas[i]})")
                print("\n Todos los cupos fueron agregados exitosamente!!")
        case "3":
            print("\n--- Mostrar los shows con sus entradas ---")
            if not show:
                print("No hay shows registrados en la lista.")
            else:
                print("Shows / Entradas")
                for i in range(len(show)):
                    print(f"- {show[i]}: {entradas[i]} entradas")

        case "4":
            print("\n--- Consultar entradas de un show ---")
            if not show:
                print("No hay shows registrados en la lista.")
            else:
                eleccion_show = input("Ingrese el show al cual quiere consultar sus entradas: ").strip()
                if eleccion_show in show:
                    indice = show.index(eleccion_show)
                    print(f"El show {eleccion_show} tiene {entradas[indice]} entradas disponibles!")
                else:
                    print("El show ingresado no se encontro en la lista.")
        case "5":
            print("\n--- Listar los shows con entradas agotadas ---")
            if not show:
                print("No hay shows registrados en la lista.")
            else:
                show_sin_entradas = False
                for i in range(len(show)):
                    if entradas[i] == 0:
                        print(f"- {show[i]}: {entradas[i]} entradas")
                        show_sin_entradas = True
                if not show_sin_entradas:
                    print("Todos los shows tienen entradas disponibles")
        case "6":
            print("\n--- Ingresar un nuevo show a la lista y sus entradas ---")
            nuevo_show = input("Ingrese el nuevo show que quiera agregar a la lista: ").strip()
            nueva_entrada = input(f"Ingrese las entradas que desea asignarle al show ({nuevo_show}): ")
            if nuevo_show and nuevo_show not in show:
                if nueva_entrada.isdigit() and int(nueva_entrada) >= 0:
                    show.append(nuevo_show)
                    entradas.append(int(nueva_entrada))
                    print("Se agrego exitosamente el nuevo show y sus entredas!!")
                else:
                    print("Error: numero invalido, el numero debe ser positivo o cero.")
            else:
                print("Error: El nombre del show no puede estar vacio o ya esta agregada a la lista.")
        case "7":
            print("\n--- Gestion de ventas y devoluciones de entradas ---")
            if not show:
                print("No hay shows registrados.")
            else:
                entradas_modificar = input("Ingrese el show al cual quiere modificar sus entradas: ").strip()
                if entradas_modificar in show:
                    indice = show.index(entradas_modificar)
                    accion = input("Ingrese V[Vender] o D[Devolver] una entrada: ").strip().lower()
                    if accion == "v":
                        if entradas[indice] > 0:
                            entradas[indice] -= 1
                            print(f"Venta exitosa, quedan {entradas[indice]} para ({entradas_modificar}).")
                        else:
                            print(f"Error: No quedan entradas disponibles para {entradas_modificar}")
                    elif accion == "d":
                        entradas[indice] += 1
                        print(f"La devolucion fue exitosa. Quedan {entradas[indice]} entradas para {entradas_modificar}")
                    else:
                        print("Error: Elija una opcion valida por favor.")
                else:
                    print(f"No se encontro {entradas_modificar} en la lista de shows.")
        case "8":
            print("\nSaliendo Del Menu...")
            break
        case _:
            print("Error: Por favor ingrese una opcion del menu.")
