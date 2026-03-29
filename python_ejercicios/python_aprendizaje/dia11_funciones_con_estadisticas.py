personas = [
    {"nombre": "Victor", "edad": 22},
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
]

def obtener_estadisticas(personas):
    total_personas = len(personas)
    
    suma_edades = 0
    edad_max = personas[0]["edad"]
    edad_min = personas[0]["edad"]
    mayores_25 = 0

    for persona in personas:
        edad = persona["edad"]
        suma_edades += edad

        if edad > edad_max:
            edad_max = edad
        
        if edad < edad_min:
            edad_min = edad
        
        if edad > 25:
            mayores_25 += 1

    media = round(suma_edades / total_personas, 2)

    return {
        "media": media,
        "max": edad_max,
        "min": edad_min,
        "total": total_personas,
        "mayores_25": mayores_25
    }

stats = obtener_estadisticas(personas)

print(stats)