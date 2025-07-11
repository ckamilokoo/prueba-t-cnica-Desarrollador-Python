# prueba-t-cnica-Desarrollador-Python

Predicción de Ventas y Stock
Óptimo para Joyería (2022–2030)
Contexto
Una empresa de joyería ha operado desde el año 2022 y desea predecir sus ventas futuras
para optimizar su stock, considerando el crecimiento en clientes, productos y tiendas. Como
parte del equipo de análisis, deberás construir un sistema predictivo que le permita tomar
mejores decisiones de negocio.
Entregables obligatorios
1. 3 archivos CSV simulados, uno por año:
○ ventas_2022.csv
○ ventas_2023.csv
○ ventas_2024.csv

Cada archivo debe contener al menos las siguientes columnas:
fecha,producto,cantidad_vendida,monto_venta,clientes,tienda
2. Y reflejar:
○ Mínimo 10 productos de joyería (ej: anillos, collares, pulseras, aros, etc.)
○ Diciembre con ventas notoriamente más altas
○ Crecimiento mensual y anual del 5%
○ Clientes en aumento mes a mes
○ Tiendas aumentando desde 40 en 2022 hasta 50 en 2030
○ Los gráficos por año (ventas totales, top 5 productos) deben estar generados
en el notebook y exportados como imágenes si es necesario.
3. Notebook Jupyter (pueden ser 2 archivos o secciones bien diferenciadas):
○ 01_entrenamiento_modelo.ipynb:

■ Carga de los 3 CSV
■ Análisis exploratorio
■ Visualización de ventas por año y por producto (incluyendo top 5)
■ Entrenamiento del modelo con Scikit-learn
■ Exportación del modelo (model.joblib o similar)
○ 02_uso_modelo_predictivo.ipynb:
■ Carga del modelo entrenado
■ Predicción de ventas para 2028 y 2029
■ Generación de gráficos con las predicciones
■ Estimación de stock óptimo para los top 5 productos
■ Lógica para evitar stock de productos que no rotan en 12 meses
■ Distribución del stock proyectado entre las tiendas
4. Gráficos generados (y guardados en carpeta graficos/):
○ ventas_2022.png, ventas_2023.png, ventas_2024.png
○ top5_2022.png, top5_2023.png, top5_2024.png
○ prediccion_2028.png, prediccion_2029.png
○ (Se puede usar Matplotlib, Seaborn, Plotly)

Entregables opcionales
4. Backend con FastAPI:
○ Endpoint /predict/ventas?anio=2029
○ Endpoint /stock/recomendado
○ Endpoint /graficos
5. Frontend HTML básico:
○ Renderizado por FastAPI con formulario
○ Muestra la predicción y gráficos

Requisitos técnicos
Datos simulados
● Ventas mensuales promedio: $5 millones
● Ventas en diciembre: $8 millones
● Aumento anual: 5% mensual acumulativo
● Clientes con crecimiento mensual (5% anual)
● Mínimo 10 productos por año
● Simular variedad en tiendas (de 40 en 2022 hasta 50 en 2030)

Modelo predictivo
● Algoritmo con Scikit-learn (árboles, regresión o similar)
● Entrenamiento supervisado usando datos históricos
● Variables consideradas: producto, mes, tienda, clientes, etc.
● Salida esperada: predicción de ventas por producto y tienda

Visualizaciones
● Gráfico de barras por año (ventas totales mensuales)
● Gráfico de líneas para top 5 productos
● Gráficos generados desde el modelo para 2028 y 2029

Lógica de stock
● Solo top 5 productos por año deben ser considerados para stock
● No mantener productos con stock sin venta >12 meses
● Stock debe distribuirse proporcionalmente entre tiendas activas

Estructura de entrega sugerida
.
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
│ └── templates/index.html
└── README.md