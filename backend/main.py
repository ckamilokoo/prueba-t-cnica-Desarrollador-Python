from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import joblib
import os
from fastapi.staticfiles import StaticFiles

# Cargar modelo
modelo_path = os.path.join("..", "modelo", "modelo_ventas.joblib")
modelo = joblib.load(modelo_path)





# Inicializar app
app = FastAPI()

app.mount("/static", StaticFiles(directory="../graficos"), name="static")

# Plantillas HTML
templates = Jinja2Templates(directory="templates")

# Ruta raíz con formulario
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Predicción de ventas por año
@app.get("/predict/ventas")
def predecir_ventas(anio: int):
    # Cargar datos simulados
    ruta = os.path.join("..", "data", f"ventas_{anio}.csv")
    if not os.path.exists(ruta):
        return {"error": f"No existe el archivo para el año {anio}"}

    df = pd.read_csv(ruta)
    X = df[["anio", "mes", "producto", "clientes", "tienda"]]
    predicciones = modelo.predict(X)
    total = round(predicciones.sum(), 2)
    return {
        "anio": anio,
        "ventas_estimadas": total
    }

# Recomendación de stock
@app.get("/stock/recomendado")
def stock_recomendado(anio: int = 2028):
    ruta_csv = os.path.join("..", "data", f"ventas_{anio}.csv")
    if not os.path.exists(ruta_csv):
        return {"error": f"No existe el archivo de ventas para el año {anio}"}

    df = pd.read_csv(ruta_csv)

    # Obtener top 5 productos por ventas
    top5 = (
        df.groupby("producto")["monto_venta"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .index.tolist()
    )

    # Filtrar los que tienen rotación de al menos 12 meses
    df_top = df[df["producto"].isin(top5)]
    rotacion = df_top.groupby("producto")["mes"].nunique()
    rotantes = rotacion[rotacion >= 12].index.tolist()

    # Filtrar los productos válidos
    df_validados = df_top[df_top["producto"].isin(rotantes)]

    # Distribución proporcional del stock
    total_stock = 10000
    resumen = df_validados.groupby("tienda")["monto_venta"].sum()
    proporciones = resumen / resumen.sum()
    distribucion = (proporciones * total_stock).round().astype(int).sort_values(ascending=False)

    # Mostrar solo las 5 primeras tiendas
    top_tiendas = distribucion.head(5).to_dict()

    return {
        "anio": anio,
        "productos_validos": rotantes,
        "stock_top5_tiendas": top_tiendas
    }


# Listar gráficos generados
@app.get("/graficos")
def listar_graficos():
    ruta = os.path.join("..", "graficos")
    archivos = [f for f in os.listdir(ruta) if f.endswith(".png")]
    return {"graficos": archivos}
