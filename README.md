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

## Roadmap de trabajo

- [x] **Fase 1 — EDA** (`01_eda.ipynb`): parsing de campos sucios con funciones nativas de Spark
      SQL, tratamiento de nulos, análisis de correlación de atributos vs. `Transfer Value`.
- [x] **Fase 2 — Clustering** (`02_clustering.ipynb`): K-Means con Spark MLlib, selección de k
      (codo + `ClusteringEvaluator` silhouette), perfil de negocio por cluster, motor de
      "jugadores clon" (distancia euclidiana / similitud coseno).
- [x] **Fase 3 — Supervisado** (`03_supervised.ipynb`): regresión (`LinearRegression` vs.
      `GBTRegressor`, CV) para `Transfer Value`; clasificación (`LogisticRegression` vs.
      `RandomForest`, CV) para potencial internacional vía `Caps`; importancia de variables.
- [ ] **Sustentación**: presentación ejecutiva (máx. 15 min) traduciendo métricas a decisiones
      de negocio.

### Resultados de referencia (última ejecución)

- Regresión (`Transfer_Value_num`): `GBTRegressor` + CV → R² test ≈ 0.49, RMSE test ≈ 4.6M
  (vs. R² ≈ 0.12 de `LinearRegression` simple).
- Clasificación (potencial/`Caps`): F1 test ≈ 0.90, AUC test ≈ 0.86. Variables más importantes:
  compostura (`Cmp`), balance (`Bal`), ambición (`Amb`), anticipación (`Ant`).
- El modelo, aplicado a menores de 21 años, identifica correctamente como top prospects a
  jugadores reales de élite (Bellingham, Musiala, Vinícius Jr., Haaland, Gavi, Pedri), y también
  señala "falsos positivos" interesantes para discutir en la sustentación (ej. Curtis Jones,
  Harvey Elliott).
