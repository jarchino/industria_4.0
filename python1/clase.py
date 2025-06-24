vehiculos=[
    {"marca":"honda", "modelo":"civic type R","año":2020},
    {"marca": "toyota", "modelo": "prius", "año":2024},
    {"marca":"mazda", "modelo":"mx-5", "año":2024}
]

def mostrar_vehiculos_por_año(lista,año):
    for v in lista:
        if v['año'] == año:
            print(f"{v['marca']} {v['modelo']} ({v['año']})")
            
mostrar_vehiculos_por_año(vehiculos,2020)