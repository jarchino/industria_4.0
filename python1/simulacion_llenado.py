import time


nivel = 0
capacidad_maxima = 100

print("Iniciando llenado de tanque automático..... \n")

while nivel < capacidad_maxima:

    nivel += 10
    print(f"Llenando el tanque..... nivel actual {nivel} litros")

    if nivel == 70:
        print(f"El tanque está casi lleno")

    if nivel >= 100:
        print("Tanque lleno. Fin del proceso.")
        break
    time.sleep(1)