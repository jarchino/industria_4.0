nivel = 0
capacidad_maxima = 100

while nivel < capacidad_maxima:
    try:
        cantidad = int(input("¿Cuántos litros de agua se agrega al tanque?"))
        
        if cantidad < 0:
            print("Ingresa una cantidad positiva.")
            continue

        nivel += cantidad
        print(f"El nivel del tanque es {nivel} litros")

        if nivel > capacidad_maxima:
            print("Se alcanzo la capacidad maxima")
            nivel = capacidad_maxima
            continue

        if nivel >= 70 and nivel < capacidad_maxima:
            print("Casi lleno!")

    except ValueError:
        print("Entrada no válida. Ingresa un número.")
        continue

print("Tanque lleno. Fin del proceso.")
        