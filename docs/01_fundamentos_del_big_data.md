FACULTAD DE INGENIERÍA
CARRERA DE INGENIERÍA DE SISTEMAS
Concepto Introductorios y
Fundamentos del Big Data
Analítica con Big Data

Presentación del Curso

Presentación
•
https://www.youtube.com/watch?v=I8Wny1ZEG8I

Horas de asesoría
•
Lunes 5pm-6pm
•
Martes 4pm-5pm
•
Miercoles 5pm-6pm
•
Jueves 6pm-7pm (Solo Virtual)
Lugar: Laboratorio ITLAB (piso 2 pabellón I2)
Zoom (*): https://ulima-edu-pe.zoom.us/j/95728854972?
pwd=dGtQU2JhSUh4WmhMMHl4Ykt1cnZEUT09
(*) Se dará preferencia a las visitas presenciales.

Normas
•
Se tomará lista a 20 minutos de iniciada la clase y también al final.
•
No estar en alguna lista invalida su asistencia.
•
No se puede justificar inasistencias, a no ser por lo siguiente:
•
Faltar más de 1 semana (con secretaría académica)
•
Eventos deportivos acreditados por secretaría académica.
•
Reunión de delegados (de darse el caso).
•
En caso de evaluaciones, para toma de rezagados:
•
Justificar con evidencias la inasistencia en las siguientes 24 horas de realizada la evaluación.

Código de Ética ULima
La Universidad de Lima fomenta la innovación, el desarrollo científico y el
pensamiento crítico de su comunidad. Asimismo, promueve la protección y el
respeto de las obras que son producto del esfuerzo académico en todas sus
manifestaciones. En tal sentido, se considera como plagio cualquier acción que
utilice el trabajo de otra persona o el resultado del empleo de inteligencia
artificial como propio, sin permiso o sin mencionar la fuente. Esta acción
constituye una transgresión a los derechos de autor y a las normas éticas que
sustentan el trabajo académico. Asimismo, se considera plagio en las
evaluaciones académicas utilizar o acceder a medios o información distintos a
los permitidos para el desarrollo de la evaluación.

Evaluación

¿Por qué un curso de Analítica con Big Data?
Experimentación => Producción
•
Diferentes enfoques: Data scientist
enfocado en investigación y
entrenamiento de modelos, Data
Engineer se encarga de la
industrialización de estos modelos.

¿Por qué un curso de Analítica con Big Data?
Especialización en Arquitecturas Modernas
•
La IA no son solamente chatbots.
•
Tenemos:
•
Sistemas RAG: El AI Engineer diseña
el flujo donde la IA consulta manuales,
SQLs o documentos privados para dar
respuestas sin "alucinaciones".
•
Agentes autónomos: Desarrollan
sistemas capaces de ejecutar tareas
(ej. "reserva este vuelo y actualiza el
presupuesto en SAP") de forma
independiente.

¿Por qué un curso de Analítica con Big Data?
Retorno de inversión en empresas
•
Las organizaciones actuales ya no invierten en IA por "moda", sino por
resultados:
•
Optimización de Costos
•
Mantenimiento y Monitoreo (LLMOps)

Big Data

¿Qué es Big Data?
•
No solo se refiere a “muchos datos”.
•
Paradigma que describe activos de información de
una gran magnitud, que requieren formas
específicas de procesamiento y métodos analíticos
que permitan la toma de decisiones,
descubrimientos de patrones y optimización de
procesos.

Objetivos
¿Qué quieres conseguir?
•
Analizar grandes cantidades de datos que requieren ser procesados.
•
Analizar menos datos, pero procesándolos en tiempo real.
•
Analizar datos que tengan un formato difícil y no estructurado ni predecible
(audios, videos).
•
Analizar datos cuyas fuentes no sean totalmente confiables

Proceso del Big Data
| Recolección | Almacenamiento | Análisis |
| ----------- | -------------- | -------- |
Toma de
decisiones
Datos

Diferencia con Data Analytics
•
Data Analytics: Es el proceso de extraer conclusiones de los datos.
•
Big Data: Infraestructura que soporta la gestión de los datos.

Actividad 1
Aplicación del Big Data en la industria
•
En grupos y utilizando IA, responder las siguientes preguntas y subirlas al foro
llamado Actividad 1.
•
¿Cómo se aplica Big Data en el sector en el que labora o laboró? En caso
ninguno del grupo trabaja o trabajó, puede elegir cualquier sector
productivo peruano (https://www.brysonhillsperu.com/2024/08/01/cuales-
son-los-5-sectores-productivos/)

Vs

Las 4 Vs
•
Nos permiten describir la naturales de los datos en procesos Big Data.
•
Son:
•
Volumen
•
Velocidad
•
Variedad
•
Veracidad

Volumen
•
Se refiere a la magnitud física de los datos (Laney, 2001). Ya no hablamos de Gigabytes, sino de
escalas que superan la capacidad de almacenamiento y procesamiento de sistemas
tradicionales (Petabytes, Exabytes).
•
Existe una cantidad masiva de datos generados cada segundo, por lo que el desafío es la forma
de almacenamiento y procesamiento en un solo servidor o en una base de datos relacional.
•
Ejm:
•
Una cadena de supermercados global. Cada transacción en cada caja, en cada país, genera
un registro. Al año, esto suma miles de millones de filas que una hoja de Excel o un SQL
tradicional no podrían abrir.
•
Los aviones modernos de Boeing generan aproximadamente 20 Terabytes de datos por
motor cada hora de vuelo. Multiplicado por miles de vuelos diarios, el volumen es masivo.

Velocidad
•
Es la rapidez con la que se generan, capturan y procesan los datos. No se trata solo de qué
tan rápido llegan, sino de qué tan rápido debemos reaccionar a ellos.
•
En muchos casos, los datos pierden su valor si no se analizan en "tiempo real" o "casi real”.
•
Ejm:
•
Los sistemas de detección de fraude con tarjetas de crédito. El banco tiene milisegundos
para analizar una transacción y decidir si la bloquea antes de que se complete el pago.
•
Los sensores de un auto autónomo. Si el sensor detecta un obstáculo, la analítica debe
procesar ese dato en milisegundos para frenar. Si el análisis tarda 10 segundos, el dato
ya no sirve.

Variedad
•
Se refiere a la heterogeneidad de las fuentes de datos (textos, audios, videos, logs de
servidores, datos de sensores GPS, etc).
•
El Big Data integra datos de diversas estructuras que deben convivir en un mismo
ecosistema.
•
Ejm:
•
Una empresa de retail analiza datos de ventas (Estructurados), comentarios en redes
sociales (No estructurados) y grabaciones de cámaras de seguridad en tiendas (No
estructurados).
•
El perfil de un cliente en una operadora telefónica. Tienen sus datos de contrato
(estructurado), las grabaciones de sus llamadas a soporte (audio/no estructurado) y sus
publicaciones en Twitter quejándose del servicio (texto/no estructurado).

Veracidad
•
Incertidumbre de los datos con los que se trabajan. Pueden tener sesgos,
ruido, errores o estar incompletos.
•
Ejm:
•
En el análisis de redes sociales, existen cuentas falsas (bots) o errores
gramaticales que pueden distorsionar el análisis de sentimiento si no se
filtran adecuadamente.
•
Un análisis de mercado basado en GPS. Si los datos de ubicación tienen un
margen de error de 500 metros, el análisis de "tráfico en tienda" será
erróneo. Los alumnos deben aprender que antes de analizar, hay que limpiar.

¿Y el Valor?
•
Se le considera la 5ta y más importante V. De nada sirve tener un sistema de
Big Data si no genera valor al negocio.
•
El valor es extrínseco al dato y depende del análisis.
•
Ejm: Beneficio vs Costo en Almacenamiento y Procesamiento.

Pregunta
•
¿En qué contextos aplicaría un sistema de Big Data en el contexto de la
Universidad de Lima?
•
Tomar en cuenta las 5 Vs explicadas anteriormente.

Fuentes de datos

Fuentes de datos
•
Podemos agruparlos por su naturaleza o por cómo se originan estos datos.

Máquinas
Por cómo se originan
•
Las máquinas con sensores generan gran cantidad de datos.
•
Obtienen y analizan datos de forma autónoma.
•
Ejemplos:
•
Smartphone: Información de geolocalización
•
Aviones: Aproximadamente 500 GB generados por vuelo.
•
Internet de las Cosas (IoT): Relojes (data biométrica).

Personas
Por cómo se originan
•
Datos obtenidos de redes sociales
•
Datos biométricos
•
La mayoría de los datos son no estructurados.

Organizaciones
Por cómo se originan
•
Cualquier evento o transacción puede ser almacenado.
•
Ejemplos:
•
Transacciones comerciales
•
Tarjetas de crédito
•
Historiales

Estructurados
•
Datos que tienen una estructura conocida y predefinida.
•
Ejemplos:
•
Bases de datos relacionales (tablas, columnas filas, relaciones)
•
Datos con estructura fija (protobuf, JSON, GraphQL, WSDL)

Semi-Estructurados
•
Datos que tienen una estructura flexible.
•
Ejemplos:
•
JSON, XML sin WSDL, bases de datos NO SQL.

No Estructurados
•
Datos que no tienen alguna estructura.
•
Ejemplos:
•
Texto, imágenes, audio, video.

Proceso del Big Data

Proceso del Big Data

Adquisición de datos
•
Los datos se encuentran almacenados en diversos lugares:
•
Bases de datos relaciones o NO SQL
•
Archivos de texto
Herramientas:
•
Datos remotos
Bases de Datos, Hadoop
•
Técnicas de recolección:
•
SQL, colas, consultas, etc.
•
PubSub

Preparación de los datos
•
Exploración inicial de los datos
•
Limpieza de los datos
•
Remover duplicados y datos con
valores faltantes.
•
Eliminar ruido, generar estimaciones
para valores no válidos.
•
Transformación de la data
•
Reducción de la dimensionalidad
•
Feature engineering

Procesamiento y análisis
•
Análisis descriptivo
•
Agrupamiento
•
Analítica de grafos
•
Análisis de asociación Herramienta:
•
Análisis predictivo
Spark
•
Regresión y Clasificación
•
Modelamiento
•
Seleccionar la técnica
•
Construir el modelo
•
Validar el modelo

Visualización
•
Presentación de resultados
•
Herramientas:
•
Python, R, Tableau, etc.

Utilización
•
En base a los resultados, tomar acciones o medidas.
•
Evaluación constante de los resultados para su mejora.