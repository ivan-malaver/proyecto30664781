#Ejercicios bloques 2 y 3

#Un programa que lea dos números por teclado, los compare y diga cual es mayor.

a = input()
b = input()

a = int(a)
b = int(b)

if a > b:
    print("A es mayor que b")
elif b > a:
    print ("B es mayor que A")
else: 
    print("Son iguales")
    
#Un programa que lea un número por teclado, y que mientras no sea impar no termine

a = int(input())

while a % 2 == 0:
    print("El número",a,"es par, introduzca otro número")
    a = int(input())
print("El número",a,"es impar. Programa terminado")

#Cree un programa que muestre unas opciones y el usuario seleccione una por teclado. Las opciones son: Comparar dos números (ejercicio1), Leer un número impar (ejercicio2) y salir (terminar el programa)
#User while(True) para tener un menú infinito

print("Menu")
while(True):
    print("Escribe una opción: \n 1. Comparar dos números.\n 2.Introduzca un número impar\n 3.Terminar programa")
    opcion = input()
    if opcion == '1':
        print("Introduzca el primer número")
        a = input()
        print("Introduzca el segundo número")
        b = input()
        a = int(a)
        b = int(b)
        if a > b:
            print("A es mayor que b")
        elif b > a:
            print ("B es mayor que A")
        else: 
            print("Son iguales")
    elif opcion == '2':
        print("Introduzca un número")
        a = int(input())
        while a % 2 == 0:
            print("El número",a,"es par, introduzca otro número")
            a = int(input())
        print("El número",a,"es impar")
    elif opcion == '3':
        print("Terminando programa...")
        break
    else:
        print("Opción no disponible")    
        

#Crea un diccionario de libros con el título y año y recorre sus títulos con un bucle for

libros = {'Los pilares de la Tierra':'1989','El Codigo Da Vinci':'2003'}

for titulo in libros:
    print(titulo)
    
#Para el ejemplo anterior, recorre los años

for key in libros:
    print(libros[key])

#Lo mismo, pero mostrando tanto la clave como el valor

for key in libros:
    print(key, libros[key])
    
#Crea una lista de películas con el título, año y director, y muestra por pantalla los datos de la 3a posición

peliculas = []

a = {'titulo':'Star wars','año':'1977','director':'George Lucas'}
b = {'titulo':'El señor de los anillos','año':'2001','director':'Peter Jackson'}
c = {'titulo':'Psicosis','año':'1960','director':'Alfred Hitchcock'}

peliculas.append(a)
peliculas.append(b)
peliculas.append(c)

contador = 0
for pelicula in peliculas:
    if contador == 2:
        print(pelicula['titulo'], pelicula['año'], pelicula['director'])
    contador += 1
