FACULTAD DE INGENIERÍA
CARRERA DE INGENIERÍA DE SISTEMAS
Modelos de Regresión
Semana 9
Analítica con Big Data · 2026-1
1

Agenda
1. Modelos de Regresión — tipos, supuestos y variantes
2. Métricas para Regresión — MAE, MSE, RMSE, R² y análisis de residuos
3. Regresión con Spark MLlib — VectorAssembler, Pipeline y evaluación distribuida
2

PARTE 1
Modelos de Regresión
Tipos, supuestos y variantes principales
3

¿Qué es la Regresión?
La regresión es una tarea de aprendizaje supervisado cuya salida es un valor continuo.
Objetivo Ejemplos de uso
Aprender una función f tal que: Predicción de precios de vivienda
ŷ = f(X)
Minimizar la diferencia entre e Estimación de temperatura
ŷ y
Proyección de ventas
Diferencia con Clasificación
Tiempo de procesamiento de consultas
→
Clasificación etiqueta discreta ( ,
spam
SQL
)
no spam
→
Regresión valor numérico ( ,
$150,000
)
23.5°C
4

Regresión Lineal Simple
Modela la relación entre una variable independiente y una variable dependiente :
x y
ŷ = β₀ + β₁x
Función de costo (MSE):
J(β₀, β₁) = (1/n) Σ (yᵢ − ŷᵢ)²
Mínimos Cuadrados Ordinarios (OLS): minimiza con solución analítica cerrada:
J
β₁ = Σ(xᵢ − x̄)(yᵢ − ȳ) / Σ(xᵢ − x̄)² β₀ = ȳ − β₁x̄
5

OLS garantiza el mejor estimador lineal no sesgado (teorema de Gauss-Markov)
cuando se cumplen los supuestos del modelo.
(Built In, 2024a; Vignesh, 2023)
6

Regresión Lineal Múltiple
Extiende la regresión simple a p features:
ₚ ₚ
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + β x
→
Forma matricial: ŷ = Xβ β̂ = (XᵀX)⁻¹Xᵀy
7

Cinco supuestos (Gauss-Markov):
# Supuesto Consecuencia de violación
1 Linealidad Sesgo en estimadores
2 Independencia de errores Autocorrelación
3 Homocedasticidad Errores estándar inválidos
4 Normalidad de errores Intervalos de confianza incorrectos
5 Ausencia de multicolinealidad Coeficientes inestables
(Statology, 2024; Towards Data Science, 2023)
8

Regresión Polinomial
Cuando la relación entre e no es lineal, se elevan las features a potencias:
x y
ŷ = β₀ + β₁x + β₂x² + β₃x³ + ...
Ventaja Riesgo
→
Captura relaciones no lineales Grado alto overfitting
→ →
Sigue siendo lineal en los parámetros Grado bajo underfitting
OLS aplica
Selección de grado: validación cruzada
Simple de implementar con
PolynomialFeatures
9

Un polinomio de grado n pasa exactamente por n+1 puntos, pero generaliza muy mal a
datos nuevos. Usar regularización o CV para controlar la complejidad.
(Mithani, 2023)
10

Regularización: Motivación
Los modelos lineales complejos o con muchas features tienden al overfitting.
Solución: agregar un término de penalización al costo:
J_reg(β) = J_OLS(β) + λ · Ω(β)
| Término               | Nombre      | Efecto                          |
| --------------------- | ----------- | ------------------------------- |
| λ ‖β‖²₂               | L2 / Ridge  | Reduce magnitud de coeficientes |
| λ ‖β‖₁                | L1 / Lasso  | Fuerza coeficientes a cero      |
| λ[α‖β‖₁ + (1−α)‖β‖²₂] | Elastic Net | Combinación de ambos            |
11

λ controla la fuerza de regularización:
→
λ 0: sin regularización (OLS)
→ →
λ ∞: coeficientes 0
(Brenndoerfer, 2024)
12

Ridge Regression (Regularización L2)
Función de costo:
J_Ridge = Σ(yᵢ − ŷᵢ)² + λ Σβⱼ²
Solución analítica: β̂ = (XᵀX + λI)⁻¹Xᵀy
Shrinkage: todos los coeficientes se reducen, pero ninguno llega a cero
Ideal con multicolinealidad o muchas features correlacionadas
Mayor λ Menor λ
Mayor sesgo Menor sesgo
Menor varianza Mayor varianza
Coeficientes más pequeños Se acerca a OLS
13

Lasso Regression (Regularización L1)
Función de costo:
J_Lasso = Σ(yᵢ − ŷᵢ)² + λ Σ|βⱼ|
→
Sparsity: fuerza algunos coeficientes exactamente a cero selección automática de
features
No tiene solución analítica cerrada (usa descenso de coordenadas)
Ideal para datasets de alta dimensionalidad con pocas features relevantes
¿Por qué L1 produce ceros y L2 no?
La región de restricción L1 (diamante) tiene esquinas sobre los ejes. El óptimo suele tocar
→
una esquina coeficiente = 0. L2 (esfera) no tiene esquinas.
14
( )

Elastic Net
Combina L1 y L2:
J_EN = Σ(yᵢ − ŷᵢ)² + λ [ α ‖β‖₁ + (1−α) ‖β‖²₂ ]
α = 1: Lasso puro
α = 0: Ridge puro
0 < α < 1: Elastic Net
Cuándo usar Elastic Net Hiperparámetros
Features en grupos correlacionados : fuerza total de regularización
λ
Se desea selección de features (Lasso) : ratio L1 / L2
α
con más estabilidad (Ridge)
Seleccionar vía cross-validation
15
Datasets con p >> n

Comparativa: OLS, Ridge, Lasso y Elastic Net
Selección de
| Método | Penalización |     | Multicolinealidad | Cuándo usar |
| ------ | ------------ | --- | ----------------- | ----------- |
features
| OLS   | Ninguna | No  | Problema    | Datos limpios, pocas features |
| ----- | ------- | --- | ----------- | ----------------------------- |
| Ridge | L2 ‖β‖² | No  | Maneja bien | Features correlacionadas      |
Alta dimensionalidad, pocas
| Lasso | L1 ‖β‖₁ | Sí  | Elige 1 del grupo |     |
| ----- | ------- | --- | ----------------- | --- |
relevantes
| Elastic |         |     |             | Grupos correlacionados + |
| ------- | ------- | --- | ----------- | ------------------------ |
|         | L1 + L2 | Sí  | Maneja bien |                          |
| Net     |         |     |             | selección                |
(Brenndoerfer, 2024; Bhuva, 2024; scikit-learn, 2024a, 2024b)
16

Decision Tree y Random Forest para Regresión
Decision Tree Regressor Random Forest Regressor
Divide el espacio de features Ensemble de árboles sobre subsets
recursivamente aleatorios (bagging)
Predicción: media de los valores en la hoja Predicción: promedio de todos los árboles
Pros: interpretable, sin supuestos de Reduce varianza sin aumentar sesgo
linealidad significativamente
Contras: alta varianza, overfitting fácil Robusto a outliers, no requiere escalado
de features
17

Random Forest es uno de los algoritmos más robustos out-of-the-box para regresión.
| Clave tunear  | n_estimators |  y  max_depth | .   |
| ------------- | ------------ | ------------- | --- |
(Oracle, 2024; Brenndoerfer, 2024b)
18

Gradient Boosting para Regresión
Construcción secuencial de árboles: cada árbol corrige los errores del anterior.
Algoritmo:
1. Inicializar
F₀(x) = ȳ
2. Para t = 1, …, T:
ₜ
| Calcular residuos:  |                   | rᵢ = yᵢ − F | ₋₁(xᵢ) |
| ------------------- | ----------------- | ----------- | ------ |
| Ajustar árbol       | ₜ  a los residuos |             |        |
h
| Actualizar:  | ₜ   | ₜ ₋₁(x) + η · h | ₜ   |
| ------------ | --- | --------------- | --- |
F (x) = F (x)
19

Hiperparámetros clave:
Parámetro Efecto
n_estimators Número de árboles (más = mejor, pero más lento)
learning_rate (η) Tamaño del paso — compensar con más árboles
max_depth Complejidad de cada árbol
(DataCamp, 2024a)
20

Support Vector Regression (SVR)
Busca un hiperplano dentro de un tubo de tolerancia ε que contenga la mayor cantidad de
puntos.
| Objetivo: minimizar  | ‖w‖²  sujeto a  | |yᵢ − ŷᵢ| ≤ ε |     |     |     |
| -------------------- | --------------- | ------------- | --- | --- | --- |
Parámetros clave:
C: penaliza puntos fuera del tubo (fuerza de regularización)
ε: ancho del tubo de tolerancia
| Kernel: transforma features ( |     |        | ,   | ,    | )   |
| ----------------------------- | --- | ------ | --- | ---- | --- |
|                               |     | linear | rbf | poly |     |
21

Ventajas Desventajas
Eficaz en alta dimensionalidad Escala mal con datasets grandes
Robusto a outliers dentro del tubo Requiere escalado de features
Flexible vía kernels no lineales Difícil de interpretar
(Analytics Vidhya, 2020)
22

Resumen: ¿Cuándo usar cada modelo?
Modelo Interpretabilidad Escalabilidad No linealidad Selección features
| OLS / MLR           | Alta     | Media | No          | No        |
| ------------------- | -------- | ----- | ----------- | --------- |
| Ridge               | Media    | Alta  | No          | No        |
| Lasso / Elastic Net | Media    | Alta  | No          | Sí        |
| Decision Tree       | Alta     | Media | Sí          | Implícita |
| Random Forest       | Baja     | Alta  | Sí          | Implícita |
| Gradient Boosting   | Baja     | Alta  | Sí          | Implícita |
| SVR                 | Muy baja | Baja  | Sí (kernel) | No        |
23

PARTE 2
Métricas para Regresión
Cómo medir y comparar el desempeño de modelos
24

MAE — Mean Absolute Error
MAE = (1/n) Σ |yᵢ − ŷᵢ|
Propiedades:
Mismas unidades que la variable objetivo
Robusto a outliers: penaliza proporcionalmente, sin elevar al cuadrado
Interpretación directa: "En promedio el modelo se equivoca en ±X unidades"
25

Ventajas Desventajas
Fácil de interpretar No diferenciable en 0 (no ideal para
gradient descent)
Menos sensible a errores grandes
No distingue entre muchos errores
Métrica mediana en distribuciones
pequeños y pocos errores grandes
simétricas
(Mundal, 2024)
26

MSE y RMSE
MSE — Mean Squared Error
MSE = (1/n) Σ (yᵢ − ŷᵢ)²
Penaliza fuertemente errores grandes (efecto cuadrático)
→
Completamente diferenciable ideal como función de pérdida en optimización
Unidades: cuadrado de la variable objetivo (menos interpretable)
RMSE — Root Mean Squared Error
RMSE = √MSE
Mismas unidades que la variable objetivo
La métrica más usada en práctica para regresión
27
Sensible a outliers (hereda de MSE)

siempre. Cuanto mayor la diferencia entre ambas, mayor es la influencia de
RMSE ≥ MAE
valores atípicos en el dataset.
(GeeksforGeeks, 2024b; Matalonga, 2024)
28

R² — Coeficiente de Determinación
R² = 1 − (SS_res / SS_tot) = 1 − [ Σ(yᵢ − ŷᵢ)² / Σ(yᵢ − ȳ)² ]
Interpretación: proporción de la varianza total explicada por el modelo.
Valor Significado
R² = 1 Ajuste perfecto — el modelo explica toda la varianza
R² = 0 El modelo equivale a predecir siempre ȳ
R² < 0 El modelo es peor que predecir la media
Trampa común: R² siempre aumenta al agregar features, aunque sean irrelevantes. Para
comparar modelos con distinto número de predictores, usar R² Ajustado.
(Built In, 2024b; DataCamp, 2024b)
29

R² Ajustado
R²_adj = 1 − [ (1 − R²)(n − 1) / (n − p − 1) ]
| Donde                       | n  = observaciones y  | p  = número de features. |                  |
| --------------------------- | --------------------- | ------------------------ | ---------------- |
|                             |                       | R²                       | R² Ajustado      |
| Agregar feature irrelevante |                       | Siempre aumenta          | Puede disminuir  |
| Penaliza complejidad        |                       | No                       | Sí               |
| Uso recomendado             |                       | Una sola configuración   | Comparar modelos |
| Rango                       |                       | (−∞, 1]                  | (−∞, 1]          |
30

R² Ajustado es el estándar para comparar modelos con distinto número de predictores.
Una caída al agregar una feature indica que no aporta valor real.
(AnalystPrep, 2024)
31

MAPE y RMSLE
MAPE — Mean Absolute Percentage Error
MAPE = (100/n) Σ | (yᵢ − ŷᵢ) / yᵢ |
→
Error relativo expresado en porcentaje comunicable a stakeholders
Problema: indefinido cuando ; sesgado con valores pequeños
yᵢ = 0
RMSLE — Root Mean Squared Log Error
RMSLE = √[ (1/n) Σ (log(ŷᵢ + 1) − log(yᵢ + 1))² ]
Útil cuando el target tiene distribución sesgada (precios, salarios, tráfico web)
Penaliza más la subestimación que la sobreestimación
Popular en competencias Kaggle con targets con cola larga
32
(Arize AI, 2024; Towards Data Science, 2024)

Análisis de Residuos
Los residuos   deben examinarse para validar los supuestos del modelo.
eᵢ = yᵢ − ŷᵢ
Gráficos diagnósticos clave:
| Gráfico | Qué detecta | Patrón problemático |
| ------- | ----------- | ------------------- |
Residuos vs Fitted Linealidad, homocedasticidad Curva o embudo
| Q-Q Plot | Normalidad de errores | Desviación de la diagonal |
| -------- | --------------------- | ------------------------- |
Scale-Location Homocedasticidad Pendiente en la línea de tendencia
Residuos vs Leverage Puntos influyentes Puntos fuera de la distancia de Cook
33

Un buen modelo muestra residuos distribuidos aleatoriamente alrededor de cero, sin
patrones sistemáticos ni heterocedasticidad.
(Six Sigma DSI, 2024; Qualtrics, 2024)
34

Tabla Comparativa de Métricas
| Métrica | Unidades | Outliers | Interpretación | Cuándo usar |
| ------- | -------- | -------- | -------------- | ----------- |
MAE = y Robusto Error promedio absoluto Interpretabilidad directa
MSE y² Sensible Error cuadrático medio Loss function / optimización
RMSE = y Sensible Error cuadrático medio (raíz) Métrica estándar principal
R² Sin unidad Medio % varianza explicada Bondad de ajuste global
R²_adj Sin unidad Medio % varianza (penaliza p) Comparar modelos distintos
| MAPE  | %          | Muy sensible | Error relativo %   | Comunicación ejecutiva |
| ----- | ---------- | ------------ | ------------------ | ---------------------- |
| RMSLE | Sin unidad | Medio        | Error log-escalado | Targets sesgados       |
35

PARTE 3
Regresión con Spark MLlib
Pipeline distribuido end-to-end
36

Algoritmos de Regresión en Spark MLlib
Spark MLlib ofrece una suite completa de algoritmos de regresión escalables:
| Algoritmo | Clase PySpark | Tipo |
| --------- | ------------- | ---- |
Lineal + regularización
Regresión Lineal
LinearRegression
L1/L2/Elastic Net
| Regresión Lineal |     | Familias: Gaussian, Poisson, |
| ---------------- | --- | ---------------------------- |
GeneralizedLinearRegression
| Generalizada      |                       | Gamma              |
| ----------------- | --------------------- | ------------------ |
| Árbol de Decisión | DecisionTreeRegressor | No lineal          |
| Random Forest     |                       | Ensemble (bagging) |
RandomForestRegressor
| Gradient Boosted Trees |     | Ensemble (boosting) |
| ---------------------- | --- | ------------------- |
GBTRegressor
| Regresión Isotónica |     | No paramétrica, monotónica |
| ------------------- | --- | -------------------------- |
IsotonicRegression
(Apache Software Foundation, 2024e; Sharma, 2024) 37

VectorAssembler: Ensamblado de Features
Paso obligatorio en MLlib: todas las features deben estar en un único vector columna.
from pyspark.ml.feature import VectorAssembler
assembler = VectorAssembler(
inputCols=["rooms", "age", "distance", "income"],
outputCol="features"
)
df_assembled = assembler.transform(df)
Resultado:
rooms age distance income features
4 10 2.5 55000 [4.0, 10.0, 2.5, 55000.0]
38
(Apache Software Foundation, 2024a)

Pipeline API: Transformers + Estimators
Un Pipeline encadena transformaciones y modelo en un objeto reproducible:
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression
assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features")
scaler = StandardScaler(inputCol="raw_features", outputCol="features")
lr = LinearRegression(featuresCol="features", labelCol="price")
pipeline = Pipeline(stages=[assembler, scaler, lr])
model = pipeline.fit(train_df)
predictions = model.transform(test_df)
39

El Pipeline garantiza que el mismo preprocesamiento se aplique en train y test —
evitando data leakage. Es la forma recomendada para producción.
(33rd Square, 2024; Apache Software Foundation, 2024b)
40

LinearRegression: Regularización en Spark
from pyspark.ml.regression import LinearRegression
lr = LinearRegression(
featuresCol="features",
labelCol="price",
maxIter=100,
regParam=0.1, # λ: fuerza de regularización
elasticNetParam=0.0 # α: 0.0 = Ridge, 1.0 = Lasso
)
model = lr.fit(train_df)
# Resumen del modelo entrenado
summary = model.summary
print(f"RMSE: {summary.rootMeanSquaredError:.4f}")
print(f"R²: {summary.r2:.4f}")
print(f"Coeficientes: {model.coefficients}")
print(f"Intercepto: {model.intercept:.4f}")
41

= λ controla la penalización. = α mezcla L1 y L2: 0 = Ridge
regParam elasticNetParam
puro, 1 = Lasso puro.
(Apache Software Foundation, 2024e)
42

GBTRegressor: Gradient Boosted Trees
from pyspark.ml.regression import GBTRegressor
gbt = GBTRegressor(
featuresCol="features",
labelCol="price",
maxIter=50, # número de árboles
maxDepth=5, # profundidad de cada árbol
stepSize=0.1 # learning rate (η)
)
model = gbt.fit(train_df)
predictions = model.transform(test_df)
43

Cuándo usar GBT sobre LinearRegression:
Relaciones no lineales entre features y target
Interacciones entre variables
Features de tipos mixtos (numéricas + categóricas codificadas)
Mayor capacidad predictiva a costo de menor interpretabilidad
(Apache Software Foundation, 2024e)
44

RegressionEvaluator
from pyspark.ml.evaluation import RegressionEvaluator
evaluator = RegressionEvaluator(
labelCol="price",
predictionCol="prediction"
)
rmse = evaluator.setMetricName("rmse").evaluate(predictions)
mae = evaluator.setMetricName("mae").evaluate(predictions)
r2 = evaluator.setMetricName("r2").evaluate(predictions)
mse = evaluator.setMetricName("mse").evaluate(predictions)
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")
45

| Métricas soportadas:  |      |  ·  |  ·  |  ·  |  ·  |
| --------------------- | ---- | --- | --- | --- | --- |
|                       | rmse | mse | r2  | mae | var |
(Apache Software Foundation, 2024c)
46

Tuning: TrainValidationSplit y CrossValidator
from pyspark.ml.tuning import TrainValidationSplit, CrossValidator, ParamGridBuilder
paramGrid = (ParamGridBuilder()
.addGrid(lr.regParam, [0.01, 0.1, 1.0])
.addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0])
.build())
# Opción A: más rápido
tvs = TrainValidationSplit(
estimator=pipeline, estimatorParamMaps=paramGrid,
evaluator=evaluator, trainRatio=0.8)
# Opción B: más robusto
cv = CrossValidator(
estimator=pipeline, estimatorParamMaps=paramGrid,
evaluator=evaluator, numFolds=5)
best_model = cv.fit(train_df)
47

Guardado de Modelos e Integración con MLflow
import mlflow
import mlflow.spark
# Guardar con MLflow (tracking completo)
with mlflow.start_run():
model = pipeline.fit(train_df)
mlflow.log_param("regParam", 0.1)
mlflow.log_param("elasticNetParam", 0.0)
mlflow.log_metric("rmse", rmse)
mlflow.log_metric("r2", r2)
mlflow.spark.log_model(model, "spark-regression-model")
# Cargar modelo guardado
loaded = mlflow.spark.load_model("runs:/<run_id>/spark-regression-model")
48

Sin MLflow (método nativo Spark):
model.save("/models/regression_v1")
from pyspark.ml import PipelineModel
model = PipelineModel.load("/models/regression_v1")
(MLflow, 2024; Toumy, 2024)
49

Pipeline End-to-End: Ejemplo Completo
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
# 1. Carga de datos
df = spark.read.csv("housing.csv", header=True, inferSchema=True)
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)
# 2. Feature engineering
assembler = VectorAssembler(
inputCols=["rooms", "age", "distance", "income"],
outputCol="features")
# 3. Modelo con regularización Ridge
lr = LinearRegression(featuresCol="features", labelCol="price",
regParam=0.1, elasticNetParam=0.0)
# 4. Pipeline + entrenamiento
model = Pipeline(stages=[assembler, lr]).fit(train_df)
# 5. Evaluación
preds = model.transform(test_df)
ev = RegressionEvaluator(labelCol="price", predictionCol="prediction")
print(f"RMSE: {ev.setMetricName('rmse').evaluate(preds):.2f}")
print(f"R²: {ev.setMetricName('r2').evaluate(preds):.4f}") 50

Referencias
Analytics Vidhya. (2020). Support vector regression tutorial for machine learning.
https://www.analyticsvidhya.com/blog/2020/03/support-vector-regression-tutorial-for-machine-
learning/
AnalystPrep. (2024). Adjusted coefficient of determination. https://analystprep.com/study-
notes/cfa-level-2/quantitative-method/adjusted-coefficient-determination/
Apache Software Foundation. (2024a). VectorAssembler — PySpark 4.1.2 documentation.
https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.feature.VectorAssem
bler.html
Apache Software Foundation. (2024b). Extracting, transforming and selecting features —
Apache Spark 4.1.2. https://spark.apache.org/docs/latest/ml-features.html
51

Apache Software Foundation. (2024c). RegressionEvaluator — PySpark 4.1.1 documentation.
https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.evaluation.Regressio
nEvaluator.html
Apache Software Foundation. (2024d). ML tuning: Model selection and hyperparameter tuning
— Spark 4.1.2. https://spark.apache.org/docs/latest/ml-tuning.html
Apache Software Foundation. (2024e). Classification and regression — Apache Spark 4.1.1.
https://spark.apache.org/docs/latest/ml-classification-regression.html
Arize AI. (2024). Mean absolute percentage error (MAPE): What you need to know.
https://arize.com/blog-course/mean-absolute-percentage-error-mape-what-you-need-to-know/
52

Bhuva, L. (2024). Lasso regression: Unveiling the math behind feature selection and sparsity.
Medium. https://medium.com/@lomashbhuva/lasso-regression-unveiling-the-math-behind-
feature-selection-and-sparsity-e951f4cadabb
Brenndoerfer, M. (2024a). Ridge regression (L2 regularization): Complete guide with
mathematical foundations. https://mbrenndoerfer.com/writing/ridge-regression-l2-
regularization-complete-guide
Brenndoerfer, M. (2024b). Random forest: Complete guide to ensemble learning.
https://mbrenndoerfer.com/writing/random-forest-ensemble-learning-bootstrap-sampling-
feature-selection-classification-regression-guide
Built In. (2024a). Understanding ordinary least squares (OLS) regression.
https://builtin.com/data-science/ols-regression
53

Built In. (2024b). R-squared and adjusted R-squared: Explained. https://builtin.com/data-
science/adjusted-r-squared
DataCamp. (2024a). A guide to the gradient boosting algorithm.
https://www.datacamp.com/tutorial/guide-to-the-gradient-boosting-algorithm
DataCamp. (2024b). Coefficient of determination: What R-squared tells us.
https://www.datacamp.com/tutorial/coefficient-of-determination
GeeksforGeeks. (2024a). Linear regression in machine learning.
https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/
GeeksforGeeks. (2024b). Mean squared error: Definition, formula, interpretation and
examples. https://www.geeksforgeeks.org/maths/mean-squared-error/
54

Jainindore, A. (2024). Elastic net regression: Combined features of L1 and L2 regularization.
Medium. https://medium.com/@abhishekjainindore24/elastic-net-regression-combined-
features-of-l1-and-l2-regularization-6181a660c3a5
Keith, J. (2021). Handbook of regression modeling in people analytics. https://peopleanalytics-
regression-book.org/linear-reg-ols.html
Matalonga, H. (2024). Choosing between MAE, MSE and RMSE.
https://hmatalonga.com/blog/choosing-between-mae-mse-and-rmse/
Meng, X., Bradley, J., Yavuz, B., Sparks, E., Venkataraman, S., Liu, D., Freeman, J., Tsai, D.,
Amde, M., Owen, S., Xin, D., Xin, R., Franklin, M. J., Zadeh, R., Zaharia, M., & Talwalkar, A.
(2016). MLlib: Machine learning in Apache Spark. Journal of Machine Learning Research,
17(34), 1–7. https://arxiv.org/pdf/1505.06807
55

Mithani, D. (2023). Overfitting and underfitting with polynomial regression. Medium.
https://medium.com/@danish.mithani/overfitting-and-underfitting-with-polynomial-regression-
7a4ab2c8177a
MLflow. (2024). mlflow.spark. MLflow documentation.
https://mlflow.org/docs/latest/python_api/mlflow.spark.html
Mundal, S. (2024). Understanding MAE, MSE, and RMSE: Key metrics in machine learning.
DEV Community. https://dev.to/mondal_sabbha/understanding-mae-mse-and-rmse-key-
metrics-in-machine-learning-4la2
Oracle. (2024). Random forests, decision trees, and ensemble methods explained. Oracle AI
& Data Science Blog. https://blogs.oracle.com/ai-and-datascience/post/random-forests-
decision-trees-and-ensemble-methods-explained
56

Qualtrics. (2024). Interpreting residual plots to improve your regression.
https://www.qualtrics.com/support/stats-iq/analyses/regression-guides/interpreting-residual-
plots-improve-regression/
Runawayhorse001. (2024). Regression — Learning Apache Spark with Python.
https://runawayhorse001.github.io/LearningApacheSpark/regression.html
scikit-learn. (2024a). Lasso — scikit-learn 1.9.0 documentation. https://scikit-
learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html
scikit-learn. (2024b). ElasticNet — scikit-learn 1.9.0 documentation. https://scikit-
learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html
57

Sharma, S. (2024). Machine learning with PySpark MLlib: Part 1 regression. Medium.
https://sharmashorya1996.medium.com/machine-learning-with-pyspark-mllib-part-1-
regression-e7ad4d9780af
Six Sigma DSI. (2024). Residual analysis explained: Understand model fit & patterns.
https://sixsigmadsi.com/residual-analysis/
Statology. (2024). The five assumptions of multiple linear regression.
https://www.statology.org/multiple-linear-regression-assumptions/
Toumy, H. (2024). Saving and loading a model with, and without MLflow. Spark Notes.
https://haya-toumy.gitbook.io/spark-notes/pyspark/pyspark/related-to-ml/saving-and-loading-a-
model-with-and-without-mlflow
58

Towards Data Science. (2023). Assumptions of multiple linear regression.
https://towardsdatascience.com/assumptions-of-multiple-linear-regression-d16f2eb8a2e7/
Towards Data Science. (2024). 6 common metrics for your next regression project.
https://towardsdatascience.com/6-common-metrics-for-your-next-regression-project-
4667cbc534a7/
Vignesh, A. (2023). Supervised linear regression using OLS model. Medium.
https://22vignesh97.medium.com/supervised-linear-regression-using-ols-model-
d2561502343b
Wikipedia. (2024). Mean absolute error. https://en.wikipedia.org/wiki/Mean_absolute_error
59

¡Gracias!
60