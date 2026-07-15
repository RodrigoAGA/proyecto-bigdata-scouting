# Sistema Global de Inteligencia de Mercado y Scouting Deportivo

Proyecto capstone de Big Data / Machine Learning para un consorcio de clubes de fútbol.
El objetivo es reemplazar decisiones basadas en intuición por un sistema analítico que:

1. Segmente el mercado de jugadores (clustering) y permita buscar "clones" de bajo costo de superestrellas.
2. Prediga el `Transfer Value` y clasifique el potencial de jóvenes talentos (proyección de `Caps`).
3. Sustente ante un comité ejecutivo las decisiones de modelado con métricas traducidas a valor de negocio.

El pipeline completo está construido con **PySpark / Spark MLlib** (Spark SQL para la limpieza y
EDA, Pipeline API para clustering y modelos supervisados), siguiendo las herramientas enseñadas en
el curso en lugar de un enfoque puramente pandas/scikit-learn.

## Estructura del repositorio

```
.
├── data/
│   ├── raw/              # merged_players.csv original, sin modificar
│   └── processed/        # players_clean.parquet generado por 01_eda.ipynb
├── notebooks/
│   ├── 01_eda.ipynb              # limpieza (Spark SQL), nulos, correlaciones (Fase 1)
│   ├── 02_clustering.ipynb       # segmentación con Spark MLlib KMeans (Fase 2)
│   └── 03_supervised.ipynb       # regresión y clasificación con Spark MLlib (Fase 3)
├── reports/
│   └── figures/          # gráficos exportados para la sustentación
│       ├── clustering_k_selection.png    # codo + silhouette (Fase 2)
│       ├── clusters_pca_2d.png           # clusters proyectados en 2D via PCA (Fase 2)
│       └── pca_varianza_explicada.png    # varianza acumulada del PCA (Fase 1)
├── requirements.txt
└── README.md
```

## Setup del entorno

Requiere Java 17 (JDK) para que PySpark pueda arrancar la JVM. En macOS con Homebrew:

```bash
brew install openjdk@17
```

Entorno Python:

```bash
python3 -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Antes de correr los notebooks, exportar `JAVA_HOME` apuntando al JDK instalado (no requiere
symlink global ni `sudo`):

```bash
export JAVA_HOME=/opt/homebrew/opt/openjdk@17   # ajustar segun tu instalacion
```

Para trabajar en los notebooks:

```bash
source venv/bin/activate
jupyter lab
```

Cada notebook crea su propia `SparkSession` en modo `local[*]` (un solo proceso, sin cluster
externo), tal como se usa en el curso.

## Dataset

`data/raw/merged_players.csv`: 91,672 jugadores, 88 columnas (atributos físicos, técnicos,
mentales, posición, valor de transferencia, internacionalidades, etc.). Requiere limpieza antes
de modelar:

- `Height` (`5'9"`) → centímetros.
- `Weight` (`65 kg`) → kilogramos.
- `Transfer Value`: no es un valor único sino un **rango** con sufijos K/M (`'250K$ - 2.5M$'`), o
  `'Not for Sale'` para jugadores sin valor de mercado definido (2,051 casos, excluidos de la
  regresión).
- Columnas con `-` como marcador de nulo (`Caps`, `AT Apps`, `AT Gls`, etc.). `Rec` usa `'- - -'`
  y es categórica, no numérica.
- `Nat.1`: nombre de columna duplicado (segundo atributo `Nat` = habilidad natural), renombrado a
  `Habilidad_Natural` para evitar conflictos con APIs que interpretan el punto como acceso a campo
  anidado.
- **Atípicos**: se valida `Height_cm`/`Weight_kg` contra un rango fisiológicamente plausible
  (140–210cm, 50–110kg) y se marcan como nulos los que caen fuera (errores de captura). Los
  atípicos de `Transfer_Value_num` (las superestrellas) **no se tocan**: son justo el segmento que
  el consorcio quiere modelar (ver motor de "clones", Fase 2).

## Roadmap de trabajo

- [x] **Fase 1 — EDA** (`01_eda.ipynb`): parsing de campos sucios con funciones nativas de Spark
      SQL, tratamiento de nulos y atípicos (criterio IQR + validación de rangos físicos),
      análisis de correlación de atributos vs. `Transfer Value`, y reducción de dimensionalidad
      (PCA) para cuantificar la redundancia entre atributos.
- [x] **Fase 2 — Clustering** (`02_clustering.ipynb`): K-Means con Spark MLlib, selección de k
      (codo + `ClusteringEvaluator` silhouette, con justificación explícita de por qué se acepta
      un silhouette modesto), perfil de negocio por cluster (medias de atributos + interpretación
      narrativa de cada arquetipo), visualización 2D de los clusters vía PCA, y motor de
      "jugadores clon" (distancia euclidiana / similitud coseno).
- [x] **Fase 3 — Supervisado** (`03_supervised.ipynb`): regresión (`LinearRegression` vs.
      `GBTRegressor`, CV) para `Transfer Value` con error segmentado por tramo de valor;
      clasificación (`LogisticRegression` vs. `RandomForest`, CV) para potencial internacional vía
      `Caps`, con matriz de confusión, análisis de la clase minoritaria y barrido de umbral de
      decisión; importancia de variables y traducción de ambos modelos a impacto de negocio.
- [ ] **Sustentación**: presentación ejecutiva (máx. 15 min) traduciendo métricas a decisiones
      de negocio.

### Resultados de referencia (última ejecución)

**Fase 1 — EDA:**
- Atípicos físicos: prácticamente ninguno tras el parsing (0 en `Height_cm`, 1 en `Weight_kg`
  marcado nulo); 14,010 "atípicos" en `Transfer_Value_num` por IQR, todos legítimos (superestrellas)
  y conservados a propósito.
- Correlación individual más alta con `Transfer_Value_num`: atributos mentales/técnicos
  (`Cmp` compostura 0.17, `Ant` anticipación 0.16, `Tea` juego en equipo 0.15) por encima de los
  físicos puros — pero con magnitudes modestas, ningún atributo aislado explica el valor por sí solo.
- PCA: el primer componente explica ~25% de la varianza, los dos primeros ~38%; se necesitan 15
  componentes para llegar a ~70% — evidencia de que la habilidad de un jugador es genuinamente
  multidimensional, lo que justifica usar el conjunto completo de atributos en Fases 2 y 3 en vez
  de reducir a 2-3 componentes.

**Fase 2 — Clustering:**
- `K=5` (silhouette baja casi monótonamente desde `k=2`; se prioriza granularidad de negocio sobre
  el máximo trivial de silhouette).
- 5 arquetipos identificados: "Elite/completos" (13,111 jugadores, valor promedio ≈ $5.46M),
  "Atacantes rápidos/técnicos" (24,253, ≈ $562,943), "Trabajadores disciplinados" (20,446,
  ≈ $370,797), "Talento físico sin consolidar" (20,014, ≈ $119,030) y "Versátiles de rol" (12,711,
  ≈ $104,726).
- El motor de "clones" busca, dentro del cluster de una superestrella, jugadores con menor valor de
  mercado y features estadísticamente equivalentes (distancia euclidiana / similitud coseno).

**Fase 3 — Supervisado:**
- Regresión (`Transfer_Value_num`): `GBTRegressor` + CV → R² test ≈ 0.35, MAE test ≈ $982K
  (vs. R² ≈ 0.12 de `LinearRegression` simple). El error absoluto crece con el precio del jugador
  (de ~$358K en el tramo `< $100K` a ~$18.9M en `>= $10M`) — el modelo es relativamente peor en el
  tramo más barato (60% del dataset), una limitación real documentada para la siguiente iteración
  (modelar `log(Transfer_Value_num)`).
- Clasificación (potencial/`Caps`): F1 ponderado ≈ 0.90, AUC ≈ 0.86 — pero esa métrica agregada
  esconde un desbalance de clases severo (8.5% positivos): con el umbral por defecto, **recall en
  la clase de interés es de solo ~0.11** (precision ≈0.83). El barrido de umbral muestra que bajar
  el corte a ~0.15 recupera recall ≈0.61 a cambio de precision ≈0.35 — un intercambio favorable
  dado que el costo de un falso negativo (talento perdido) es mucho mayor que el de un falso
  positivo (tiempo de scouting).
- El modelo, aplicado a menores de 21 años, identifica correctamente como top prospects a
  jugadores reales de élite (Haaland, Bellingham, Saka, Gavi, Vinícius Jr., Pedri, Musiala).
