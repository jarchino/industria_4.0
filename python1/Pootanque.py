import time
import matplotlib.pyplot as plt


class Tanque:
    def __init__(self, capacidad_maxima):
        self.nivel = 0
        self.capacidad_maxima = capacidad_maxima
        self.niveles = []
        self.tiempos = []

    def llenar(self, paso=10, intervalo=1):
        for segundo in range((self.capacidad_maxima // paso) + 1):
            if self.nivel > self.capacidad_maxima:
                self.nivel = self.capacidad_maxima

            self.niveles.append(self.nivel)
            self.tiempos.append(segundo)

            print(f"Segundo {segundo}s - Nivel: {self.nivel} litros")
            time.sleep(1)
            self.nivel += paso

        print("¡Tanque lleno...!")

    def graficar(self):
        plt.plot(self.tiempos, self.niveles, marker= 'o')
        plt.title("Simulación de llenado de tanque")
        plt.xlabel("tiempo (segundos)")
        plt.ylabel("Nivel (litros)")
        plt.grid(True)
        plt.show()

#Simulación
tanque = Tanque(200)    #Se crea un tanque de 100 litros
tanque.llenar()         #Se llena poco a poco
tanque.graficar()       #Se muestra grafica del proceso