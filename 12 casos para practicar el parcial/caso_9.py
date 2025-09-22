herramientas = []
cantidad = []
while True:
    print("\n--- Menu Principal ---")
    print("1. Ingresar herramientas a la lista.")
    print("2. Ingresar la cantidad que hay de cada herramienta.")
    print("3. Mostrar las herramientas con su cantidad correspondiente.")
    print("4. Consultar la cantidad de una herramienta.")
    print("5. Mostrar las herramientas con cantidad (0)")
    print("6. Agregar una herramienta a la lista y la cantidad que desee.")
    print("7. Actualizar la cantidad de herramientas.")
    print("8. Salir del Menu.")
    
    opcion = input("Ingrese una opcion del menu: ").strip()
    if not opcion.isdigit():
        print("Error: Por favor ingrese un numero del menu.")
        continue
    match opcion:
        case "1":
            print("\n--- Ingrasar herramientas a la lista ---")
            ingresar_lista = input("Ingrese la cantidad de herramientas que desee agregar a la lista, separadas con una coma: ").strip()
            lista_temporal = ingresar_lista.split(",")
            for lista_nueva in lista_temporal:
                lista_limpia = lista_nueva.strip()
                herramientas.append(lista_limpia)
                cantidad.append(0)
            print("Las herramientas fueron agregadas a la lista con exito!!")
        case "2":
            print("\n--- Ingresar la cantidad de herramientas ---")
            if not herramientas:
                print("No se han registrado herramientas todavia.")
            else:
                for i in range(len(herramientas)):
                    ingresar_cantidad = input(f"Ingrese la cantidad de herramientas que desea agregar para {herramientas[i]}: ")
                    if ingresar_cantidad.isdigit():
                        numero_cantidad = int(ingresar_cantidad)
                        cantidad[i] = numero_cantidad
                    else:
                        print(f"Entrada no valida para {herramientas[i]}, la cantidad de esta herramienta no cambiara ({cantidad[i]})")
                print("Todas las herramientas fueron agregadas exitosamente!!")
        case "3":
            print("\n--- Mostrar las herramientas con su cantidad ---")
            if not herramientas:
                print("No se han registrado herramientas todavia.")
            else:
                print("Herramientas / Cantidad")
                for i in range(len(herramientas)):
                    print(f"- {herramientas[i]}: {cantidad[i]}")
        case "4":
            print("\n--- Consultar la cantidad que hay de una herramienta ---")
            if not herramientas:
                print("No hay herramientas registradas todavia.")
            else:
                consulta_herramienta = input("Ingrese el nombre de la herramienta a consultar: ").strip()
                if consulta_herramienta in herramientas:
                    indice = herramientas.index(consulta_herramienta)
                    print(f"La herramienta que usted consulta: {consulta_herramienta}, de esta herramienta hay: {cantidad[indice]}")
                else:
                    print("No se encontro la herramienta en la lista.")
        case "5":
            print("\n--- Mostrar las herramientas que no contengan disponibilidad ---")
            if not herramientas:
                print("No hay herramientas registradas todavia.")
            else:
                herramientas_sin_cantidad = False
                for i in range(len(herramientas)):
                    if cantidad[i] == 0:
                        print(f"- {herramientas[i]}: {cantidad[i]}.")
                    herramientas_sin_cantidad = True
                    if not herramientas_sin_cantidad:
                        print("No hay herramientas sin disponibilidad")
        case "6":
            print("\n--- Agregar una herramienta a la lista y su cantidad ---")
            nueva_herramienta = input("Ingrese el nombre de la nueva herramienta que desea agregar a la lista: ").strip()
            nueva_cantidad = input("Ingrese la cantidad que desea que contenga la nueva herramienta: ")
            if nueva_herramienta and nueva_herramienta not in herramientas:
                if nueva_cantidad.isdigit() and int(nueva_cantidad) >= 0:
                    herramientas.append(nueva_herramienta)
                    cantidad.append(int(nueva_cantidad))
                    print("La nueva herramienta y su disponibilidad fue agregada con exito a la lista!!")
                else:
                    print("Error: Numero invalido, por favor ingrese un numero positivo o cero.")
            else:
                print("Error: No puede agregar un espacio vacio, o esa herramienta ya se encuentra registrada en la lista.")
        case "7":
            print("\n--- Actualizar cantidad de disponibilidad de una herramienta ---")
            if not herramientas:
                print("No hay herramientas registradas todavia.")
            else:
                herramienta_modificar = input("Ingrese el nombre de la herramienta que desea modificar: ").strip()
                if herramienta_modificar in herramientas:
                    indice = herramientas.index(herramienta_modificar)
                    accion = input("Ingrese R[Retirar] o A[Agregar] una herramienta: ").strip().lower()
                    if accion == "r":
                        if cantidad[indice] > 0:
                            cantidad[indice] -= 1
                            print(f"Retiro exitoso, {herramienta_modificar}: {cantidad[indice]}")
                        else:
                            print("Error: No quedan herramientas disponibles para retirar")
                    elif accion == "d":
                        cantidad[indice] += 1
                        print(f"La nueva herramienta ({herramienta_modificar}) se agrego con exito!!")
                    else:
                        print("Error: Ingrese una opcion valida por favor.")
                else:
                    print(f"No se encontro {herramienta_modificar} en la lista.")
        case "8":
            print("Saliendo del Menu...")
            break
        case _:
            print("Error: Por favor ingrese un numero del menu.")