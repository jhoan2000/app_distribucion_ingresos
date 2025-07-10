import json
import os

RUTA_ARCHIVO = "data/registros.json"

def guardar_registro(registros):
    os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=4, ensure_ascii=False)

def cargar_registros():
    if not os.path.exists("data/registros.json"):
        return []

    with open("data/registros.json", "r") as f:
        try:
            registros = json.load(f)
            return registros if isinstance(registros, list) else []
        except json.JSONDecodeError:
            return []
