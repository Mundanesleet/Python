#Promedio Con ifs condicionales
print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, ¿Cual es tu nombre?: ")
print("Hola " + nombre + " vamos a realizar un promedio.")

mat = float(input(nombre + " ¿Cual es tu calificacion en matematicas?: "))
qui = float(input(nombre + " ¿Cual es tu calificacion en quimica?: "))
bio = float(input(nombre + " ¿Cual es tu calificacion en biologia?: "))

promedio = (mat + qui + bio) / 3

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,2))
else:
    print("Lo sentimos" + nombre + " has 'reprobado' con un promedio de: ", promedio)
    print("Lo sentimos" + nombre + " has 'reprobado' con un promedio de: ", round(promedio,1))
    

print("Fin")
