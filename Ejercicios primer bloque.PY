#Ejercicios primer bloque

#Multiplica 5 y 7, y súmale 3 al resultado. Guárdalo en una variable y muéstralo por pantalla

a = 5
b = 7
c = a *b + 3
print(c)

#Di si el resultado de lo anterior es igual a 38 (usando booleanos)

print(c == 38)

#Introduce la edad de dos personas por teclado, y muestra por pantalla un texto similar a este "La edad de Ana es 27"

a = input()
b = input()

print("La edad de Ana es", a, "y la de Pablo es",b)

#Introduce dos números por teclado y determine si son iguales, distintos, mayor o menor uno de otro. 

a = input()
b = input()
c = int(a)
d = int(b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

#Mismo caso pero comparando el tamaño de dos cadenas de caracteres

a = input()
b = input()
c = len(a)
d = len(b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)