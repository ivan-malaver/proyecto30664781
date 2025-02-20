#Listas

#Creación de una Listas

a = [1,2,3,4]
print(a)

#Operaremos como si fuese un basestring

print(a[0])

print(a[0:2])

#Concatenaremos lista con un otra lista o un número

b = [5,6]

print(a + b)

#Podemos sustituir el valor de una posición

a[3] = 'Hola'
print(a)

#Podemos usar el método append() para añadir un elemento

a.append(3)

print(a)

#Al igual que en los strings, podemos usar el método len()

print(len(a))

#Podemos ver si un elemento está o no en una lista

print(5 in a)

print(1 in a)
