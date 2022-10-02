#Menu
menu = '''
Bienvenidos al registro de usuarios, selecione un numero del 1 al 3
(1) DIGITE SU NOMBRE
(2) DIGITE SU EDAD
(3) DIGITAR SU CORREO ELECTRONICO
'''
print(menu)
opcion = input('Digite una opcion entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digite su nombre: ')
    if nombre.isalpha():
        print('Tu nombre es {} , mucho gusto!'.format(nombre))
    else:
            print('Escriba su nombre bien')

elif opcion == '2':
     edad = input('Digite su edad: ')
     if edad.isnumeric():
         print('Tu edad es {} años'.format(edad))
     else:
         print('Escriba su edad real, cobarde.')
elif opcion == '3':
    correo = input('Digite su correo: ')
    if correo.find('@') >= 0 and correo.find('.') >= 0:
        print('Tu correo electronico es {}'.format(correo))
    else:
        print('Escriba bien su correo, carajoooo')
else:
    print('Debes digitar un numero del 1 al 3')
print("Fin.")
