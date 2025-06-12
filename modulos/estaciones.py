# Ejercicio 1: Lista de Estaciones
estaciones_linea_a = ["San Antonio", "Alpujarra", "Exposiciones", "Industriales", "Poblado"]

# Tarea 1: Imprimir todas las estaciones
def mostrar_estaciones(lista_estaciones):
    for estacion in lista_estaciones:
        print(estacion)

# Tarea 2: Contar el número de estaciones
def contar_estaciones(lista_estaciones):
    return len(lista_estaciones)

# Llamar la funcion
cantidad = contar_estaciones(estaciones_linea_a)

# Imprimir
print(cantidad)

# Agregar estaciones
estaciones_linea_a.append("Aguacatala")
estaciones_linea_a.append("Ayurá")
estaciones_linea_a.append("Envigado")

# Mostrar la primera y última estación
print(estaciones_linea_a[0])
print(estaciones_linea_a[-1])

# Buscar si una estación existe en la lista
estacion_buscar = input()

# Funcion para buscar estaciones
def buscar_estacion(buscar, lista_estaciones):
    for estacion in lista_estaciones:
        if estacion.lower() == buscar.lower():
            print(f"Se hallo la estacion {buscar}")

# Llamar a la funcion e imprimir
buscar_estacion(estacion_buscar, estaciones_linea_a)


# Pruebas y Ejemplos

estaciones_linea_a.append("Itagüí")
estaciones_linea_a.append("Sabaneta")
estaciones_linea_a.append("La Estrella")

# Mostrar estaciones actualizadas
mostrar_estaciones(estaciones_linea_a)

# Mostrar primera y ultima estacion actualizada
print(estaciones_linea_a[0])
print(estaciones_linea_a[-1])

# Buscar si una estacion existe en la lista
buscar = input("Que estacion deseas buscar: ")
buscar_estacion(buscar, estaciones_linea_a)