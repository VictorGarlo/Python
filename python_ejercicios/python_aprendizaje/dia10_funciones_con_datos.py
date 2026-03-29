personas = [
    {"nombre": "Victor", "edad": 22},
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
]

def obtener_nombres_mayores(personas, edad_minima):
    nombres = []
    for persona in personas:
        if persona["edad"] > edad_minima:
            nombres.append(persona["nombre"])
    return nombres
print(obtener_nombres_mayores(personas,25))