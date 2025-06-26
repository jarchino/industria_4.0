import pandas as pd


#leer archivo csv
df = pd.read_csv("datos_tanque.csv")

#mostrar las primeras filas
print("primeros datos: ")
print(df.head())

#Estadisticas generales
print("\nResumen estadisticos:")
print(df.describe())

#Nivel maximo alcanzado
nivel_max = df["Nivel (litros)"].max()
print(f"\nNivel máximo: {nivel_max} litros")

#Tiempo en el que se estuvo lleno
tiempos_lleno = df[df["Nivel (litros)"] == 100]["Tiempo (s)"]
print("\nTiempos en los que estuvo lleno:")
print(tiempos_lleno.to_list())
