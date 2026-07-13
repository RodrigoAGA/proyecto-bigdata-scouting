# Sistema Global de Inteligencia de Mercado y Scouting Deportivo

Proyecto capstone de Big Data / Machine Learning para un consorcio de clubes de fútbol.
El objetivo es reemplazar decisiones basadas en intuición por un sistema analítico que:

1. Segmente el mercado de jugadores (clustering) y permita buscar "clones" de bajo costo de superestrellas.
2. Prediga el `Transfer Value` y clasifique el potencial de jóvenes talentos (proyección de `Caps`).
3. Sustente ante un comité ejecutivo las decisiones de modelado con métricas traducidas a valor de negocio.

Ver el enunciado completo en [`docs/enunciado.md`](docs/enunciado.md) (convertido desde `enunciado.docx`).

## Material de curso (docs/)

Los PDFs de teoría del curso están en la raíz del proyecto y su conversión a markdown (vía
[markitdown](https://github.com/microsoft/markitdown)) en `docs/`:

| PDF | Markdown |
| --- | --- |
| `1. fundamentos del big data.pdf` | `docs/01_fundamentos_del_big_data.md` |
| `2. infraestructura para datos.pdf` | `docs/02_infraestructura_para_datos.md` |
| `3. paradigma mapReduce.pdf` | `docs/03_paradigma_mapreduce.md` |
| `4. hadoop.pdf` | `docs/04_hadoop.md` |
| `5. spark.pdf` | `docs/05_spark.md` |
| `abd_usos_bigdata.pdf` | `docs/abd_usos_bigdata.md` |
| `abd_no_supervisado.pdf` | `docs/abd_no_supervisado.md` |
| `abd_clasificacion.pdf` | `docs/abd_clasificacion.md` |
| `abd_regresion.pdf` | `docs/abd_regresion.md` |
| `introduccion_machine_learning.pdf` | `docs/introduccion_machine_learning.md` |
| `spark_sql.pdf` | `docs/spark_sql.md` |

## Estructura del repositorio

```
.
├── data/
│   ├── raw/              # merged_players.csv original, sin modificar
│   └── processed/        # datasets limpios generados por el notebook de EDA
├── docs/
│   └── enunciado.md      # enunciado del proyecto en markdown
├── notebooks/
│   ├── 01_eda.ipynb              # limpieza, nulos, correlaciones (Fase 1)
│   ├── 02_clustering.ipynb       # segmentación no supervisada (Fase 2)
│   └── 03_supervised.ipynb       # predicción y clasificación (Fase 3)
├── src/
│   └── data_cleaning.py  # funciones reutilizables de parsing (altura, peso, moneda)
├── reports/
│   └── figures/          # gráficos exportados para la sustentación
├── requirements.txt
└── README.md
```

## Setup del entorno

```bash
python3 -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Para trabajar en los notebooks:

```bash
source venv/bin/activate
jupyter lab
```

## Dataset

`data/raw/merged_players.csv`: ~91,672 jugadores, 88 columnas (atributos físicos, técnicos,
mentales, posición, valor de transferencia, internacionalidades, etc.). Requiere limpieza antes
de modelar:

- `Height` (`5'9"`) → centímetros o pulgadas numéricas.
- `Weight` (`65 kg`) → kilogramos numéricos.
- `Transfer Value` (`0$`) → valor numérico.
- Columnas con `-` como marcador de nulo (`Caps`, `AT Apps`, etc.).

## Roadmap de trabajo

- [ ] **Fase 1 — EDA**: parsing de campos sucios, tratamiento de nulos/atípicos, análisis de
      correlación y reducción de dimensionalidad.
- [ ] **Fase 2 — Clustering**: selección y justificación del algoritmo, número óptimo de
      clusters (codo/silueta), interpretación de perfiles, motor de "jugadores clon".
- [ ] **Fase 3 — Supervisado**: modelos de regresión (Transfer Value) y clasificación (potencial
      /Caps), comparación de métricas, control de overfitting, importancia de variables.
- [ ] **Sustentación**: presentación ejecutiva (máx. 15 min) traduciendo métricas a decisiones
      de negocio.
