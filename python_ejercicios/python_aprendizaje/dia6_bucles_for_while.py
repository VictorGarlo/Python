num = int(input("Ingresa un número: "))
suma_total = 0

while num != 0:
    suma_total += num
    num = int(input("Ingresa otro número: "))

print(f"La suma total es: {suma_total}")