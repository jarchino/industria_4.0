import time
import matplotlib.pyplot as plt


niveles = []
tiempos = []


nivel = 0
capacidad_maxima= 100


print("Iniciando llenado automático de tanque....\n")

for segundo in range(11):
    if nivel > capacidad_maxima:
        nivel = capacidad_maxima

    niveles.append(nivel)
    tiempos.append(segundo)

    print(f"Segundo {segundo}s - Nivel: {nivel} litros")
    time.sleep(1)
    nivel += 10


print("\n Llenado de tanque completo. Generando grafico...")

plt.plot(tiempos, niveles, marker= 'o')
plt.title("Simulación de llenado de tanque")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Nivel (litros)")
plt.grid(True)
plt.show()