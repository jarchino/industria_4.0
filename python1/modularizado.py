import pandas as pd
import matplotlib.pyplot as plt

def leer_datos(nombre_archivo):
    """
    Lee un archivo CSV y muestra las primeras filas.
    Retorna un DataFrame con los datos.
    """
    df = pd.read_csv(nombre_archivo)
    print("Primeros datos:")
    print(df.head())
    return df

def mostrar_estadisticas(df):
    """
    Muestra un resumen estadístico del DataFrame y retorna el nivel máximo.
    """
    print("\nResumen estadístico:")
    print(df.describe())
    nivel_max = df["Nivel (litros)"].max()
    print(f"\nNivel máximo: {nivel_max} litros")
    return nivel_max

def tiempos_tanque_lleno(df, nivel_max):
    """
    Muestra los tiempos en los que el tanque estuvo lleno.
    """
    tiempos_lleno = df[df["Nivel (litros)"] == nivel_max]["Tiempo (s)"]
    print("\nTiempos en los que estuvo lleno:")
    print(tiempos_lleno.to_list())

def graficar_nivel(df):
    """
    Grafica el nivel del tanque en función del tiempo.
    Guarda la imagen como 'grafica_nivel_tanque.png'.
    """
    df.plot(x="Tiempo (s)", y="Nivel (litros)", marker='o', title="Nivel de tanque a lo largo del tiempo")
    plt.tight_layout()
    plt.savefig("grafica_nivel_tanque.png")
    plt.close()

def clasificar_estado(nivel, nivel_max):
    """
    Clasifica el estado del tanque según el porcentaje de llenado.
    """
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
        return "Lleno"

def agregar_estado(df, nivel_max):
    """
    Agrega una columna 'Estado' al DataFrame usando la función clasificar_estado.
    """
    df["Estado"] = df["Nivel (litros)"].apply(lambda x: clasificar_estado(x, nivel_max))

def mostrar_estados(df):
    """
    Muestra la cantidad de registros en cada estado y retorna el conteo ordenado.
    """
    estado_ordenado = ["Vacío", "Bajo", "Medio", "Alto", "Lleno"]
    conteo = df["Estado"].value_counts().reindex(estado_ordenado).fillna(0).astype(int)
    print("\nEstados del tanque:")
    print(conteo)
    return conteo

def mostrar_duracion(conteo):
    """
    Muestra la duración total y el porcentaje de tiempo en cada estado.
    """
    print("\nDuración total por estado (en segundos):")
    for estado, segundos in conteo.items():
        print(f"{estado}: {segundos} segundos")
    total = conteo.sum()
    print("\nPorcentaje por tiempo de estado")
    for estado, segundos in conteo.items():
        porcentaje = (segundos / total) * 100
        print(f"{estado}: {segundos} segundos ({porcentaje:.1f}%)")

def graficar_duracion(conteo):
    """
    Crea un gráfico de barras de la duración en segundos por estado.
    Guarda la imagen como 'grafica_duracion_estados.png'.
    """
    plt.bar(conteo.index, conteo.values, color='skyblue')
    plt.title("Duración total por estado del tanque")
    plt.xlabel("Estado del tanque")
    plt.ylabel("Duración (segundos)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("grafica_duracion_estados.png")
    plt.close()

def guardar_datos(df, nombre_archivo):
    """
    Guarda el DataFrame en un archivo CSV.
    """
    df.to_csv(nombre_archivo, index=False)

def main():
    archivo_entrada = "datos_tanque.csv"
    archivo_salida = "datos_tanque_estado.csv"

    df = leer_datos(archivo_entrada)
    nivel_max = mostrar_estadisticas(df)
    tiempos_tanque_lleno(df, nivel_max)
    graficar_nivel(df)
    agregar_estado(df, nivel_max)
    conteo = mostrar_estados(df)
    mostrar_duracion(conteo)
    graficar_duracion(conteo)
    guardar_datos(df, archivo_salida)

if __name__ == "__main__":
    main()
