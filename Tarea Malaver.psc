Proceso Tarea_Malaver
	Escribir 'Este programa calcula tres alternativas cilindro cono y esfera seleccione alternativa';
	Definir opcion como entero;
	Definir cilindro, cono, esfera como real;
	Escribir "Ingrese una alternativa a desarrollar:";
	Escribir "0: calcular el area de un cilindro";
	Escribir "1: calcular el area de un cono";
	Escribir "2: calcular el area de una esfera";
	Leer opcion;
	Segun opcion Hacer
		0:
				Definir P Como Real;
				P =3.1416;
				Definir radio, altura, volumen Como Real;
				Escribir "Ingrese el valor del radio: ";
				Leer radio;
				Escribir "Ingrese el valor de la altura: ";
				Leer altura;
				volumen = p * radio * radio * altura;
				Escribir "El volumen del cilindro es: ", volumen;
		1:
			Definir radio, altura, volumen Como Real;
			Definir P Como Real;
			P =3.1416;
			Escribir "Ingrese el valor del radio: ";
			Leer radio;
			Escribir "Ingrese el valor de la altura: ";
			Leer altura;
			volumen = (1/3) * p * radio * radio * altura;
			Escribir "El volumen del cono es: ", volumen;
		2:
			Definir radio, volumen Como Real;
			Definir P Como Real;
			P =3.1416;
			Escribir "Ingrese el valor del radio: ";
			Leer radio;
			volumen = (4/3) * p * radio * radio * radio;
			Escribir "El volumen de la esfera es: ", volumen;
		De Otro Modo:
			Escribir "opcion ivalidad";
	FinSegun
	
	
	
	
	
	
	
FinProceso
