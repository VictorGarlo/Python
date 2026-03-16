numeros = []
suma_total = 0

for _ in range(5):
    numero = int(input("Indica tu número: "))
    numeros.append(numero)
    suma_total += numero

num_mayor = numeros[0]
num_menor = numeros[0]

for i in numeros:
    if i > num_mayor:
        num_mayor = i
    if i < num_menor:
        num_menor = i

print(f"Lista: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Número mayor: {num_mayor}")
print(f"Número menor: {num_menor}")