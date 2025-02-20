# Definimos una función llamada "validar_numeros" que recibe dos parámetros: "a" y "b".
def validar_numeros(a, b):
    # Usamos una estructura condicional para comparar si "a" es igual a "b".
    if a == b:
        # Si son iguales, retornamos True.
        return True
    else:
        # Si no son iguales, retornamos False.
        return False

# Solicitamos al usuario que ingrese un número y lo convertimos a entero.
print("Introduzca un número")
a = int(input())

# Solicitamos al usuario que ingrese otro número y lo convertimos a entero.
print("Introduzca otro número")
b = int(input())

# Llamamos a la función "validar_numeros" pasando los dos números ingresados como argumentos y almacenamos el resultado en "resultado".
resultado = validar_numeros(a, b)

# Usamos una estructura condicional para verificar el valor de "resultado".
if resultado:
    # Si "resultado" es True, imprimimos "Son iguales".
    print("Son iguales")
else:
    # Si "resultado" es False, imprimimos "Son distintos".
    print("Son distintos")