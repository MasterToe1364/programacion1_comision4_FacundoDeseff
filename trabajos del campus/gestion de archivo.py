def cargar_productos(nombre_archivo="productos.txt"):
    """
    (Actividad 4)
    Carga los productos desde el archivo de texto a una lista de diccionarios.
    """
    productos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    
                    if len(partes) == 3:
                        producto = {
                            "nombre": partes[0],
                            "precio": float(partes[1]),
                            "cantidad": int(partes[2]) 
                        }
                        productos.append(producto)
    
    except FileNotFoundError:
        print(f"ADVERTENCIA: El archivo '{nombre_archivo}' no se encontró.")
        print("Se creará uno nuevo cuando guardes los cambios.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al cargar el archivo: {e}")
        
    return productos

def mostrar_productos(lista_productos):
    """
    (Actividad 2)
    Muestra los productos de la lista con el formato solicitado.
    """
    if not lista_productos:
        print("\nNo hay productos cargados en la lista.")
        return
        
    print("\n--- Lista de Productos ---")
    # (Actividad 2) Mostramos con el formato pedido
    for producto in lista_productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    print("--------------------------\n")

def agregar_producto(lista_productos):
    """
    (Actividad 3)
    Pide datos al usuario y agrega un nuevo producto a la lista EN MEMORIA.
    """
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese nombre del producto: ").strip()
    
    try:
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))
        
        # (Actividad 3) Creamos y agregamos el nuevo producto a la lista
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        lista_productos.append(nuevo_producto)
        print(f"¡Producto '{nombre}' agregado a la lista!")
        print("Recuerda guardar los cambios para que se actualice el archivo.")

    except ValueError:
        print("Error: El precio y la cantidad deben ser valores numéricos.")

def buscar_producto(lista_productos):
    """
    (Actividad 5)
    Busca un producto por nombre en la lista de diccionarios.
    """
    print("\n--- Buscar Producto ---")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    
    encontrado = False
    for producto in lista_productos:
        # Comparamos en minúsculas para que no sea sensible a may/min
        if producto['nombre'].lower() == nombre_buscar:
            print("\n¡Producto encontrado!")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"\nError: El producto '{nombre_buscar}' no se encontró.") [cite: 32]

def guardar_productos(lista_productos, nombre_archivo="productos.txt"):
    """
    (Actividad 6)
    Sobrescribe el archivo productos.txt con los datos de la lista de diccionarios.
    """
    print(f"\nGuardando {len(lista_productos)} productos en '{nombre_archivo}'...")
    try:
        # (Actividad 6) Abrimos en modo 'w' (write) para sobrescribir
        with open(nombre_archivo, "w") as archivo:
            for producto in lista_productos:
                # Convertimos el diccionario de nuevo al formato "nombre,precio,cantidad"
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print("¡Productos guardados exitosamente!")

    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

# --- Programa Principal (Menú) ---
def main():
    # 1. Cargamos los productos del archivo al iniciar
    lista_de_productos = cargar_productos()

    while True:
        print("\n===== GESTIÓN DE PRODUCTOS =====")
        print("1. Mostrar todos los productos (Actividad 2 y 4)")
        print("2. Agregar un producto (Actividad 3)")
        print("3. Buscar un producto (Actividad 5)")
        print("4. Guardar cambios y Salir (Actividad 6)")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_productos(lista_de_productos)
        
        elif opcion == '2':
            agregar_producto(lista_de_productos)
        
        elif opcion == '3':
            buscar_producto(lista_de_productos)
        
        elif opcion == '4':
            guardar_productos(lista_de_productos)
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            
if __name__ == "__main__":
    main()