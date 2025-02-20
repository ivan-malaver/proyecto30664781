#Ejercicios Funciones

# Ejercicios Funciones

# 1. Crea un programa con una función que calcule el cuadrado de un valor dado (por teclado o directamente)

def cuadrado(a):
    """
    Calcula el cuadrado de un número.
    
    Parámetros:
        a (int o float): El número al que se le calculará el cuadrado.
    
    Retorna:
        int o float: El cuadrado del número.
    """
    return a * a  # Devuelve el cuadrado del número

a = 5  # Definimos un valor para 'a'
resultado = cuadrado(a)  # Llamamos a la función y guardamos el resultado
print(resultado)  # Mostramos el resultado (25, ya que 5 * 5 = 25)


# 2. Un programa con una función que reciba una lista, la procese y nos devuelva una nueva lista con cada elemento multiplicado por dos.

def multiplicar_lista(a):
    """
    Multiplica cada elemento de una lista por 2.
    
    Parámetros:
        a (list): La lista de números a procesar.
    
    Retorna:
        list: Una nueva lista con cada elemento multiplicado por 2.
    """
    for index, numero in enumerate(a):  # Recorremos la lista con su índice
        a[index] *= 2  # Multiplicamos cada elemento por 2
    return a  # Retornamos la lista modificada

numeros = [1, 2, 3, 4, 5]  # Definimos una lista de números
resultado = multiplicar_lista(numeros)  # Llamamos a la función y guardamos el resultado
print(resultado)  # Mostramos la lista modificada ([2, 4, 6, 8, 10])


# 3. Un programa que reciba dos números por teclado y los procese en una función y devuelva si son o no iguales.

def validar_numeros(a, b):
    """
    Compara dos números y determina si son iguales.
    
    Parámetros:
        a (int o float): El primer número.
        b (int o float): El segundo número.
    
    Retorna:
        bool: True si los números son iguales, False si no lo son.
    """
    if a == b:  # Comparamos los dos números
        return True  # Retornamos True si son iguales
    else:
        return False  # Retornamos False si son distintos

# Solicitamos dos números al usuario
print("Introduzca un número")
a = int(input())  # Leemos el primer número
print("Introduzca otro número")
b = int(input())  # Leemos el segundo número

# Llamamos a la función y guardamos el resultado
resultado = validar_numeros(a, b)

# Mostramos el resultado de la comparación
if resultado:
    print("Son iguales")  # Si son iguales
else:
    print("Son distintos")  # Si son distintos