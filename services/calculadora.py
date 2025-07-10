def calcular_distribucion(ingreso):
    necesidades_basicas = ingreso * 0.30
    gastos_personales = ingreso * 0.20
    imprevistos = ingreso * 0.10
    ahorros = ingreso * 0.40

    fondo_emergencia = ahorros * 0.30
    inversiones = ahorros * 0.45
    viajes_tecnologia = ahorros * 0.25

    return {
        "necesidades_basicas": round(necesidades_basicas),
        "gastos_personales": round(gastos_personales),
        "imprevistos": round(imprevistos),
        "ahorros": {
            "fondo_emergencia": round(fondo_emergencia),
            "inversiones": round(inversiones),
            "viajes_tecnologia": round(viajes_tecnologia)
        }
    }
