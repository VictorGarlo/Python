edad_1 = int(input("Introduce la primera edad: "))
edad_2 = int(input("Introduce la segunda edad: "))

if edad_1 > edad_2:
    print("La primera persona es mayor que la segunda.")
elif edad_2 > edad_1:
    print("La segunda persona es mayor que la primera.")
else:
    print("Las dos personas tienen la misma edad.")