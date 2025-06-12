from modulos import estaciones, pasajeros, registro_diario, tiquetes

# main.py
def mostrar_menu():
    print("\n=== Metro de Medellín ===")
    print("1. Ver estaciones")
    print("2. Ver pasajeros por hora")
    print("3. Calcular total de ventas")
    print("4. Ver recaudo por tipo de tiquete")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            estaciones.mostrar_estaciones(estaciones.estaciones_linea_a)
        elif opcion == "2":
            print("Pasajeros por hora:", pasajeros.pasajeros_por_hora)
        elif opcion == "3":
            total = tiquetes.calcular_recaudo(tiquetes.precios, tiquetes.ventas)
            print(f"Recaudo total: ${total}")
        elif opcion == "4":
            recaudo = tiquetes.ventas_por_tiquete(tiquetes.ventas, tiquetes.precios)
            print(f"Recaudo por tipo de tiquete:")
            for tipo, total in recaudo.items():
                print(f"${tipo.capitalize()}: {total}")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()