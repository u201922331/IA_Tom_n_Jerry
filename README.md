# IA_Tom_n_Jerry
Minijuego de Tom &amp; Jerry

## Miembros del Grupo:
- Stephano Morales Linares (u201912659)
- Natalia Melissa Maury Castañeda (u201816996)
- Nander Emanuel Melendez Huamanchumo (u201922331)

## I. Planteamiento del juego o planteamiento del problema a resolver 300 palabras máximo.
Se hará una simulación inspirada en la serie animada Tom y Jerry,  donde se pondrán a prueba en un versus de la inteligencia representando a Jerry y la fuerza bruta representando a Tom. Tom hará todo lo posible para atrapar a Jerry, sin importar con qué trampa u obstáculo se encuentre. Mientras que Jerry intentará llegar a su ratonera antes de que Tom lo atrape evitando trampas. Debido a esto, el algoritmo de Tom será diseñado para que solo tome en cuenta la ruta más corta a Jerry, no importa el tiempo de la ruta solo que sea la más corta. Por el otro lado, el algoritmo de Jerry está diseñado para encontrar la ruta más rápida y eficiente para llegar a su ratonera, evitando a Tom. Si Tom atrapa a Jerry, él habrá ganado y Jerry habrá perdido. Si Jerry llega antes a la ratonera, se salva y Tom pierde. 

## II. Fundamentación de cómo adapta o usa la técnica o el algoritmo de Inteligencia Artificial, explique las entradas el proceso y salida de acuerdo al problema puede usar una gráfica o arquitectura. (300 palabras máximo).
El algoritmo A* será utilizado para el movimiento de Jerry para que evite los obstáculos y llegue a su ratonera por la ruta más rápida posible. Y el algoritmo de Tom, también será el A*, pero no le importa evitar trampas, sólo la ruta más corta para atrapar a Jerry.

La tabla de las entradas y salidas del Algoritmo A*
Entrada:
- Matriz del mapa
- Posición Actual del personaje
- Objetivo

Salida:
- Nueva Posición Actual

Sobre los elementos de la tabla, la matriz del mapa contiene toda la información del mapa: camino libre, obstáculos, trampas, inicio de cada personaje y ratonera. Esta información es importante para poder saber qué camino está disponible, cuál evitar, etc. La posición actual del personaje se utiliza para poder calcular la distancia más corta desde donde está al objetivo usando la información del mapa. El objetivo depende de cada personaje: en el caso de Tom, su objetivo es Jerry por lo que recibe la posición actual de Jerry. En el caso de Jerry, su objetivo es llegar a la ratonera, por lo que recibe la posición de la ratonera. Finalmente, se obtiene la nueva posición actual, que es dónde se moverá el personaje, luego de ejecutar el algoritmo.

## III. Explicación de la heurística y de qué manera permite resolver el problema en cuestión (300 palabras máximo). 
La heurística que utilizamos para los algoritmos de Tom y Jerry es la de Afecto. Por un lado, Tom está impulsado por el hambre, y hará cualquier cosa con tal de atrapar a Jerry lo más pronto posible. Por lo tanto, elegirá el camino más corto sin importar que pase por una trampa. 

Por el otro lado, Jerry estará impulsado por el miedo, así que buscará también la ruta más corta para ir a su ratonera. Sin embargo, como es más inteligente, él no intentará pasar por las trampas para llegar a su ratonera y tratará de evitar a Tom cuando esté cerca de él. 

Las trampas tendrán un peso mucho mayor para Jerry cuando analize que camino usar, así que decidirá escoger ir por otro lado. En cambio Tom, tendrá esos lugares con menos peso, y así si lo ve más factible, va intentar pasar por las trampas. Asimismo, utilizamos la heurística de la distancia Manhattan para poder hallar el camino más corto, poniendo un peso más elevado cuando estés alejándote del destino, y menos peso si te estás acercando.


## IV. Detalles del código fuente de la aplicación: sí ha utilizado algún framework, especificar librerías si fuera el caso que está usando, API etc., todo lo que fuera necesario para poner en marcha su aplicación.
Para el proyecto, hemos decidido desarrollarlo en Python sin ninguna librería que ayude al algoritmo principal en sí. Pero, para la interfaz gráfica hemos utilizado una librería llamada Pygame, que nos otorga la facilidad de poder dibujar el juego de manera sencilla. Algunas herramientas que utilizamos para codear son: Visual Code, Jupyter Notebook, PyCharm y Github.


## V. Pruebas de uso, ejecución y descripción de las funcionalidades (3 a 5 capturas de pantalla)
Para poder ver el informe completo con las imágenes, entrar al link: https://docs.google.com/document/d/13A8yP4stbQnI2gLVnYFEmlXZaqoxvDABEbYoJ-iYU6g/edit?usp=sharing 
1.- En esta imagen es donde empieza todo. Tom está en su posición inicial que le hemos otorgado, igual que Jerry, y la ratonera. La ratonera es el cuadrado de color naranja, es donde Jerry tiene que ir. Tom, en cambio, tiene que atrapar a Jerry antes que llegue a su ratonera.

2.- Es un juego por turnos, así que van analizando por dónde ir cada vez que se mueven para llegar lo más pronto posible al destino de cada uno. Como se puede ver Tom ha pasado por trampas que son el color celeste y rojo, no le importo e igualmente pasó. Sin embargo, Jerry no quiso ir por las trampas porque era muy peligroso para él. Por ende, está rodeando los obstáculos para llegar a su destino.

3.- Acá se puede ver un ejemplo que a Tom no le importó pasar por una trampa, ya que solo quiere atrapar a Jerry no importa el costo y cómo de grave llegue a su destino.

4.- En esta imagen, se puede ver cuando Jerry llega a la ratonera a tiempo, antes de que lo atrapara Tom. Se puede ver que al medio del juego sale GANASTE!, eso significa que Jerry llegó a la ratonera. En cambio, si sale PERDISTE!, es que Tom atrapó a Jerry antes de que llegara a su destino.

5.- Este es otro ejemplo de otro mapa. Se puede confirmar que el algoritmo sirve para cualquier mapa.

## VI. Referencias bibliográficas (Lo necesario y lo que ha utilizado)
Cursos - Ciencia de Datos (31 de agosto del 2021). Algoritmo de Búsqueda Informada (Heurística) A-star / A-estrella / A [Archivo de video]. Youtube.https://www.youtube.com/watch?v=JvgKPtGKmao&ab_channel=Cursos-CienciadeDatos
