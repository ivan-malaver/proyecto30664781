#Con los bucles podremos procesar grandes cantidades de datos de manera automática. 
#El bucle ejecutará unas instrucciones X veces, hasta que la condición o el valor de salida del bucle se cumpla. 
#Ejemplo: Para una lista de 30 elementos, haremos que el bucle se ejecute desde 0 hasta 30, una por cada elemento, 
#y ejecute la suma de cada valor con su siguiente. 
#El bucle recorrerá la suma para cada posición de la lista y la guardará en una variable, que imprimiremos por pantalla al final.
#Bucle For 

#Nos permite recorrer una lista o diccionario

nombres = ['Ana', 'Pablo', 'Diego', 'Carmen']
#for nombre in nombres:
    #print(nombre)

#Para una lista de diccionarios

personas = []
a = {'nombre':'Ana', 'edad': 28 }
b = {'nombre':'Pablo', 'edad': 35}
c = {'nombre':'Luis', 'edad': 38 }

personas.append(a)
personas.append(b)
personas.append(c)

for persona in personas:
    print(persona['nombre'])
    print( persona['edad'])
    print( personas)
#Nos permite acceder a los valores del diccionario y operar con ellos. Por ejemplo para crear una nueva lista

lista_nombres = []

for persona in personas:
    lista_nombres.append(persona['nombre'])
print(lista_nombres)

#Podemos coger una lista de números y modificar cada valores

numeros = [1, 2, 3, 4, 5]

for index, numero in enumerate(numeros):
    numeros[index] += 3
print(numeros)


