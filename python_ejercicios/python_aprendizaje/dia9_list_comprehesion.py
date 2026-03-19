personas = [
    {"nombre": "Victor", "edad": 22},
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
]
nombres = [persona["nombre"] for persona in personas if persona["edad"] > 25]
print(nombres)