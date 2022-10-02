#numero par o impar

print("Vamos a ver si es par o impar")


nombre = input("Cual es tu nombre?: ")
num = int(input(nombre + " ingresa un número: "))

if num % 2 == 0:
    print(nombre + " el número " + str(num) + " es par ")
else:
    print(nombre + " el número " + str(num) + " es impar")
    
