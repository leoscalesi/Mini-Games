# Mini-Juegos
Aplicación de escritorio utilizando Python y MySql.

Esta vez les presento una aplicación de escritorio hecha con Python y su librería Tkinter.

La idea es implementarla en un futuro como una alternativa mas a los juegos que vienen por defecto instalados en los sistemas operativos,como
por ejemplo el solitario y el buscaminas.

Mi aplicación se divide en 4 minijuegos:

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
1-CALCULADORA DE IRRELEVANCIAS:

Nunca te pasó de ver en algún noticiero que una persona cayó de un determinado piso de un edificio, a veces con un triste desenlace, y preguntarte:

CON QUÉ VELOCIDAD HABRÁ LLEGADO ESA PERSONA AL PISO?
CUANTO TIEMPO TARDÓ EN LLEGAR AL PISO?

Bueno, yo si me lo pregunté, y con mi calculadora podrás tener una aproximación a estas dos cuestiones, 
utilizando las ecuaciones de Cinemática para un M.R.U.V. (movimiento rectilíneo uniformemente variado).

Lo bueno es que no necesitás poner ningún tipo de unidad ni nada por el estilo, solo deberás poner el número de piso desde el cual cayó la persona
y listo!! 

Se estima que cada piso tiene aproximadamente una altura de 2.5 metros.

La velocidad se expresa en km/h, y el tiempo en segundos.

Tambien tenemos una calculadora que dada una determinada profundidad, nos calcula cual es la presión en atmósferas a la que esta sometido un cuerpo, considerando 
que esta sumergido en agua.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------

2-QUINI SIX:

TENÉS LO QUE SE NECESITA PARA SER MILLONARIO?


En este juego, deberás seleccionar 6 números al azar entre el 0 y el 45, y sortear!!

Tanto los números seleccionados, la cantidad de aciertos y los números sorteados van a una base de datos, en caso de que te interese analizar algún tipo de patrón en los
sorteos.

En el archivo sorteos.txt se encuentra la query que deberás utilizar en MySql Workbench para crear la base de datos y la tabla correspondiente.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------


3-PREGUNTAS Y RESPUESTAS:


CUANTO SABES DE CULTURA GENERAL?


Se te harán 5 preguntas de cultura general, extraídas al azar de una base de datos. En el archivo preguntas.txt se encuentra la query para que puedas crear la base de 
datos, la tabla y puedas hacer la inserción de unas cuantas preguntas iniciales.

Las respuestas que debes dar son numéricas... BUENA SUERTE!!!



---------------------------------------------------------------------------------------------------------------------------------------------------------------------


4-APORTA TU GRANITO DE ARENA AL JUEGO DE PREGUNTAS Y RESPUESTAS


Podrás escribir una pregunta con su respuesta y al pulsar el boton enviar a base de datos se cargará automáticamente en la base correspondiente!!



---------------------------------------------------------------------------------------------------------------------------------------------------------------------


RECUERDA DESCARGARTE XAMMP Y MySql Workbench para así poder interactuar con las bases de datos, que deberás crear previamente usando las querys suministradas.
