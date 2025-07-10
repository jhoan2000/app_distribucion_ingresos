from datetime import datetime

def obtener_fecha_actual_formateada():
    return datetime.now().strftime("%Y-%m-%d")

def formatear_moneda(valor):
    return f"${valor:,.0f}".replace(",", ".")  # Cambia , por . si lo usas en español
