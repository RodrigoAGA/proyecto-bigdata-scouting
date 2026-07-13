FACULTAD DE INGENIERÍA
CARRERA DE INGENIERÍA DE SISTEMAS
Modelos de Clasificación
Sesión 10
Analítica con Big Data · 2026-1
1

Agenda
1. Modelos de Clasificación
2. Métricas para Clasificación
3. Regresión Logística
4. Árboles de Decisión
5. Clasificación con Spark MLlib
2

PARTE 1
Modelos de Clasificación
Conceptos fundamentales del aprendizaje supervisado
3

¿Qué es la clasificación?
Definición y tipos
La clasificación es una tarea de aprendizaje supervisado donde el objetivo es predecir una
etiqueta de clase discreta para cada observación a partir de variables de entrada (Hastie et
al., 2009).
4

Tipos por número de clases Proceso general
Binaria: dos clases (spam / no spam) 1. Conjunto de datos etiquetado
Multiclase: tres o más clases (especie de 2. Entrenamiento del modelo
flor)
3. Predicción sobre nuevos datos
Multi-etiqueta: múltiples etiquetas
4. Evaluación con métricas
simultáneas (categorías de artículo)
El modelo aprende una función f: X → Y que mapea características a clases (Hastie et al.,
2009).
5

Clasificadores probabilísticos vs.
Hard classifiers
Umbral de decisión
Clasificadores probabilísticos Hard classifiers
Producen una probabilidad P(y = 1 | x) Producen directamente una etiqueta
Permiten ajustar el umbral de decisión El umbral está fijo (por defecto 0.5)
Ejemplos: regresión logística, Naive Bayes Ejemplos: SVM con kernel, k-NN
Más flexibles ante desbalance de clases Más simples de interpretar
6

Elegir el umbral correcto depende del costo relativo de los errores de tipo I y tipo II en
cada problema (James et al., 2013).
7

Desbalance de clases
Oversampling, undersampling y SMOTE
En muchos problemas reales, las clases no están distribuidas uniformemente (James et al.,
2013).
Técnica Descripción Ventaja
Undersampling Reducir muestras de la clase mayoritaria Rápido, menos datos
Oversampling Duplicar muestras de la clase minoritaria Sin pérdida de información
SMOTE Generar muestras sintéticas interpolando vecinos Más diversidad sintética
Pesos de clase Penalizar más los errores en la clase rara Sin modificar datos
8

SMOTE (Synthetic Minority Over-sampling Technique) genera nuevas instancias
interpolando entre muestras existentes de la clase minoritaria, evitando la simple
duplicación.
9

Aplicaciones reales
¿Dónde se usa la clasificación?
La clasificación está presente en prácticamente todas las industrias (Goodfellow et al., 2016).
Ejemplos por dominio Criterios de elección del modelo
Finanzas: detección de fraude en Volumen y dimensionalidad de los datos
transacciones
Interpretabilidad requerida
Salud: diagnóstico médico (tumor
Velocidad de predicción
benigno/maligno)
Distribución de clases
Marketing: predicción de churn
Costo de errores (FP vs. FN)
(abandono)
10

PARTE 2
Métricas para Clasificación
Cómo medir el rendimiento de un modelo
11

Matriz de Confusión
La base de todas las métricas
La matriz de confusión resume los resultados de predicción de un clasificador binario
(Powers, 2011).
12

|                | Predicho: Positivo      | Predicho: Negativo      |
| -------------- | ----------------------- | ----------------------- |
| Real: Positivo | TP (Verdadero Positivo) | FN (Falso Negativo)     |
| Real: Negativo | FP (Falso Positivo)     | TN (Verdadero Negativo) |
TP: modelo dice positivo, es positivo FP: modelo dice positivo, es negativo
(Error tipo I)
TN: modelo dice negativo, es negativo
FN: modelo dice negativo, es positivo
(Error tipo II)
Todos los errores no tienen el mismo costo. En diagnóstico médico, un FN (enfermedad
no detectada) es mucho más grave que un FP (Powers, 2011).
13

Accuracy, Precision, Recall y
Specificity
Las métricas fundamentales
Derivadas directamente de la matriz de confusión (Powers, 2011):
| Métrica  | Fórmula           | Interpreta                  |
| -------- | ----------------- | --------------------------- |
| Accuracy | (TP + TN) / Total | % de predicciones correctas |
Precision TP / (TP + FP) De los que predije positivos, ¿cuántos lo eran?
Recall TP / (TP + FN) De los positivos reales, ¿cuántos detecté?
Specificity TN / (TN + FP) De los negativos reales, ¿cuántos identifiqué?
14

Accuracy puede ser engañosa con clases desbalanceadas. Un modelo que predice
siempre la clase mayoritaria puede tener 99% de accuracy pero ser inútil (Scikit-learn
developers, n.d.).
15

F1-Score
Media armónica entre Precision y Recall
El F1-Score equilibra la precisión y el recall en una sola métrica (Powers, 2011):
16

¿Cuándo usar F1? Variantes
Clases desbalanceadas F-beta: prioriza recall (β > 1) o precision (β
< 1)
Ambos errores (FP y FN) son importantes
Macro F1: promedio no ponderado por
Comparar modelos con trade-off diferente
clase
Weighted F1: promedio ponderado por
soporte
Si el costo de FN > FP, usar recall como métrica principal. Si FP > FN, usar precision. F1
balancea ambas.
17

Curva ROC y AUC
Evaluación independiente del umbral
La curva ROC (Receiver Operating Characteristic) grafica TPR vs. FPR para todos los
umbrales posibles (Fawcett, 2006).
18

Componentes Ventajas de ROC-AUC
TPR (Recall): TP / (TP + FN) No depende del umbral elegido
FPR: FP / (FP + TN) Útil para comparar modelos
AUC: Área bajo la curva ROC Robusto ante desbalance moderado
Interpretación del AUC Alternativa: PR Curve
→
AUC = 1.0 clasificador perfecto Mejor para desbalance severo
→
AUC = 0.5 clasificador aleatorio Grafica Precision vs. Recall
→
AUC < 0.5 peor que aleatorio
Fawcett (2006) propone ROC-AUC como métrica estándar para comparación de clasificadores binarios.
19

Métricas para Datasets
Desbalanceados
Evaluación con distribuciones asimétricas
Cuando las clases están muy desbalanceadas, las métricas estándar pueden ser engañosas
(Scikit-learn developers, n.d.).
20

| Situación | Métrica recomendada | Razón |
| --------- | ------------------- | ----- |
Desbalance moderado F1 Weighted Pondera por soporte de cada clase
| Desbalance severo | PR-AUC | Más informativa que ROC-AUC |
| ----------------- | ------ | --------------------------- |
Costo asimétrico Recall o Precision Según qué error es más costoso
| Comparación general | Cohen's Kappa | Corrige por azar |
| ------------------- | ------------- | ---------------- |
Cohen's Kappa (κ) mide el acuerdo entre predicciones y etiquetas reales corrigiendo por
la probabilidad de acuerdo al azar. κ > 0.8 indica excelente concordancia.
21

PARTE 3
Regresión Logística
Del espacio lineal a la probabilidad de clase
22

Función Sigmoide
El corazón de la regresión logística
La regresión logística transforma una combinación lineal de características en una
probabilidad usando la función sigmoide (Bishop, 2006):
23

Propiedades de σ(z) Decisión binaria
Salida siempre en (0, 1) P(y=1|x) = σ(z)
σ(0) = 0.5 P(y=0|x) = 1 − σ(z)
Monótonamente creciente Predice clase 1 si σ(z) ≥ 0.5
Diferenciable en todo su dominio Equivalente a z ≥ 0
A pesar del nombre, la regresión logística es un modelo de clasificación, no de
regresión (Bishop, 2006).
24

Frontera de Decisión
Separación lineal en el espacio de características
La frontera de decisión es el conjunto de puntos donde P(y=1|x) = 0.5, es decir, donde z = 0
(Ng, n.d.):
25

Características Extensiones no lineales
La frontera es lineal en el espacio original Agregar términos polinomiales: x², x₁·x₂
En 2D: una línea recta Transformaciones de características
En nD: un hiperplano de dimensión n−1 Kernels (SVM logístico)
No captura relaciones no lineales Redes neuronales
directamente
Para fronteras no lineales con regresión logística, se pueden agregar features
polinomiales antes de entrenar (Ng, n.d.).
26

Estimación de Máxima Verosimilitud
(MLE)
Cómo se ajustan los parámetros
Los parámetros w se estiman maximizando la verosimilitud de los datos observados (Murphy,
2012):
Equivalentemente, se minimiza la log-loss (entropía cruzada binaria):
27

| Optimización | Convergencia |     |
| ------------ | ------------ | --- |
→
| No tiene solución cerrada | Función convexa  |  mínimo global |
| ------------------------- | ---------------- | -------------- |
garantizado
Se usa Gradient Descent
Sensible a la escala de features
Variantes: SGD, L-BFGS, Newton-CG
Normalizar variables antes de entrenar
28

Regularización
Controlar el sobreajuste
La regularización añade una penalización sobre los coeficientes para evitar el overfitting
(Bishop, 2006):
29

L2 — Ridge L1 — Lasso
Encoge coeficientes hacia cero Puede fijar coeficientes en cero
No los hace exactamente cero Selección implícita de features
Estable ante multicolinealidad Útil en alta dimensionalidad
Optimizer: L-BFGS Optimizer: coordenada descendente
Elastic Net combina L1 y L2: penaliza con α·L1 + (1−α)·L2. Útil cuando hay muchas
features correlacionadas (Bishop, 2006).
30

PARTE 4
Árboles de Decisión
Particionando el espacio de características recursivamente
31

¿Qué es un Árbol de Decisión?
Estructura y funcionamiento
Un árbol de decisión particiona el espacio de características en regiones rectangulares y
asigna una clase a cada región (Breiman et al., 1984).
32

Componentes del árbol Ventajas
Nodo raíz: primera partición (feature más Interpretable y visualizable
informativa)
No requiere normalización de datos
Nodos internos: condiciones de división
Maneja features numéricas y categóricas
(x ≤ umbral)
Captura relaciones no lineales
Ramas: resultado de cada condición
Desventajas
(sí/no)
Tendencia al sobreajuste
Hojas: predicción final (clase mayoritaria)
Alta varianza (inestable)
Fronteras solo ortogonales
33

Algoritmo ID3 — Entropía e
Information Gain
Selección de la mejor división
El algoritmo ID3 elige en cada nodo la feature que maximiza el Information Gain (Quinlan,
1993):
í
34

Interpretación Limitaciones de ID3
Entropía = 0: nodo puro (una sola clase) Sesgo hacia features con muchos valores
Entropía = 1: máxima impureza (50/50) No soporta valores continuos directamente
IG mide cuánto reduce la entropía dividir Sin mecanismo de poda
por A
C4.5 corrige estas limitaciones (Quinlan,
1993)
35

CART — Impureza Gini
La alternativa a la entropía
CART (Classification and Regression Trees) usa la impureza Gini como criterio de división
(Breiman et al., 1984):
36

| Gini vs. Entropía |     |     | Características de CART |
| ----------------- | --- | --- | ----------------------- |
Solo particiones binarias
| Criterio | Cálculo | Velocidad |     |
| -------- | ------- | --------- | --- |
Gini Sin logaritmo Más rápido Soporta regresión y clasificación
|          |          | Ligeramente más | Base de Random Forests y Gradient |
| -------- | -------- | --------------- | --------------------------------- |
| Entropía | Con log₂ |                 |                                   |
lento
Boosting
Similar en
| Resultado |     | —   | Incluye cost-complexity pruning (Breiman |
| --------- | --- | --- | ---------------------------------------- |
práctica
et al., 1984)
37

Partición Recursiva
Construcción del árbol paso a paso
El árbol se construye con un algoritmo greedy top-down (Breiman et al., 1984):
38

función ConstruirÁrbol(S, features):
si S es puro o criterio de parada → retornar hoja con clase mayoritaria
para cada feature A y umbral t:
calcular IG(S, A, t)
(A*, t*) = argmax IG
S_izq = {x ∈ S : x[A*] ≤ t*}
S_der = {x ∈ S : x[A*] > t*}
retornar Nodo(A*, t*,
ConstruirÁrbol(S_izq),
ConstruirÁrbol(S_der))
La búsqueda es greedy: elige la mejor división local sin garantizar el árbol globalmente
óptimo. Esto puede llevar a sobreajuste si no se controla la profundidad (Breiman et al.,
1984).
39

Poda del Árbol
Evitando el sobreajuste
Un árbol sin restricciones memoriza los datos de entrenamiento. La poda reduce su
complejidad (Quinlan, 1993):
40

Pre-poda (criterios de parada) Post-poda
: profundidad máxima Cost-complexity pruning (α): elimina
max_depth
subárboles que no mejoran lo suficiente la
: mínimo de muestras
min_samples_split
precisión ponderada por tamaño
para dividir
Reduced error pruning: elimina nodos si
: mínimo en nodos
min_samples_leaf
el error en validación no aumenta
hoja
Selección de α con cross-validation
: features a considerar
max_features
En Spark MLlib, es el parámetro más importante. Valores típicos: 3–8. Un árbol
maxDepth
con profundidad > 10 casi siempre tiene sobreajuste.
41

PARTE 5
Clasificación con Spark
MLlib
Pipelines distribuidos para datos a escala
42

Pipeline API de Spark MLlib
Stages, Transformers y Estimators
La Pipeline API de Spark MLlib organiza el flujo de ML en etapas encadenadas y
reproducibles (Apache Software Foundation, n.d.):
43

| Transformer |     |     | Estimator |     |     |     |
| ----------- | --- | --- | --------- | --- | --- | --- |
Aplica una transformación a un DataFrame Aprende parámetros del dato de
entrenamiento
Método:
.transform(df)
→
|            |               |     | Método:  | .fit(df) |    retorna un Model |     |
| ---------- | ------------- | --- | -------- | -------- | ------------------- | --- |
| Ejemplos:  | StringIndexer | ,   |          |          |                     |     |
(Transformer)
,
VectorAssembler StandardScaler
|     |     |     | Ejemplos:  | LogisticRegression |     | ,   |
| --- | --- | --- | ---------- | ------------------ | --- | --- |
No aprende parámetros del dato
DecisionTreeClassifier
El Model resultante puede transformar
nuevos datos
44

from pyspark.ml import Pipeline
pipeline = Pipeline(stages=[indexer, assembler, scaler, classifier])
model = pipeline.fit(train_df)
predictions = model.transform(test_df)
Apache Software Foundation (n.d.)
45

Feature Engineering en Spark MLlib
Preparación de datos para el modelo
Spark MLlib provee transformers estándar para preparar las features (Apache Software
Foundation, n.d.):
46

from pyspark.ml.feature import StringIndexer, VectorAssembler, StandardScaler
# Codificar variables categóricas
indexer = StringIndexer(inputCol="categoria", outputCol="categoria_idx")
# Combinar features en un vector
assembler = VectorAssembler(
inputCols=["edad", "ingreso", "categoria_idx"],
outputCol="features_raw"
)
# Normalizar (media=0, desv=1)
scaler = StandardScaler(inputCol="features_raw", outputCol="features")
47

| Transformer | Propósito |     |
| ----------- | --------- | --- |
→
|     | Categoría  |  índice numérico |
| --- | ---------- | ---------------- |
StringIndexer
→
|     | Columnas  |  vector de features |
| --- | --------- | ------------------- |
VectorAssembler
Normalización Z-score
StandardScaler
→
| OneHotEncoder | Índice  |  vector binario |
| ------------- | ------- | --------------- |
48

LogisticRegression en Spark MLlib
Clasificación logística distribuida
Spark MLlib ofrece una implementación distribuida y escalable de regresión logística (Karau &
Warren, 2015):
49

from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(
featuresCol="features",
labelCol="label",
maxIter=100,
regParam=0.01, # λ de regularización
elasticNetParam=0.0, # 0=L2, 1=L1
family="binomial" # "multinomial" para multiclase
)
lr_model = lr.fit(train_df)
print(lr_model.coefficients)
print(lr_model.intercept)
50

DecisionTreeClassifier en Spark
MLlib
Árbol de decisión distribuido
Spark MLlib implementa CART con soporte nativo para datos distribuidos (Apache Software
Foundation, n.d.):
51

from pyspark.ml.classification import DecisionTreeClassifier
dt = DecisionTreeClassifier(
featuresCol="features",
labelCol="label",
maxDepth=5, # profundidad máxima
minInstancesPerNode=10, # pre-poda por tamaño
impurity="gini" # "entropy" también disponible
)
dt_model = dt.fit(train_df)
# Ver la estructura del árbol
print(dt_model.toDebugString)
# Importancia de features
print(dt_model.featureImportances)
52

devuelve un vector sparse con la importancia de cada feature
featureImportances
basada en la reducción total de impureza ponderada por el número de muestras
(Apache Software Foundation, n.d.).
53

Evaluadores en Spark MLlib
Medir el rendimiento del modelo
Spark MLlib provee evaluadores estándar para modelos de clasificación (Zaharia et al.,
2016):
54

from pyspark.ml.evaluation import (
BinaryClassificationEvaluator,
MulticlassClassificationEvaluator
)
# Para clasificación binaria
binary_eval = BinaryClassificationEvaluator(
labelCol="label",
rawPredictionCol="rawPrediction",
metricName="areaUnderROC" # o "areaUnderPR"
)
# Para clasificación multiclase
multi_eval = MulticlassClassificationEvaluator(
labelCol="label",
predictionCol="prediction",
metricName="f1" # "accuracy", "weightedPrecision", "weightedRecall"
)
auc = binary_eval.evaluate(predictions)
f1 = multi_eval.evaluate(predictions)
55

CrossValidator y ParamGridBuilder
Ajuste de hiperparámetros distribuido
Spark MLlib permite realizar k-fold cross-validation de forma distribuida sobre todo el
pipeline (Karau & Warren, 2015):
56

from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
# Grilla de hiperparámetros
param_grid = (ParamGridBuilder()
.addGrid(lr.regParam, [0.01, 0.1, 1.0])
.addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0])
.addGrid(dt.maxDepth, [3, 5, 8])
.build())
cv = CrossValidator(
estimator=pipeline,
estimatorParamMaps=param_grid,
evaluator=binary_eval,
numFolds=5,
parallelism=4 # evaluaciones paralelas
)
cv_model = cv.fit(train_df)
best_model = cv_model.bestModel
57

Flujo Completo: Pipeline de
Clasificación en Spark
Integrando todos los componentes
58

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, StandardScaler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
# 1. Preparación
indexer = StringIndexer(inputCol="cat", outputCol="cat_idx")
assembler = VectorAssembler(inputCols=["f1","f2","cat_idx"], outputCol="feats_raw")
scaler = StandardScaler(inputCol="feats_raw", outputCol="features")
# 2. Modelo
lr = LogisticRegression(featuresCol="features", labelCol="label")
# 3. Pipeline + CV
pipeline = Pipeline(stages=[indexer, assembler, scaler, lr])
param_grid = ParamGridBuilder().addGrid(lr.regParam, [0.01, 0.1]).build()
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=param_grid,
evaluator=BinaryClassificationEvaluator(), numFolds=5)
# 4. Entrenamiento y evaluación
cv_model = cv.fit(train_df)
predictions = cv_model.transform(test_df)
59

Referencias
60

Referencias
Apache Software Foundation. (n.d.). MLlib: Machine learning library.
https://spark.apache.org/docs/latest/ml-guide.html
Bishop, C. M. (2006). Pattern recognition and machine learning. Springer.
Breiman, L., Friedman, J., Stone, C. J., & Olshen, R. A. (1984). Classification and regression
trees. Chapman & Hall.
Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8), 861–
874. https://doi.org/10.1016/j.patrec.2005.10.010
Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT Press.
61

Hastie, T., Tibshirani, R., & Friedman, J. (2009). The elements of statistical learning: Data
mining, inference, and prediction (2nd ed.). Springer. https://doi.org/10.1007/978-0-387-
84858-7
James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An introduction to statistical learning:
With applications in R. Springer. https://doi.org/10.1007/978-1-4614-7138-7
Karau, H., & Warren, R. (2015). Learning Spark: Lightning-fast big data analysis. O'Reilly
Media.
Murphy, K. P. (2012). Machine learning: A probabilistic perspective. MIT Press.
Ng, A. (n.d.). CS229 lecture notes: Supervised learning. Stanford University.
https://cs229.stanford.edu/notes/cs229-notes1.pdf
62

Powers, D. M. W. (2011). Evaluation: From precision, recall and F-measure to ROC,
informedness, markedness and correlation. Journal of Machine Learning Technologies, 2(1),
37–63.
Quinlan, J. R. (1993). C4.5: Programs for machine learning. Morgan Kaufmann.
Salzberg, S. L. (1994). C4.5: Programs for machine learning [Review]. Machine Learning, 16,
235–240. https://doi.org/10.1007/BF00993309
Zaharia, M., Xin, R. S., Wendell, P., Das, T., Armbrust, M., Dave, A., Meng, X., Rosen, J.,
Venkataraman, S., Franklin, M. J., Ghodsi, A., Gonzalez, J., Shenker, S., & Stoica, I. (2016).
Apache Spark: A unified engine for big data processing. Communications of the ACM, 59(11),
56–65. https://doi.org/10.1145/2934664
63