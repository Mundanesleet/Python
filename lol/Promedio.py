#Promedio
nombre = input("Cual es tu nombre?")
print("Hola" + nombre + "Vamos a realizar un promedio.")

mat = int(input("Cual es tu calificacion en matematicas?"))
qui = int(input("Cual es tu calificacion en quimica?"))
bio = int(input("Cual es tu calificacion en biologia?"))

resultado =  mat + qui + bio
promedio = resultado / 3

print("Felicidades " + nombre + "Tu promedio es: " + str(resultado))
