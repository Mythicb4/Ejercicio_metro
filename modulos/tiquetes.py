# Lista de precios de diferentes tipos de tiquetes
precios = {
    "unitario": 2650,
    "integrado": 3400,
    "estudiante": 2450
}

# Lista de ventas por tipo
ventas = [10, 5, 8, 6]  # unitario, integrado, estudiante

# Tarea 1: Calcular el total recaudado
def calcular_recaudo(precios_tiquetes, cantidad_ventas):
    total = 0
    tipos = list(precios_tiquetes.keys())
    for i in range(len(tipos)):
        total += precios_tiquetes[tipos[i]] * cantidad_ventas[i]
    return total

# Agregar un nuevo tipo de tiquete
precios["turista"] = 4000

# Calcular el promedio de ventas
ventas_total = calcular_recaudo(precios, ventas)
def promedio_ventas(ventas_total, precios_tiquetes):
    tipos = list(precios_tiquetes.keys())
    return (ventas_total/len(tipos))

# Recaudo por tipo de tiquete
def ventas_por_tiquete(ventas_tiquete, precios_tiquetes):
    recaudo_por_tiquete = {}
    tipos = list(precios_tiquetes.keys())  # ["sencillo", "doble", "turista"]
    
    for i in range(len(ventas_tiquete)):
        tiquete = tipos[i]
        cantidad = ventas_tiquete[i]
        precio = precios_tiquetes[tiquete]
        recaudo = cantidad * precio
        recaudo_por_tiquete[tiquete] = recaudo

    return recaudo_por_tiquete

# Encontrar el tipo de tiquete más vendido
mas_vendido = list(precios.keys())[ventas.index(max(ventas))]

print(promedio_ventas(ventas_total, precios))
print(precios)
print(mas_vendido)

# Ejemplos

# Agregar un nuevo tipo de tiquete
precios["3ra_edad"] = 2000

# Calcular el promedio de ventas
ventas.append(23)
print(promedio_ventas(ventas_total, precios))

# Mas vendido actualizado
mas_vendido = list(precios.keys())[ventas.index(max(ventas))]
print(mas_vendido)