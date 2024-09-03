celsius = float(input("Ingrese la temperatura en grados Celsius: "))

if celsius < 10:
    print("Hace frío")
elif 10 <= celsius <= 25:
    print("Esta templado")
elif celsius > 25:
    print("Hace calor")
