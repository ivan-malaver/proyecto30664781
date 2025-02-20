#Condicionales if/else
#Sentencias condicionales IF/ELSE  
#Un condicional es una instrucción o grupo de instrucciones que se pueden ejecutar o no en función del valor de una condición. 
#De esta manera, controlaremos si la ejecución va por A o por B, 
#lo que nos ayudará a contemplar diferentes casos para cubrir el mayor número de escenarios posibles
#Depende de la condición del IF, tomará un camino u otro

a = 2
if a == 2:
    print("a vale 2")
else:
    print("a es distinto de 2")
    
#Podemos concatenar condiciones con los operadores lógicos and, or y not

nombre = "Ana"
edad = 28
ciudad = "Colombia"

if nombre == "Ana" and edad == 28 and ciudad == "Colombia":
    print("Su nombre es Ana, tiene 28 años y es de  Colombia ")
elif nombre == "Ana" and not edad == 28:
    print("Su nombre es Ana y no tiene 28 años")
elif nombre != "Ana" and edad == 28:      
    print("Su nombre no es Ana y tiene 28 años")
else:
    print("No se llama Ana ni tiene 28 años")
