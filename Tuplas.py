#Tuplas

#Creación de una Listas las Duplas son inmutables no se realizan cambios, 

a = (1,2,3,4)
print(a)

#Operaremos como si fuese una lista

print(a[0])

print(a[0:2])

#No podemos concatenar al no poder modificar los valores. Tampoco usar el método append

#Podemos ver su tamaño

print(len(a))

#Podemos ver si un elemento está o no en una tupla

print(5 in a)

print(1 in a)

#Resumen, mismas funciones y sintaxis que las listas, pero sin poder alterar los valores o el tamaño

a =list(a)
print(a)

a.append(5)
print(a)