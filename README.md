# RETO-6-POO

Excepciones en el reto 1.1: para el reto 1.1 solo habia puesto un pequeña verificacion manuel en el momento en el que se quiere dividir por cero, debido a la opcion de "ZeroDivisionError" en el maejo de expciones ya no seria necesario, adicional a eso en esta ocasion puse una validacion para el numero que se ingresa al incio sea valido y no algun otro caracter cuando esto no pasa, se le pregunta al usuario de nuevo por los numeros hasta que los ponga correctamente.

excepciones en el reto 1.2: Para este reto hice unas pruebas y me di cuenta que si en mi codigo anterior se ingresaban palabras con espacios no funcionaba, para esto use la funcion ".strip" adicional a eso me di cuenta que si ponia numeros palindromos tambien funcionaba entonces puse una excepcion igualmente para que solo toamra en cuenta palabras palindromas con la funciona ".isalpha"

Excepciones en el reto 1.3: En este caso use la misma funcion ".strip para eliminar los primeros y ultimos espacios que hayan, luego verificando que todos sean digitos con una fucniona parecida a la usada en el ejercicio anterior para verificar que todo lo ingreasado fueran numeros ".isdigit"

Excepciones en el reto 1.4: Para esta ocasion use las mismas exepciones, debido a que solo peudo usar nuemros use la exepcion para que el usuario solo peuda ingresar numero con la funcion ".isdigit", con esta sabre si el usuario ingreso alguna letra, despues convierto la 
 lista que da el usuario a "int" debido a que es al unica forma de sumar los numeros

 Excepciones reto 1.5: Para la ultiam aplicacion de la excepciones en el reto 1 use la misma funcion ".isalpha" para verificar que solo se introdujeran palabras o letras en la lista para encontrar anagramas


 Resumen: en cada uno de los codigos del reto 1 use "valueError" como excepcion en todas y adicional en la primera use la excepcion "ZeroDivisionError" prar evitar la divison entre 0, tambien en algunos casos use la funcion raise para saltar al except de una antes del break en caso de no tener la salida esperada; la verificacion mediante estas manera me ayudara a la eficacia de mis codigos y eviat validaciones manuales algo complejas.




"Explicit is better than implicit."
"Simple is better than complex."
