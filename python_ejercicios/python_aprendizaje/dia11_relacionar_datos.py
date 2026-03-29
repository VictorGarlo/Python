personas = [
    {"nombre": "Victor", "edad": 22},
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
]

def obtener_nombres_extremos(personas):
    edad_max = personas[0]["edad"]
    nombre_max = personas[0]["nombre"]
    edad_min = personas[0]["edad"]
    nombre_min = personas[0]["nombre"]

    for persona in personas:
        edad = persona["edad"]
        nombre = persona["nombre"]
        if edad > edad_max:
            edad_max = edad
            nombre_max = nombre
        if edad < edad_min:
            edad_min = edad
            nombre_min = nombre
    return {
        "mayor" : nombre_max,
        "menor" : nombre_min
    }
print(obtener_nombres_extremos(personas))