import pandas as pd
import matplotlib.pyplot as plt


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
tiempos_lleno = df[df["Nivel (litros)"] == nivel_max]["Tiempo (s)"]
print("\nTiempos en los que estuvo lleno:")
print(tiempos_lleno.to_list())

df.plot(x="Tiempo (s)", y="Nivel (litros)", marker='o', title="Nivel de tanque a lo largo del tiempo")

plt.tight_layout() 
plt.savefig("grafica_nivel_tanque.png")
#plt.show() #Para mostrar
plt.close() #Para cerrar sin mostrar

def clasificar_estado(nivel):
    nivel_porciento = (nivel / nivel_max) * 100
    if nivel_porciento == 0:
        return "Vacío"
    elif nivel_porciento <= 40:
        return "Bajo"
    elif nivel_porciento <= 70:
        return "Medio"
    elif nivel_porciento < 100:
        return "Alto"
    else:
        return"Lleno"
    
#Creal columna estado
df["Estado"] = df["Nivel (litros)"].apply(clasificar_estado)

#Contar cuantas veces estuvo en cada estado
print("\nEstados del tanque: ")
estado_ordenado = ["Vacío","Bajo","Medio","Alto","Lleno"]
print(df["Estado"].value_counts().reindex(estado_ordenado).fillna(0).astype(int))

# Calcular duración total en cada estado
duraciones = df["Estado"].value_counts().reindex(estado_ordenado).fillna(0).astype(int)

print("\nDuración total por estado (en segundos):")
for estado, segundos in duraciones.items():
    print(f"{estado}: {segundos} segundos")

total = duraciones.sum()
print("\nPorcentaje por tiempo de estado")
for estado, segundos in duraciones.items():
    porcentaje = (segundos / total) * 100
    print(f"{estado}: {segundos} segundos ({porcentaje:.1f}%)")


df.to_csv("datos_con_estado.csv", index=False)
