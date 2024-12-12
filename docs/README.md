# Guía de Optimización y Análisis de una API con Instituciones Públicas de la Republica Dominicana

Este repositorio no solo actúa como una API que contiene todas las instituciones públicas Republica Dominicana, sino también como una guía práctica sobre cómo optimizar el rendimiento de aplicaciones sin necesidad de incrementar los recursos de hardware.

## Rendimiento Inicial

### Prueba Inicial
El primer resultado tras realizar pruebas de carga fue el siguiente:

![Primera Prueba](https://i.ibb.co/7NQ9Kmb/Primera-Prueba.png)

- **Carga:** 64 KB en formato JSON.
- **Concurrencia:** 1,000 usuarios simultáneos enviando 1,000 solicitudes.
- **Resultados:**
  - Tiempo total: 8 segundos.
  - Solicitudes fallidas: Ninguna.
  - Transferencia total: 65,015,000 bytes.

### Identificación de Áreas de Mejora
Se detectaron puntos clave a optimizar:

1. **Base de datos:** El uso de SQLite en su configuración inicial era inadecuado para un entorno asíncrono.
2. **Endpoint:** La implementación tenía un procesamiento sincronizado.
3. **Acceso a los datos:** Las solicitudes concurridas no eran manejadas eficientemente.

## Configuración Inicial de la Base de Datos
La configuración inicial de SQLite mostró limitaciones claras:

![Primera configDB](https://i.ibb.co/T1WcZRp/Config-DBV1.png)

- **Problemas:**
  - SQLite opera de manera sincrónica, lo que genera cuellos de botella en sistemas que utilizan frameworks asíncronos como FastAPI y servidores como Uvicorn.
  - La sesión no estaba optimizada para manejar solicitudes concurridas.

En el archivo `main.py`, se utilizaba un generador que accedía a los datos de forma sincrónica. Esto resultó en:

- Datos estáticos que no se actualizaban sin reiniciar el servidor, lo cual es válido para contenidos estáticos.
- Procesamiento sincrónico que afectaba la escalabilidad.

## Estrategias de Optimización

### Base de Datos

Se implementaron las siguientes mejoras:

1. **Uso de `sqlalchemy.ext.asyncio`:**
   - Permitimos consultas asíncronas hacia la base de datos.
2. **Optimización de PRAGMAs:**
   - Mejoramos el rendimiento ajustando configuraciones específicas de SQLite.
3. **Fábrica de sesiones:**
   - Creación de una fábrica de sesiones asíncronas para gestionar mejor las conexiones.

Nueva configuración:
![Nueva configDB](https://i.ibb.co/MkLPzLN/Config-DBV2.png)

### Obtención de Datos

Anteriormente, el acceso a los datos era sincrónico y estaba poco estructurado. Las mejoras incluyeron:

1. **Ejecución asíncrona:**
   - Reescritura del código para hacerlo limpio, escalable y completamente asíncrono.
2. **Caché:**
   - Incorporación de almacenamiento temporal para mejorar la eficiencia en consultas repetitivas.

![Mejora Obtención Datos](https://i.ibb.co/d2C1bgm/dump.png)

### Endpoint

Las mejoras en los endpoints incluyeron:

1. **Asíncronía total:**
   - Llamadas de datos asíncronas en todo el proceso.
2. **Especificación de JSON en la respuesta:**
   - Esto optimizó el procesamiento al reducir las transformaciones necesarias.
3. **Cabeceras HTTP:**
   - Agregado de `Content-Length` y `Cache-Control` para optimizar el manejo del contenido y el caché por parte del cliente.

Código optimizado del endpoint:
![Endpoint Optimizado](https://i.ibb.co/Hgr4dkf/main.png)

## Resultados Finales

Tras las optimizaciones, los resultados mejoraron significativamente:

![Resultado Final](https://i.ibb.co/3SpB4c1/Resultado-Final-Prueba.png)

- **Tiempo de respuesta:** 2 ms.
- **Procesamiento:** 479 solicitudes por segundo.
- **Concurrencia:** 1,000 usuarios simultáneos.
- **Comparación:**
  - Inicialmente: 8 segundos y 121 respuestas/segundo.
  - Tras la optimización: 2 ms y 479 respuestas/segundo.

## Conclusiones

- Las optimizaciones mostraron que es posible mejorar significativamente el rendimiento sin aumentar los recursos de hardware.
- SQLite, aunque no es ideal para entornos asíncronos, puede ajustarse con las configuraciones correctas.
- El manejo eficiente de caché y cabeceras HTTP contribuye al rendimiento global.

## Observaciones 

1. **Aprovechamiento del hardware:** El servidor de uvicorn en la forma que se ejecuto no aprovecha todo el potencial de los nucleos del CPU, el rendimiento podria aumentar si este se configura para esto..
2. **Cache:** El manejar el cache mediantes proxy o servidores como redis pueden aumentar notablemente el rendimiento de la aplicacion claro con un costo extra en recursos.
3. **Imagen Docker:** La imagen docker utilizada se puede optimizar para hacer las APIs mas eficiente como tecnicas como el `multi-stage` o usar imagenes `slim` .

Para mayor información sobre los resultados y los gráficos utilizados, consulta las URLs:

- [Primera Prueba](https://i.ibb.co/7NQ9Kmb/Primera-Prueba.png)
- [Primera Configuración de la Base de Datos](https://i.ibb.co/T1WcZRp/Config-DBV1.png)
- [Nueva Configuración de la Base de Datos](https://i.ibb.co/MkLPzLN/Config-DBV2.png)
- [Mejora en la Obtención de Datos](https://i.ibb.co/d2C1bgm/dump.png)
- [Endpoint Optimizado](https://i.ibb.co/Hgr4dkf/main.png)
- [Resultado Final](https://i.ibb.co/3SpB4c1/Resultado-Final-Prueba.png)

