FACULTAD DE INGENIERÍA
CARRERA DE INGENIERÍA DE  SISTEMAS

Hadoop

Semana 4

Analítica con Big Data

Introducción a Hadoop

Hitos históricos

• - 2003 : Google publica el paper del Google File System (GFS)

• - 2004 : Google publica el paper de MapReduce

• - 2006 : Yahoo! separa el componente de Nutch: nace Hadoop

• - 2008 : Apache Software Foundation adopta Hadoop como proyecto top-

level

Filosofía central

"Move the computation to the data, not the data to the computation"

• En lugar de mover petabytes por la red, Hadoop envía el código de

procesamiento a los nodos donde ya residen los datos.

Problemática
¿Por qué las RDBMS tradicionales no escalan?

• Escalado vertical (hardware más potente) → costo prohibitivo y límites físicos

• Hadoop propone escalado horizontal: añadir nodos commodity de bajo

costo

Arquitectura Hadoop

• Hadoop Common: Utilidades y librerías

compartidas por todos los demás
módulos del framework.

• HDFS: Hadoop Distributed File System

— capa de almacenamiento distribuido y
tolerante a fallos.

• YARN: *Yet Another Resource

Negotiator* — gestión de recursos del
clúster y planiﬁcación de trabajos.

• MapReduce: Modelo de programación
para procesamiento paralelo de datos a
gran escala.

MapReduce

YARN (*)

HDFS

Hadoop
Common

Hadoop fue diseñado para correr sobre hardware
commodity asumiendo que los fallos de nodos son la
norma, no la excepción. La tolerancia a fallos es
gestionada a nivel de software.

HDFS

Arquitectura de HDFS

• HDFS sigue una arquitectura **maestro-esclavo** con tres componentes

principales:

NameNode (maestro)

DataNode (esclavos)

- Almacena el namespace del sistema
de archivos (metadatos: nombres,
permisos, estructura de directorios)

- Almacenan los bloques de datos en

disco

Secondary NameNode

- No es un failover del NameNode

(nombre engañoso)

- Registra el mapeo: qué bloques

componen cada archivo y en qué
DataNodes residen.

-  No almacena datos reales, es el
"índice" del sistema de archivos

- Envían heartbeats periódicos al

- Realiza checkpoints periódicos del

NameNode para señalar que están
activos

namespace para reducir el tiempo de
arranque del NameNode

- Sirven las operaciones de lectura y

escritura solicitadas por los clientes.

Bloques en HDFS

• Tamaño por defecto: 128 MB (conﬁgurable; bloques grandes reducen el

overhead de metadatos)

• Un archivo grande se divide en múltiples bloques distribuidos entre los

DataNodes del clúster

• Permite procesar bloques en paralelo en los nodos donde residen

Factor de Replicación

• Por defecto: 3 réplicas por cada bloque

• Conﬁgurable en `hdfs-site.xml` mediante la propiedad `dfs.replication`

• Las réplicas se distribuyen estratégicamente en distintos nodos y racks

Tolerancia a fallos

• Si un DataNode deja de enviar heartbeats, el NameNode lo marca como

caído

• El framework re-replica automáticamente los bloques afectados para

restaurar el factor de replicación

Comandos Básicos de HDFS

# Listar archivos y directorios

hdfs dfs -ls /user/hadoop/

# Crear un directorio en HDFS

hdfs dfs -mkdir /user/hadoop/datos

# Subir archivo desde el sistema local a HDFS

hdfs dfs -put archivo_local.txt /user/hadoop/datos/

# Descargar archivo de HDFS al sistema local

hdfs dfs -get /user/hadoop/datos/archivo.txt ./local/

# Ver el contenido de un archivo directamente

hdfs dfs -cat /user/hadoop/datos/archivo.txt

Comandos Básicos de HDFS
Continuación

# Eliminar un archivo (usar -rm -r para directorios)

hdfs dfs -rm /user/hadoop/datos/archivo.txt

# Copiar archivo dentro de HDFS

hdfs dfs -cp /origen/archivo.txt /destino/

# Mover archivo dentro de HDFS

hdfs dfs -mv /origen/archivo.txt /destino/

Interfaz Web del NameNode

• El NameNode expone una **UI Web** para monitoreo y exploración del sistema de

archivos.

• Funcionalidades principales:

• Explorar el árbol de directorios y archivos de HDFS

• Monitorear DataNodes: activos, inactivos y en decommission

• Ver estadísticas de capacidad: espacio total, usado y libre

• Consultar el estado de bloques bajo-replicados

• Acceder a logs del NameNode

Goggle Cloud Storage como alternativa

En entornos cloud, Google Cloud Storage (GCS) es la alternativa
recomendada a HDFS:

• HDFS (On-Premise)

• GCS (Cloud-Native)

• Almacenamiento acoplado al clúster

• Almacenamiento desacoplado del clúster

• Requiere gestionar DataNodes activos

• Fully managed por Google

• Esquema: `hdfs://`

• Esquema: `gs://`

• Los datos desaparecen si el clúster se

elimina

• Los datos **persisten** aunque el clúster

sea eliminado

• Escalado manual de capacidad

• Escalado automático e ilimitado

Referencias

Apache Software Foundation. (n.d.a). *HDFS architecture guide*. https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html

Apache Software Foundation. (n.d.b). *HDFS commands guide* (Version 3.3.5). https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/
HDFSCommands.html

Apache Software Foundation. (n.d.c). *MapReduce tutorial*. https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/
MapReduceTutorial.html

Apache Software Foundation. (n.d.d). *Hadoop streaming*. https://hadoop.apache.org/docs/current/hadoop-streaming/HadoopStreaming.html

CodeWithFaraz. (n.d.). *Top 15 Hadoop ecosystem components in 2024: A comprehensive guide*. https://www.codewithfaraz.com/article/78/top-15-hadoop-ecosystem-
components-in-2024-a-comprehensive-guide

DataFlair. (n.d.). *Hadoop ecosystem components*. https://data-ﬂair.training/blogs/hadoop-ecosystem-components/

Databricks. (n.d.). *Hadoop ecosystem*. https://www.databricks.com/glossary/hadoop-ecosystem

Edureka. (n.d.). *Hadoop ecosystem*. https://www.edureka.co/blog/hadoop-ecosystem

freeCodeCamp. (n.d.). *What is Google Dataproc?* https://www.freecodecamp.org/news/what-is-google-dataproc/

GeeksforGeeks. (n.d.). *Hadoop ecosystem*. https://www.geeksforgeeks.org/dbms/hadoop-ecosystem/

Google Cloud. (n.d.a). *Dataproc Hadoop data storage*. https://docs.cloud.google.com/dataproc/docs/concepts/dataproc-hdfs

Google Cloud. (n.d.b). *Use Cloud Client Libraries for Python*. https://docs.cloud.google.com/dataproc/docs/tutorials/python-library-example

LabEx. (n.d.a). *How to use HDFS commands to interact with Hadoop Distributed File System*. https://labex.io/tutorials/hadoop-how-to-use-hdfs-commands-to-interact-with-
hadoop-distributed-ﬁle-system-417618

LabEx. (n.d.b). *How to conﬁgure HDFS in a Hadoop cluster*. https://labex.io/tutorials/hadoop-how-to-conﬁgure-hdfs-in-a-hadoop-cluster-415124

Wikipedia. (n.d.). *Apache Hadoop*. https://en.wikipedia.org/wiki/Apache_Hadoop

