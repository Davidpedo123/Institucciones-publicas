# API de Instituciones Públicas y Guía de Optimización

Este repositorio, además de ser una API que proporciona información sobre todas las instituciones públicas, sirve como una guía práctica para optimizar el rendimiento de aplicaciones sin necesidad de aumentar recursos de hardware, instancias adicionales o servidores de caché.

Detalles de la API

URL: https://institucciones-publicas-rd.onrender.com/api/instituciones

![Primera Prueba](https://i.ibb.co/5sBNcVT/Response-APIComplete.jpg)

Nota: Las pruebas de rendimiento se realizaron en un entorno local. El servidor desplegado tiene recursos limitados.

# Rendimiento Inicial


Al inicio del proyecto, este era el tiempo de respuesta de la API tras realizar pruebas de carga:

![Primera Prueba](https://i.ibb.co/7NQ9Kmb/Primera-Prueba.png)

Tiempo total: 8 segundos.

Procesamiento: 121 respuestas por segundo.

Carga: 1,000 usuarios concurrentes.

# Resultado Final

Tras aplicar optimizaciones, los resultados mejoraron significativamente:

![Resultado Final](https://i.ibb.co/3SpB4c1/Resultado-Final-Prueba.png)

Tiempo de respuesta: 2 ms.

Procesamiento: 479 respuestas por segundo.

Carga: 1,000 usuarios concurrentes.

# Resultado final utilizando varios workers

![Resultado Final con CPU](https://i.ibb.co/m9SkKxj/Resultado-Final-Con-Uso-Del-Procesador.png)

Tiempo de respuesta: 0.69 ms.

Procesamiento: 692 respuestas por segundo.

Carga: 1,000 usuarios concurrentes.

Enlaces Relacionados

Guía de Optimización

