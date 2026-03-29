while True:
    try:
        numero_1 = int(input("Escribe tu primer número: "))
        break
    except:
        print("Introduce un número válido")
    
while True:
    try:
        numero_2 = int(input("Escribe tu segundo número: "))
        break
    except:
        print("Introduce un número válido")
    
while True:
    operacion = (input("Escribe la operación que deseas realizar: "))
    if operacion in ["+", "-", "*", "/"]:
        break
    else:
        print("Introduce una operación válida(+,-,*,/)")

if numero_2 == 0 and operacion == "/":
    print("0 no es un número válido para dividir")
    exit()
    

def calcular_suma(numero_1, numero_2):
    resultado_suma = numero_1 + numero_2
    return resultado_suma

def calcular_resta(numero_1, numero_2):
    resultado_resta = numero_1 - numero_2
    return resultado_resta

def calcular_multiplicacion(numero_1, numero_2):
    resultado_multiplicacion = numero_1 * numero_2
    return resultado_multiplicacion

def calcular_division(numero_1, numero_2): 
    resultado_division = numero_1 / numero_2
    return resultado_division

if operacion == "+":
    print(calcular_suma(numero_1, numero_2))

elif operacion == "-":
    print(calcular_resta(numero_1, numero_2))

elif operacion == "*":
    print(calcular_multiplicacion(numero_1, numero_2))

elif operacion == "/":
    print(calcular_division(numero_1, numero_2))