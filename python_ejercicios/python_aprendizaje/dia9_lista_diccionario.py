personas = [
    {"nombre": "Victor", "edad": 22},
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
]
mayores_25 = []
for persona in personas:
    #print(f"{persona['nombre']} tiene {persona['edad']} años")
    if persona["edad"] > 25:
        mayores_25.append(persona)
        #print(f"{persona['nombre']} tiene {persona['edad']} años")
print(mayores_25)