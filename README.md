
Este repositorio aparte de ser una API que contiene todas las instituciones publicas, es una guia de como podemos optimizar el rendimiento de nuestros aplicativos sin tener que aumentar el hardware, sin agregar nuevas instancias o servidores de cache.

URL: https://institucciones-publicas-rd.onrender.com/api/instituciones
(las pruebas fueron hechas en local, el servidor en la que esta esta desplegada esta limitada)
Al inicio del proyecto este era el response de la API tras las pruebas.
![Primera Prueba](https://i.ibb.co/7NQ9Kmb/Primera-Prueba.png)

'Resultado Final'

![Primera configDB](https://i.ibb.co/3SpB4c1/Resultado-Final-Prueba.png)

2ms en el test, con una carga de 1k usuarios concurrentes procesando 479s por segundo.

Cuando anteriormente sin optimizar, tuvimos el primer resultado de 8s para culminar el test, con la misma carga, pero con 121 respuestas por segundo.
