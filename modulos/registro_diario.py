# Matriz: 2 estaciones x 3 horas
# Cada fila es una estación, cada columna una hora
registro_pasajeros = [
    [100, 200, 150],  # Estación 1: 7AM, 8AM, 9AM
    [120, 250, 180]   # Estación 2: 7AM, 8AM, 9AM
]

# Tarea 1: Mostrar pasajeros por estación y hora
def mostrar_registro(matriz):
    for estacion in range(len(matriz)):
        print(f"Estación {estacion + 1}:")
        for hora in range(len(matriz[estacion])):
            print(f"  {hora + 7}:00 - {matriz[estacion][hora]} pasajeros")

# Tarea 2: Calcular total por estación
def total_por_estacion(matriz):
    totales = []
    for estacion in matriz:
        totales.append(sum(estacion))
    return totales

# Agregar una hora más (10 AM) a cada estación
def agregar_hora(matriz):
    for estacion in matriz:
        estacion.append(220)
    return matriz

# Calcular el promedio de pasajeros por hora
promedio = []
def promedio_hora(matriz):
    for j in range(len(matriz[0])):
        sum = 0
        for i in range(len(matriz)):
            sum += matriz[i][j]
        promedio.append((sum/len(matriz)))
    return promedio

# Encontrar la hora más ocupada de cada estación
hora_pico_list = []
def hora_pico_estacion(matriz):
    for estacion in matriz:
        hora_pico = estacion.index(max(estacion))
        hora_pico_list.append((hora_pico + 7))
    return hora_pico_list

print(agregar_hora(registro_pasajeros))
print(promedio_hora(registro_pasajeros))
print(hora_pico_estacion(registro_pasajeros))

# Ejemplo

# Agregar hora
def agregar_hora_2(matriz):
    for estacion in matriz:
        estacion.append(300)
    return matriz

print(agregar_hora_2(registro_pasajeros))

# Promedio de pasajeros por hora actualizado
print(promedio_hora(registro_pasajeros))

# Hora pico actualizada
print(hora_pico_estacion(registro_pasajeros))