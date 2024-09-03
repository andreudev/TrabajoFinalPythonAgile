print("Ingrese que desea hacer: ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")


opcion = int(input("Ingrese la opción: "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))


if opcion == 1:
    print("La suma es: ", num1 + num2)
elif opcion == 2:
    print("La resta es: ", num1 - num2)
elif opcion == 3:
    print("La multiplicación es: ", num1 * num2)
elif opcion == 4:
    if num2 == 0:
        print("No se puede dividir por cero")
    else:
        print("La división es: ", num1 / num2)
else:
    print("Opción inválida")
