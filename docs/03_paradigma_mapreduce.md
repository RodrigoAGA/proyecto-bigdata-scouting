FACULTAD DE INGENIERÍA
CARRERA DE INGENIERÍA DE  SISTEMAS

Paradigma MapReduce

Semana 3

Analítica con Big Data

Orígenes

Contexto histórico
El paper de Google (2004)

• En 2004, Jeﬀ Dean y Sanjay Ghemawat publicaron "MapReduce: Simpliﬁed

Data Processing on Large Clusters"

• Google necesitaba procesar terabytes de datos del índice web con miles de

máquinas

• El modelo abstraía la complejidad del cómputo distribuido, permitiendo a
ingenieros sin experiencia en sistemas distribuidos escribir programas
paralelos.

El problema a escala web

• Procesar petabytes de datos con hardware commodity (barato, no

conﬁable)

• Las supercomputadoras son costosas y no escalan linealmente

• La solución: distribuir el trabajo en miles de nodos estándar

• Paradigma "scale out" (más nodos) vs. "scale up" (hardware más potente)

Programación distribuida
Calcular el promedio histórico de la ULima

10

15

13

16

06

12

15

19
…
14

¿Cómo lo haríamos de forma distribuida?

Programación distribuida
Calcular el promedio histórico de la ULima

10

15

13

16

06

12

15

19
…
14

Principios de diseño

Modelo MapReduce

Paradigma Funcional
Pares key-value

• Map: función stateless que transforma cada registro en pares `(clave, valor)`

• Reduce: agrega todos los valores con la misma clave

• Inspirado en lenguajes funcionales (Lisp)

• El framework gestiona automáticamente la distribución y comunicación entre

nodos

Fases de Ejecución

Input Splits

Map

Shufﬂe & Sort

Reduce

Output

• Input Splits: HDFS divide los datos en bloques (128 MB por defecto)

• Map: cada mapper procesa un split de forma independiente

• Shuﬄe & Sort: reagrupa pares por clave entre nodos de la red

• Reduce: agrega los valores agrupados por clave

• Output: escritura del resultado ﬁnal en HDFS

Ejemplo

• Se quiere calcular el promedio de edad por provincia del Perú.

Input Splits

Map

Shuﬄe & Sort

Reduce

Output

Ejecución distribuida más sencilla

Referencias

Analytics Vidhya. (2022). *Apache Spark vs. Hadoop MapReduce: Top 7 diﬀerences*. https://www.analyticsvidhya.com/
blog/2022/06/apache-spark-vs-hadoop-mapreduce-top-7-diﬀerences/

Anomaly AI. (2026). *Big data analytics tools: Hadoop, Spark, BigQuery, Snowﬂake*. https://www.ﬁndanomaly.ai/big-
data-analytics-tools-hadoop-spark-bigquery-snowﬂake

Apache Hadoop. (n.d.). *MapReduce tutorial*. https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/
hadoop-mapreduce-client-core/MapReduceTutorial.html

Cornell Center for Advanced Computing. (2012). *MapReduce* [Training material]. https://www.cac.cornell.edu/
education/training/ParallelMay2012/MapReduce.pdf

Dean, J., & Ghemawat, S. (2004). MapReduce: Simpliﬁed data processing on large clusters. In *OSDI '04: Sixth
Symposium on Operating System Design and Implementation*. USENIX.

Dremio. (n.d.). *MapReduce programming model*. https://www.dremio.com/wiki/mapreduce-programming-model/

Edureka. (n.d.). *MapReduce tutorial: Understanding MapReduce in Hadoop*. https://www.edureka.co/blog/
mapreduce-tutorial/

