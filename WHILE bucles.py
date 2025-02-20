#Introducción a los bucles. WHILE 
#La principal diferencia con el bucle FOR es que para el WHILE se ejecutá infinitas veces mientras la condición de 
#guarda del bucle no se cumpla. 
#Por ejemplo: De una lista con valores True y False, quiero que la recorra tantas veces como sea necesario 
#mientras el valor del elemento sea False, 
#y que me guarde en una variable su posición.  
#El funcionamiento es similar, pero se usa para casos en los que quieres que se cumpla una condición. 
#El bucle FOR se utiliza más orientado a recorrer una lista por completo y a operar con sus elementos.

#Bucle while 

#Ejecutará las instrucciones que tenga dentro mientras no se cumpla la condición de guarda del bucle

contador = 0
while contador < 10:
    contador += 1
    print("Iteración", contador)

#While=True combinado con break nos permite un bucle infinito mientras no se cumpla la condición

while True:
    print("Introduzca un valor mayor que 5")
    a = int(input())
    if a > 5:
        print("Es correcto")
       
    else:
        print("Es incorrecto, pruebe de nuevo")
        break