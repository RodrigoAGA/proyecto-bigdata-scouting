FACULTAD DE INGENIERÍA
CARRERA DE INGENIERÍA DE  SISTEMAS

Infraestructura para datos

Analítica con Big Data

Data Warehouses y Data Lakes

¿Qué es un Data Warehouse (DWH)?

"Un repositorio central de datos integrados, orientado al análisis histórico y la toma de
decisiones, provenientes de múltiples fuentes operacionales.”

W.H. Inmon (1992)

Dos enfoques arquitectónicos
Data Warehouse

Top Down vs Bottom Up
Ejemplo

Esquemas relacionales
Modelado dimensional

• Estrella: Consultas más rápidas, menos JOINS pero mayor redundancia de datos.

• Copo de nieve: Datos normalizados, menos redundancia, mayor complejidad en queries.

Ejemplo

Estrella

Copo de nieve

Actividad 1
Modelado dimensional para matrícula

• Realizar el modelado dimensional que permita análisis del sistema de

matrícula para la toma de decisiones. Ustedes debe de decidir las entidades
y sus atributos que formarán parte del datamart (facts, dimensiones).

Data Lake
Almacenamiento sin esquema previo

Repositorio centralizado que permite almacenar cualquier tipo de datos en su formato nativo
(estructurados, semiestructurados y no estructurados), a cualquier escala.

Data Lakehouse

• Paradigma moderno (popularizado por Databricks y Snowﬂake).

• Implementa la estructura y gobernanza de un DWH sobre la ﬂexibilidad y bajo

costo de un Data Lake.

• Es un Data Lake pero con una capa de metadatos:

• Log para nuevos datos

• Veriﬁcación de esquemas. Puede rechazar o actualizar esquemas.

• Puede guardar históricos de archivos.

Comparativa

Actividad 2 (guiada)

• Construcción de data lakehouse.

Procesamiento en Batch y En
Stream

Procesamiento batch
Por lotes

Procesa grandes volúmenes de datos recolectados durante un período de tiempo,
ejecutando el trabajo completo de una sola vez, sin interacción continua del usuario.

Procesamiento de Streams
Tiempo real

Procesa cada evento (o micro-batch) en cuanto llega, produciendo resultados
continuos con latencia de milisegundos a segundos.

Batch vs Stream: Comparativa
¿Cuándo usar cada uno?

