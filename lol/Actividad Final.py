#Actividad Final

#Numeros pares o impares
num = int(input("Introduce un numero: "))

if num % 2 == 0:
    print("El numero " + str(num) + " es par")
else:
    print("El numero " + str(num) + " es impar")

print("\n\n")
    
#Dias de vacaciones
print("Vamos a ver cuantos dias de vacaciones tienes!! ")
nombre = input("¿Cual es tu nombre?: ")
print("                    ")
print(nombre + " escribe la clave de tu departamento en letras minusculas\n" "No utilizes numero, Gracias")
print("No utilizes numeros, Gracias")
print("Ejemplo: clave uno, clave dos, clave tres")
print("                    ")
clave = input(str(nombre + " ¿Cual es la clave de tu departamento?: "))
print("                    ")

if clave == str("clave uno"):
    años = input(nombre + " digita en numero entero la cantidad de años que llevas trabajando aqui: ")
    if años == '1':
        print("                                          ")
        print(nombre + "Tienes 6 dias de vaciones ¡FELICIDADES!")
    elif años == '2':
        print("                                          ")
        print(nombre + " tienes 14 dias de vaciones ¡FELICIDADES!")
    elif años == '3':
        print("                                          ")
        print(nombre + " tienes 14 dias de vaciones ¡FELICIDADES!")
    elif años == '4':
        print("                                          ")
        print(nombre + " tienes 14 dias de vaciones ¡FELICIDADES!")
    elif años == '5':
        print("                                          ")
        print(nombre + " tienes 14 dias de vaciones ¡FELICIDADES!")
    elif años == '6':
        print("                                          ")
        print(nombre + " tienes 14 dias de vaciones ¡FELICIDADES!")
    elif años == '7':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")
    elif años == '8':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")
    elif años == '9':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")
    elif años >= '10':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")       
    else:
        print(nombre + " porfavor digita numeros enteros")
   
if clave == str("clave dos"):
    print("                                          ")
    años = input(nombre + " digita en numero entero la cantidad de años que llevas trabajando aqui: ")
    if años == '1':
        print("                                          ")
        print(nombre + " tienes 7 dias de vaciones ¡FELICIDADES!")
    elif años == '2':
        print("                                          ")
        print(nombre + " tienes 15 dias de vaciones ¡FELICIDADES!")
    elif años == '3':
        print("                                          ")
        print(nombre + " tienes 15 dias de vaciones ¡FELICIDADES!")       
    elif años == '4':
        print("                                          ")
        print(nombre + " tienes 15 dias de vaciones ¡FELICIDADES!")       
    elif años == '5':
        print("                                          ")
        print(nombre + " tienes 15 dias de vaciones ¡FELICIDADES!")
    elif años == '6':
        print("                                          ")
        print(nombre + " tienes 15 dias de vaciones ¡FELICIDADES!")
    elif años == '7':
        print("                                          ")
        print(nombr + " tienes 22 dias de vaciones ¡FELICIDADES!")
    elif años == '8':
        print("                                          ")
        print(nombr + " tienes 22 dias de vaciones ¡FELICIDADES!")
    elif años == '9':
        print("                                          ")
        print(nombre + " tienes 22 dias de vaciones ¡FELICIDADES!")
    elif años >= '10':
        print("                                          ")
        print(nombre + " tienes 22 dias de vaciones ¡FELICIDADES!")       
    else:
        print(nombre + " Porfavor digita numeros enteros")

        
if clave == str("clave tres"):
    print("                                          ")
    años = input(nombre + " digita en numero entero la cantidad de años que llevas trabajando aqui: ")
    if años == '1':
        print("                                          ")
        print(nombre + " tienes 10 dias de vaciones ¡FELICIDADES!")
    elif años == '2':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")
    elif años == '3':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")       
    elif años == '4':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")       
    elif años == '5':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")
    elif años == '6':
        print("                                          ")
        print(nombre + " tienes 20 dias de vaciones ¡FELICIDADES!")
    elif años == '7': 
        print("                                          ")
        print(nombre + " tienes 30 dias de vaciones ¡FELICIDADES!")
    elif años == '8':
        print("                                          ")
        print(nombre + " tienes 30 dias de vaciones ¡FELICIDADES!")
    elif años == '9':
        print("                                          ")
        print(nombre + " tienes 30 dias de vaciones ¡FELICIDADES!")
    elif años >= '10':
        print("                                          ")
        print(nombre + " tienes 30 dias de vaciones ¡FELICIDADES!")       
    else:
        print(nombre + " Porfavor digita numeros enteros")

print("\n\n")

#El mayor numero
print("Vamos a ver cual es el mayor de todos!!")
numeros = []

for m in range(3):
  numero = float(input("Introduce el número #{}: ".format(m + 1)))
  numeros.append(numero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("El mayor numero es: ", mayor)
print("\n\n")

#Sucesion de fibonacci
print("Veamos la secuencia de Fibonacci")
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n
for i in range(18):
    print(fib(i))



print("\n\n")


 



    


 
