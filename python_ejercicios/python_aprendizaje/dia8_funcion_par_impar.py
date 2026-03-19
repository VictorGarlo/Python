def es_par(num):
    return num % 2 == 0
        
es_par(4) # True
es_par(5) # False

numeros = []
for i in range(5):
    numero = int(input("Ingresa un número: "))
    numeros.append(numero)
    
num_par = 0
for n in numeros:
    if es_par(n):
        num_par+=1
    
print(f"Hay {num_par} números pares")