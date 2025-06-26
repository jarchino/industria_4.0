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

            print(f"Segundo {segundo}s - Nivel: {self.nivel} litros - Estado: {self.estado()}")
            time.sleep(intervalo)
            self.nivel += paso

        print("¡Tanque lleno...!")

    def descargar(self, paso=10, intervalo=1):
        print("\nIniciando vaciado del tanque...\n")
        segundos_base = self.tiempos[-1] + 1  # continuar desde último segundo registrado
        while self.nivel > 0:
            self.nivel -= paso
            if self.nivel < 0:
                self.nivel = 0

            self.niveles.append(self.nivel)
            self.tiempos.append(segundos_base)
            print(f"Segundo {segundos_base}s - Nivel: {self.nivel} litros - Estado: {self.estado()}")
            segundos_base += 1
            time.sleep(intervalo)

        print("¡Tanque vacío!\n")

    def estado(self):
        porcentaje = (self.nivel / self.capacidad_maxima) * 100
        if porcentaje == 0:
            return "Vacío"
        elif porcentaje <= 40:
            return "Bajo"
        elif porcentaje <= 70:
            return "Medio"
        elif porcentaje < 100:
            return "Alto"
        else:
            return "Lleno"

    def graficar(self):
        plt.plot(self.tiempos, self.niveles, marker='o')
        plt.title("Simulación de llenado y vaciado del tanque")
        plt.xlabel("Tiempo (segundos)")
        plt.ylabel("Nivel (litros)")
        plt.grid(True)
        plt.show()


# Simulación
tanque = Tanque(100)
tanque.llenar()
tanque.descargar()
tanque.graficar()
