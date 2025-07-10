import json
import os

RUTA_ARCHIVO = "data/registros.json"

def cargar_registros():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        try:
            registros = json.load(f)
            return registros if isinstance(registros, list) else []
        except json.JSONDecodeError:
            return []

def guardar_registro(nuevo_registro):
    os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
    registros = cargar_registros()  # ⬅️ Carga los anteriores
    registros.append(nuevo_registro)  # ⬅️ Añade el nuevo
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=4, ensure_ascii=False)
