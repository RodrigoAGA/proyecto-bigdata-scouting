FACULTAD DE INGENIERÍA
CARRERA DE INGENIERÍA DE SISTEMAS
Aprendizaje No
Supervisado
Analítica con Big Data · 2026-1
1

Agenda
Contenido de la sesión
1. Introducción al Aprendizaje No Supervisado
2. Agrupamiento (Clustering)
K-Means, DBSCAN
Métricas de evaluación
3. PCA — Análisis de Componentes Principales
2

SECCIÓN 1
Introducción al Aprendizaje
No Supervisado
Definición, tipos de tareas y métricas de evaluación
3

Aprendizaje No Supervisado
Definición y diferencias con otros paradigmas
Supervisado Semi-supervisado
Los datos tienen etiquetas conocidas (y) Mezcla de datos etiquetados y sin
→ etiquetar
El modelo aprende la función f(x) y
Aprovecha la estructura latente del
Ejemplos: clasificación, regresión
conjunto
4

No supervisado
Los datos no tienen etiquetas
El modelo descubre patrones, estructura y agrupaciones por sí solo
Objetivo: aprender la distribución subyacente de los datos
El modelo no recibe retroalimentación externa sobre si sus predicciones son
correctas (IBM, s.f.; Chust, s.f.).
5

Tipos de Tareas No Supervisadas
| Categoría | Objetivo | Ejemplos |
| --------- | -------- | -------- |
K-Means, DBSCAN,
| Clustering | Agrupar observaciones similares |     |
| ---------- | ------------------------------- | --- |
Jerárquico
| Reducción de | Comprimir información preservando |     |
| ------------ | --------------------------------- | --- |
PCA, t-SNE, UMAP
| dimensionalidad | varianza                              |                      |
| --------------- | ------------------------------------- | -------------------- |
|                 | Aprender la distribución para generar | VAE, GAN, modelos de |
Modelos generativos
|     | nuevos datos | mezcla |
| --- | ------------ | ------ |
Isolation Forest, One-
Detección de anomalías Identificar puntos atípicos o inusuales
Class SVM
| Sistemas de | Descubrir relaciones latentes entre |     |
| ----------- | ----------------------------------- | --- |
Filtrado colaborativo
| recomendación | usuarios e ítems |     |
| ------------- | ---------------- | --- |
6

Métricas de Evaluación Sin Etiquetas
Intrínsecas (sin ground truth) Extrínsecas (con etiquetas de
referencia)
Miden la calidad interna de los
Comparan los clusters con etiquetas
agrupamientos:
conocidas (solo para evaluación, no para
Silhouette Score — cohesión vs.
entrenamiento):
separación
Rand Index (RI / ARI)
Davies-Bouldin Index — relación entre
Mutual Information (NMI)
dispersión y distancia entre clusters
Homogeneity & Completeness
Calinski-Harabasz Index — varianza
inter-cluster vs. intra-cluster
7

En producción las métricas intrínsecas son las únicas disponibles. Las extrínsecas
solo se usan en benchmarking (Kashnitsky, s.f.).
8

SECCIÓN 2
Agrupamiento (Clustering)
K-Means, Jerárquico, DBSCAN y evaluación
9

K-Means
Algoritmo, centroides y convergencia
Pasos del algoritmo
1. Inicializar K centroides aleatorios (o con K-Means++)
2. Asignar cada punto al centroide más cercano (distancia euclidiana)
3. Recalcular el centroide de cada cluster como la media de sus puntos
4. Repetir pasos 2–3 hasta convergencia (sin cambios en las asignaciones)
10

Función objetivo (inercia):
Limitaciones:
Sensible a la inicialización
Asume clusters esféricos y de tamaño
Minimiza la suma de distancias cuadradas al
similar
centroide.
Requiere definir K a priori
11

K-Means++
Inicialización inteligente de centroides
El método estándar de inicialización aleatoria puede converger a mínimos locales
subóptimos.
K-Means++ (Arthur & Vassilvitskii, 2007)
1. Elegir el primer centroide aleatoriamente de los datos
2. Para cada punto restante, calcular su distancia al centroide más cercano ya elegido: D(x)
3. Seleccionar el siguiente centroide con probabilidad proporcional a D(x)²
4. Repetir hasta tener K centroides
12

K-Means++ garantiza una solución O(log K)-competitiva en esperanza respecto al óptimo
global. Reduce drásticamente iteraciones necesarias y mejora la calidad del clustering
final (Kashnitsky, s.f.).
13

Selección del Número de Clusters
Elbow Method Silhouette Score
Grafica la inercia (WCSS) en función de K. Mide la cohesión y separación.
La inercia es la suma de las distancias al Para cada punto i:
cuadrado entre los puntos y el centroide.
La inercia disminuye monotónicamente al
aumentar K
a(i): distancia media intra-cluster
El "codo" marca el punto de rendimientos
b(i): distancia media al cluster vecino más
decrecientes
cercano
K óptimo = punto de inflexión de la curva
Rango: [-1, 1] — cuanto mayor, mejor
14
separación

Combinar ambas métricas evita elegir K erróneamente cuando el codo no es claro
(Kashnitsky, s.f.).
15

DBSCAN
Clustering basado en densidad
Density-Based Spatial Clustering of Applications with Noise
Parámetros clave
ε (eps): radio de vecindad
MinPts: número mínimo de puntos para formar una región densa
16

Clasificación de puntos
Tipo Condición
Core point Tiene ≥ MinPts vecinos dentro de radio ε
Border point Vecino de un core point pero con < MinPts vecinos propios
Noise (outlier) No es core ni border point
Ventaja clave: detecta clusters de forma arbitraria y etiqueta automáticamente ruido y
outliers sin necesitar K
17

Cálculo de ε con Distancia K
Se fija como MinPts = 4 ( o doble de las dimensiones)
1. Para cada punto del dataset, calcular la distancia a su 4to vecino más cercano.
2. Ordenar las distancias de menor a mayor.
3. Graficar los puntos en el eje X (ordenados) y su distancia en el eje Y.
18

Evaluación de Clustering
Silhouette, Davies-Bouldin y Calinski-Harabasz
| Métrica | Fórmula | Interpretación | Óptimo |
| ------- | ------- | -------------- | ------ |
→
Máximo
| Silhouette | (b−a)/max(a,b) | Cohesión vs. separación por punto |     |
| ---------- | -------------- | --------------------------------- | --- |
1
→
|                |                    | Razón dispersión intra / distancia | Mínimo  |
| -------------- | ------------------ | ---------------------------------- | ------- |
| Davies-Bouldin | Media de max(Ri,j) |                                    |         |
|                |                    | inter                              | 0       |
| Calinski-      | Tr(Bk)/Tr(Wk) ×    |                                    |         |
|                |                    | Varianza entre clusters vs. dentro | Máximo  |
| Harabasz       | (n−k)/(k−1)        |                                    |         |
19

Cuándo usar cada una
Silhouette: comparar distintos K o algoritmos; interpretable intuitivamente
Davies-Bouldin: penaliza clusters compactos pero cercanos entre sí
Calinski-Harabasz: rápida de calcular; útil para grandes datasets
(Kashnitsky, s.f.)
20

SECCIÓN 3
PCA
Análisis de Componentes Principales
21

Fundamentos Matemáticos de PCA
Varianza, covarianza, eigenvectores y eigenvalores
Idea central
PCA encuentra las direcciones de máxima varianza en los datos proyectando a un nuevo
espacio ortogonal.
22

Pasos matemáticos: Interpretación:
̃ →
1. Centrar los datos: X = X − μ Eigenvalores varianza capturada por
cada componente
2. Calcular la matriz de covarianza: Σ =
̃ᵀ ̃ →
(1/n) X X Eigenvectores dirección de cada
componente principal
3. Calcular eigenvectores (componentes
principales) y eigenvalores de Σ Componentes son ortogonales entre sí
(sin correlación)
4. Ordenar por eigenvalor descendente
̃
5. Proyectar: Z = X · W_k
PCA es equivalente a la SVD de la
matriz de datos centrada (UC Berkeley
CS 189, s.f.).
23

Reducción de Dimensionalidad con
PCA
Varianza explicada y selección de componentes
Varianza explicada acumulada
donde λᵢ son los eigenvalores ordenados de mayor a menor.
24

Criterios de selección de K:
from sklearn.decomposition import PCA
Umbral de varianza: retener K que pca = PCA(n_components=0.95) # 95% varianza
X_reduced = pca.fit_transform(X_scaled)
explique ≥ 95% (o 90%) de la varianza
print(pca.explained_variance_ratio_)
total
print(pca.n_components_)
Scree plot: buscar el "codo" en la curva de
(Kashnitsky, s.f.; DataCamp, s.f.)
eigenvalores
Kaiser rule: retener componentes con
eigenvalor > 1
25

Visualización con PCA
Proyección de datos a 2D y 3D
PCA permite proyectar datos de alta dimensión a 2 o 3 componentes para visualización
exploratoria.
26

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
pca2d = PCA(n_components=2)
X_2d = pca2d.fit_transform(X_scaled)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap='tab10')
plt.xlabel(f'PC1 ({pca2d.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca2d.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('Proyección PCA 2D')
plt.show()
Etiquetar los ejes con el porcentaje de varianza explicada es buena práctica: permite
evaluar cuánta información se pierde en la proyección. Para datos muy no lineales, t-SNE
o UMAP producen mejores visualizaciones.
27

Preprocesamiento antes de PCA
Normalización y estandarización
PCA es sensible a la escala de las variables. Sin estandarización, las variables con
mayor magnitud dominarán las primeras componentes, independientemente de su
relevancia real.
28

from sklearn.preprocessing import StandardScaler
StandardScaler (recomendado para
from sklearn.decomposition import PCA
PCA)
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
('scaler', StandardScaler()),
('pca', PCA(n_components=0.95))
])
Media 0, desviación estándar 1
X_transformed = pipeline.fit_transform(X)
Preserva la forma de la distribución
MinMaxScaler
Rango [0, 1]
Sensible a outliers
29

Referencias
4Geeks. (s.f.). Aprendizaje no supervisado. 4Geeks Academy.
https://4geeks.com/es/lesson/aprendizaje-no-supervisado
AI Future School. (s.f.). Unsupervised learning techniques explained. https://www.ai-
futureschool.com/en/programming/unsupervised-learning-techniques-explained.php
Chust, A. (s.f.). Aprendizaje no supervisado. https://adrianchust.com/aprendizaje-no-supervisado/
DataCamp. (s.f.). Unsupervised learning in Python [Curso en línea].
https://www.datacamp.com/courses/unsupervised-learning-in-python
30

IBM. (s.f.). ¿Qué es el aprendizaje no supervisado? IBM Think.
https://www.ibm.com/think/topics/unsupervised-learning
Kashnitsky, Y. (s.f.). Topic 7: Unsupervised learning — PCA and clustering [Notebook]. Kaggle.
https://www.kaggle.com/code/kashnitsky/topic-7-unsupervised-learning-pca-and-clustering
MICROCHIPOTLE. (s.f.). Aprendizaje no supervisado en machine learning: técnicas y
aplicaciones. https://microchipotle.com/aprendizaje-no-supervisado-en-machine-learning-
tecnicas-y-aplicaciones/
UC Berkeley. (s.f.). CS 189/289A: Introduction to Machine Learning [Notas de curso].
https://people.eecs.berkeley.edu/~jrs/189/
31