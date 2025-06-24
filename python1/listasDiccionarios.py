#listas
colores = ["rojo", "azul", "verde", "amarillo"]
colores.append("cafe")

autos = {
    "marca":"honda",
    "modelo":"civic type R",
    "año":2020,
}

autos["año"] = 2022

print(colores)
print(autos)

frutas = ["manzana", "banana", "cereza"]
#print(frutas)          # Muestra toda la lista
#print(frutas[0])       # Muestra "manzana" (el primer elemento)

frutas.append("naranja")     # Agrega un elemento al final
frutas.remove("banana")      # Elimina un elemento específico
#print(len(frutas))           # Longitud de la lista
#print(frutas[-1])            # Último elemento

#diccionarios
persona = {
    "nombre": "Adrián",
    "edad": 25,
    "ciudad": "Culiacán"
}
#print(persona["nombre"])     # Muestra "Adrián"

persona["edad"] = 26         # Actualiza valor
persona["profesion"] = "Ingeniero"  # Agrega nueva clave-valor
del persona["ciudad"]        # Elimina una clave

