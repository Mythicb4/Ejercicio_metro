# Ejercicio 1: Lista de Estaciones
estaciones_linea_a = ["Industriales", "Poblado", "Aguacatala","Ayurá", "Envigado"]

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
estaciones_linea_a.append("Itagüí")
estaciones_linea_a.append("Sabaneta")
estaciones_linea_a.append("La Estrella")

# Llamar la funcion e imprimir

# Mostrar la primera y última estación
print(estaciones_linea_a[0])
print(estaciones_linea_a[-1])

# Buscar si una estación existe en la lista
estacion_buscar = input()

# Funcion para buscar estaciones
def buscar_estacion(buscar, lista_estaciones):
    for estacion in lista_estaciones:
        if estacion.lower() == buscar.lower():
            return "Se hallo la estacion", buscar

# Llamar a la funcion e imprimir
buscar = buscar_estacion(estacion_buscar, estaciones_linea_a)
print(buscar)