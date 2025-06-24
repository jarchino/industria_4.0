colores = ["rojo", "azul", "verde", "amarillo"]

for color in colores:
    print("color", color)

    
autos = {
    "marca":"honda",
    "modelo":"civic type R",
    "año":2020,
}

for clave in autos:
    print(clave, ":", autos[clave])

vehiculos=[
    {"marca":"honda", "modelo":"civic type R","año":2020},
    {"marca": "toyota", "modelo": "prius", "año":2024},
    {"marca":"mazda", "modelo":"mx-5", "año":2024}
]

for vehiculo in vehiculos:
    print(f"{vehiculo['marca']} {vehiculo['modelo']} ({vehiculo['año']})")

for vehiculo in vehiculos: 
    if vehiculo['año'] == 2024: #filtrar por año
        print(f"{vehiculo['marca']} {vehiculo['modelo']} ({vehiculo['año']})")

