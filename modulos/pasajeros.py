# Ejercicio 2: Registro de Pasajeros
# Lista con el número de pasajeros por hora (6 AM a 10 AM)
pasajeros_por_hora = [100, 350, 500, 320, 150]

# Tarea 1: Calcular total de pasajeros
def calcular_total_pasajeros(lista_pasajeros):
    return sum(lista_pasajeros)

# Tarea 2: Encontrar hora más congestionada
def encontrar_hora_pico(lista_pasajeros):
    hora_pico = lista_pasajeros.index(max(lista_pasajeros))
    return hora_pico + 6  # Sumamos 6 porque empezamos a contar desde las 6 AM

# Calcular el promedio de pasajeros
suma = calcular_total_pasajeros(pasajeros_por_hora)
def promedio_pasajeros(suma, lista_pasajeros):
    return suma / len(lista_pasajeros)

# Encontrar la hora con menos pasajeros
def menos_pasajeros(lista_pasajeros):
    hora_baja = lista_pasajeros.index(min(lista_pasajeros))
    return hora_baja + 6

lista_mas_300 = []
def mas_300_pasajeros(lista_pasajeros):
    for pasajeros in lista_pasajeros:
        if pasajeros > 300:
            lista_mas_300.append((lista_pasajeros.index(pasajeros) + 6))
    return lista_mas_300

print(calcular_total_pasajeros(pasajeros_por_hora))
print(encontrar_hora_pico(pasajeros_por_hora))
print(promedio_pasajeros(suma, pasajeros_por_hora))
print(menos_pasajeros(pasajeros_por_hora))
print(mas_300_pasajeros(pasajeros_por_hora))

# Ejemplos

pasajeros_por_hora.append(400)
pasajeros_por_hora.append(350)

# Promedio de pasajeros
print(promedio_pasajeros(suma, pasajeros_por_hora))

# Hora con menos pasajeros
print(menos_pasajeros(pasajeros_por_hora))

# Horas con mas de 300 pasajeros
print(mas_300_pasajeros(pasajeros_por_hora))