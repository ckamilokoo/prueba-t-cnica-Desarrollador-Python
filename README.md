# Prueba Técnica – Desarrollador Python

## Predicción de Ventas y Stock Óptimo para Joyería (2022–2030)

### 🧠 Contexto

Una empresa de joyería ha operado desde el año 2022 y desea **predecir sus ventas futuras** para optimizar su stock, considerando el crecimiento de clientes, productos y tiendas.

Como parte del equipo de análisis, deberás construir un **sistema predictivo** que le permita tomar mejores decisiones de negocio.

---

## ✅ Entregables obligatorios

### 1. Datos simulados (CSV)

Se deben entregar **3 archivos CSV simulados**, uno por año:

- `ventas_2022.csv`
- `ventas_2023.csv`
- `ventas_2024.csv`

Cada archivo debe contener las siguientes columnas:

fecha, producto, cantidad_vendida, monto_venta, clientes, tienda


Los datos deben reflejar:

- Al menos **10 productos de joyería** (anillos, collares, pulseras, aros, etc.)
- **Ventas más altas en diciembre**
- **Crecimiento mensual y anual del 5%**
- **Aumento de clientes** mes a mes
- Aumento en el número de tiendas: de **40 en 2022** hasta **50 en 2030**
- Gráficos generados por año:
  - Ventas totales
  - Top 5 productos

---

### 2. Notebooks Jupyter

#### 📘 `01_entrenamiento_modelo.ipynb`

Debe incluir:

- Carga de los 3 CSV
- Análisis exploratorio de datos
- Visualización de:
  - Ventas por año
  - Ventas por producto (Top 5 incluidos)
- Entrenamiento del modelo (con `Scikit-learn`)
- Exportación del modelo entrenado (`model.joblib` o similar)

#### 📗 `02_uso_modelo_predictivo.ipynb`

Debe incluir:

- Carga del modelo entrenado
- Predicción de ventas para los años **2028 y 2029**
- Generación de gráficos de predicción
- Estimación de stock óptimo para los **Top 5 productos**
- Lógica para eliminar productos sin rotación de 12 meses
- Distribución del stock proyectado entre tiendas activas

---

### 3. Gráficos generados

Guardar los gráficos en la carpeta `graficos/`. Archivos requeridos:

- `ventas_2022.png`, `ventas_2023.png`, `ventas_2024.png`
- `top5_2022.png`, `top5_2023.png`, `top5_2024.png`
- `prediccion_2028.png`, `prediccion_2029.png`

**Herramientas sugeridas:** `Matplotlib`, `Seaborn`, `Plotly`

---

## 🧪 Entregables opcionales

### 4. Backend con FastAPI

Endpoints sugeridos:

- `GET /predict/ventas?anio=2029`
- `GET /stock/recomendado`
- `GET /graficos`

### 5. Frontend HTML básico

- Formulario HTML simple para hacer predicciones
- Renderizado con FastAPI (`Jinja2`)
- Visualización de predicciones y gráficos

---

## ⚙️ Requisitos técnicos

### Datos simulados

- Ventas mensuales promedio: **$5 millones**
- Ventas en diciembre: **$8 millones**
- Aumento anual: **5% mensual acumulativo**
- Crecimiento de clientes mensual
- Mínimo **10 productos por año**
- Número de tiendas: de **40 (2022)** a **50 (2030)**

### Modelo predictivo

- Algoritmo: `Scikit-learn` (árboles, regresión, etc.)
- Entrenamiento supervisado usando datos históricos
- Variables consideradas:
  - Producto, mes, tienda, clientes, etc.
- Salida esperada:
  - Predicción de ventas por producto y tienda

### Visualizaciones

- Gráfico de barras por año (ventas totales mensuales)
- Gráfico de líneas (top 5 productos)
- Gráficos de predicción para 2028 y 2029

### Lógica de stock

- Solo se consideran los **Top 5 productos por año**
- Eliminar stock de productos sin venta en 12 meses
- Distribuir stock proporcionalmente entre tiendas activas

---

## 📁 Estructura de entrega sugerida

├── data/
│ ├── ventas_2022.csv
│ ├── ventas_2023.csv
│ └── ventas_2024.csv
├── notebooks/
│ ├── 01_entrenamiento_modelo.ipynb
│ └── 02_uso_modelo_predictivo.ipynb
├── graficos/
│ ├── ventas_2022.png
│ ├── top5_2022.png
│ └── ...
├── modelo/
│ └── modelo_ventas.joblib
├── backend/ (opcional)
│ ├── main.py
│ └── templates/
│ └── index.html
└── README.md