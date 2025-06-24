vehiculos=[
    {"marca":"honda", "modelo":"civic type R","año":2020},
    {"marca": "toyota", "modelo": "prius", "año":2024},
    {"marca":"mazda", "modelo":"mx-5", "año":2024}
]

# def mostrar_vehiculos_por_año(lista,año):
#     for v in lista:
#         if v['año'] == año:
#             print(f"{v['marca']} {v['modelo']} ({v['año']})")
            
# mostrar_vehiculos_por_año(vehiculos,2020)

# def mostrar_vehiculos_por_año(lista,año):
#     resultado =[]
#     for v in lista:
#         if v['año'] == año:
#             resultado.append(v)
#     return resultado

# vehiculos_filtrados = mostrar_vehiculos_por_año(vehiculos, 2024)

# for v in vehiculos_filtrados:
#     print(f"{v['marca']} {v['modelo']} ({v['año']})")

def mostrar_vehiculos_por_año(lista, año):
    resultado = [v for v in lista if v['año'] == año]
    resultado.sort(key=lambda x: x['marca'])  # ordena por marca
    return resultado
vehiculos_filtrados = mostrar_vehiculos_por_año(vehiculos, 2024)

for v in vehiculos_filtrados:
     print(f"{v['marca']} {v['modelo']} ({v['año']})")