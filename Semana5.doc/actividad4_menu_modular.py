
def sumar_tupla(tup):
    """Suma todos los elementos de una tupla y retorna el valor."""
    return sum(tup)

def ejecutar_tuplas():
    print("\n--- SECCIÓN: TUPLAS ---")
    # 1. Crear tupla con al menos 5 elementos numéricos
    numeros = (12, 5, 33, 8, 20)
    print(f"Tupla de partida: {numeros}")
    
    # 2. Imprimir el tercer elemento (índice 2)
    print(f"El tercer elemento es: {numeros[2]}")
    
    # 3. Capturar dos números adicionales mediante input()
    try:
        num1 = int(input("Ingresa el primer número adicional: "))
        num2 = int(input("Ingresa el segundo número adicional: "))
    except ValueError:
        print("Entrada inválida, se usarán valores por defecto (0 y 0).")
        num1, num2 = 0, 0

    nueva_tupla = numeros + (num1, num2)
    print(f"Nueva tupla combinada: {nueva_tupla}")
    
    # 4. Convertir la tupla en lista, ordenarla y mostrarla
    lista_numeros = list(nueva_tupla)
    lista_numeros.sort()
    print(f"Lista ordenada: {lista_numeros}")
    
    # 5. Llamar a la función que suma los elementos
    resultado_suma = sumar_tupla(nueva_tupla)
    print(f"La suma total de los elementos de la tupla es: {resultado_suma}")


# 2.2 Uso de diccionarios
def buscar_telefono(dic_contactos, nombre):
    """Recibe un diccionario y un nombre, retornando el teléfono si existe."""
    if nombre in dic_contactos:
        return dic_contactos[nombre]
    return None

def ejecutar_diccionarios():
    print("\n--- SECCIÓN: DICCIONARIOS ---")
    # 1. Crear diccionario con al menos tres registros iniciales
    contactos = {
        "Ana": "555-0101",
        "Luis": "555-0102",
        "Mía": "555-0103"
    }
    
    # 2. Permitir la captura y adición de un nuevo contacto
    nuevo_nombre = input("Ingresa el nombre del nuevo contacto: ")
    nuevo_tel = input(f"Ingresa el número de teléfono para {nuevo_nombre}: ")
    contactos[nuevo_nombre] = nuevo_tel
    
    # 3. Iterar sobre las claves e imprimir exclusivamente los nombres
    print("Nombres de contactos registrados:")
    for nombre in contactos.keys():
        print(f"- {nombre}")
        
    # 4. Buscar contacto mediante la función modular
    nombre_a_buscar = input("¿Qué contacto deseas buscar en la agenda?: ")
    telefono = buscar_telefono(contactos, nombre_a_buscar)
    
    if telefono:
        print(f"¡Encontrado! El teléfono de {nombre_a_buscar} es: {telefono}")
    else:
        print("El contacto ingresado no se encuentra registrado.")


# 2.3 Uso de excepciones
def ejecutar_excepciones():
    print("\n--- SECCIÓN: EXCEPCIONES ---")
    try:
        num1 = int(input("Ingresa el primer número entero: "))
        num2 = int(input("Ingresa el segundo número entero: "))
        
        # División y manejo de cero
        division = num1 / num2
        suma = num1 + num2
        print(f"Suma de ambos números: {suma}")
        print(f"Resultado de la división ({num1} / {num2}): {division}")
        
    except ValueError:
        print("Error: Debes ingresar caracteres numéricos enteros válidos (sin dejar espacios vacíos).")
    except ZeroDivisionError:
        print("Error amigable: No es posible realizar una división entre cero. Ingresa un divisor distinto.")


# 2.4 Uso de strings
def contar_palabras(texto):
    """Recibe un string y retorna la cantidad de palabras que contiene."""
    return len(texto.split())

def ejecutar_strings():
    print("\n--- SECCIÓN: STRINGS ---")
    # 1. Crear variable de texto llamada mensaje
    mensaje = "Python es un lenguaje de programación excelente y muy versátil."
    print(f"Mensaje original: {mensaje}")
    
    # 2. Imprimir la longitud usando len()
    print(f"Longitud del string: {len(mensaje)}")
    
    # 3. Transformar a mayúsculas
    print(f"En mayúsculas: {mensaje.upper()}")
    
    # 4. Buscar y reemplazar una palabra clave
    mensaje_modificado = mensaje.replace("excelente", "poderoso")
    print(f"Mensaje modificado: {mensaje_modificado}")
    
    # 5. Función modular para contar palabras
    total_palabras = contar_palabras(mensaje)
    print(f"Cantidad de palabras en el mensaje: {total_palabras}")


# 2.5 Menú principal interactivo
def main():
    """Controla el flujo principal de la aplicación mediante un ciclo."""
    while True:
        print("\n==========================================")
        print("   ACTIVIDAD EVALUABLE 4 - MENÚ MODULAR")
        print("==========================================")
        print("1. Tuplas")
        print("2. Diccionarios")
        print("3. Excepciones")
        print("4. Strings")
        print("5. Finalizar")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            ejecutar_tuplas()
        elif opcion == "2":
            ejecutar_diccionarios()
        elif opcion == "3":
            ejecutar_excepciones()
        elif opcion == "4":
            ejecutar_strings()
        elif opcion == "5":
            print("¡Programa finalizado con éxito. Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona un número entre 1 y 5.")

if __name__ == "__main__":
    main()
