#Conjuntos

#Creación de un conjunto

a = {1,2,3,4}
print(a)

#No tienen índice, no podemos usar a[0]

#Podemos añadir valores y quitarlos, y ver su tamaño

print(len(a))

a.add(8)
a.remove(2)

print(a)


#Podemos ver si un elemento está o no en un conjunto

print(5 in a)

print(1 in a)
