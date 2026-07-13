**PROYECTO CAPSTONE: *Sistema Global de Inteligencia de Mercado y Scouting Deportivo***

**1. CONTEXTO DE NEGOCIO**

Ustedes han sido contratados como el equipo de Consultoría en Analítica Avanzada y Big Data para un consorcio internacional de clubes de fútbol. Históricamente, las decisiones de fichajes, renovación de contratos y asignación de salarios en el consorcio se han basado en la intuición de los directores deportivos y reportes cualitativos de los visores (scouts). Este enfoque tradicional ha generado ineficiencias financieras significativas, incluyendo la compra de jugadores sobrevalorados y la pérdida de talentos emergentes en ligas secundarias.

Para mitigar este problema, el consorcio ha adquirido un dataset global unificado (merged\_players.csv) que contiene registros detallados de miles de jugadores profesionales de todo el mundo. Este dataset incluye atributos físicos, habilidades técnicas, características psicológicas, posiciones tácticas, lesiones históricas y valoraciones de mercado actuales. El objetivo del consorcio es realizar una transición completa hacia un modelo de gestión basado en datos (estrategia Moneyball Avanzada).

**2. OBJETIVOS DEL PROYECTO CAPSTONE**

El equipo de consultores deberá diseñar, implementar y sustentar un Sistema Analítico que resuelva las siguientes necesidades estratégicas utilizando técnicas avanzadas de Machine Learning:

* **Modelamiento No Supervisado:** Segmentar el mercado de jugadores para descubrir perfiles tácticos ocultos, identificar grupos homogéneos de rendimiento y diseñar un motor de búsqueda de 'clones' (jugadores de bajo costo con un perfil estadístico idéntico al de superestrellas inalcanzables).
* **Modelamiento Supervisado:** Desarrollar modelos predictivos robustos para estimar el valor de transferencia (Transfer Value) de los jugadores, identificar qué variables influyen críticamente en la valoración y clasificar el potencial de éxito de los jóvenes talentos (proyecciones de internacionalidades/Caps).
* **Sustentación de Negocio y Defensa de Decisiones:** Argumentar técnicamente la elección de los algoritmos utilizados ante el Comité Ejecutivo del Consorcio, demostrando rigor estadístico y traduciendo las métricas de rendimiento (RMSE, MAE, R², F1-Score, Silhouette Index) en impacto financiero y deportivo.

**3. FASES Y REQUISITOS TÉCNICOS**

**Fase 1: Ingeniería de Datos y Análisis Exploratorio (EDA)**• Limpieza y Transformación: El dataset contiene variables en formatos no listos para modelos (ej. alturas en formato de pies y pulgadas como 5'9", pesos con texto 'kg', y valores de transferencia con símbolos monetarios). Es obligatorio realizar el parsing y conversión a formato numérico puro.
• Tratamiento de Nulos y Atípicos: Sustentar la estrategia de imputación u omisión de datos faltantes.
• Análisis de Correlación y Reducción de Dimensionalidad: Analizar cómo interactúan los atributos mentales, físicos y técnicos con el valor económico del jugador.

**Fase 2: Analítica No Supervisada (Clustering & Segmentación)**El equipo debe seleccionar, justificar e implementar un algoritmo de aprendizaje no supervisado (ej. K-Means). Deben responder a:
• ¿Cómo se determinó el número óptimo de clusters? (Demostrar mediante el Método del Codo, Coeficiente de Silueta, etc.).
• ¿Cuál es la interpretación de cada cluster encontrado? Describir el perfil de negocio de los grupos.
• Aplicación Práctica: Presentar un caso de uso de 'Búsqueda de Reemplazos Similares' utilizando distancias estadísticas (ej. Distancia Euclidiana o Similitud de Coseno).

**Fase 3: Analítica Supervisada (Predicción y Clasificación)**El equipo debe seleccionar, evaluar y comparar libremente algoritmos supervisados Deben:
• Justificar la división de datos (Train/Test o Cross-Validation).
• Evaluar y contrastar los modelos mediante múltiples métricas de rendimiento.
• Explicar y controlar activamente el riesgo de sobreajuste (Overfitting).

**4. ENTREGABLES Y SUSTENTACIÓN**

Cada equipo presentará los siguientes entregables:

1. Repositorio de Código o Notebook estructurado: Limpio, comentado, con celdas ejecutables que muestren el pipeline de datos desde la carga hasta la evaluación de modelos.
2. Presentación Ejecutiva (Sustentación Oral): Máximo 15 minutos de exposición seguidos de una ronda de preguntas del comité (profesor). El enfoque debe ser híbrido: rigor técnico combinado con traducción de resultados a decisiones de negocio.

**5. MATRIZ DE EVALUACIÓN (RÚBRICA)**

|  |  |  |
| --- | --- | --- |
| Criterio de Evaluación | Aspectos Técnicos Esperados | Peso |
| Ingeniería de Datos y EDA | Limpieza correcta de cadenas complejas (altura, peso, moneda). Tratamiento de nulos y justificación de variables seleccionadas. | 20% |
| Modelamiento No Supervisado | Sustentación matemática del número de clusters. Interpretación cualitativa y aplicación práctica del algoritmo seleccionado. | 30% |
| Modelamiento Supervisado | Comparación de modelos, métricas de error/precisión bien justificadas, control de overfitting y análisis de importancia de variables. | 30% |
| Sustentación Oral y Negocio | Capacidad para defender las decisiones de algoritmos ante el comité y traducir métricas abstractas en valor comercial/deportivo. | 20% |