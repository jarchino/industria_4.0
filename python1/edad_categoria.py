# Programa para determinar categoría de edad

edad = int(input("¿Cuál es tu edad? "))

if edad < 18:
    print("Eres menor de edad")
elif edad < 60:
    print("Eres adulto")
else:
    print("Eres adulto mayor")
