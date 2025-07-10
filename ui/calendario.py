import flet as ft
from services.storage import cargar_registros
from utils.helpers import formatear_moneda

def pantalla_calendario(page: ft.Page):
    page.title = "Historial por Fecha"
    page.scroll = ft.ScrollMode.AUTO

    registros = cargar_registros()
    output = ft.Column()

    def filtrar_por_fecha(e):
        if not date_picker.value:
            return

        fecha = date_picker.value.strftime("%Y-%m-%d")
        encontrados = [r for r in registros if r["fecha"] == fecha]

        output.controls.clear()
        if encontrados:
            for r in encontrados:
                dist = r["distribucion"]
                ahorros = dist["ahorros"]
                output.controls.append(
                    ft.Card(
                        ft.Container(
                            content=ft.Column([
                                ft.Text(f"Fecha: {fecha}", weight="bold"),
                                ft.Text(f"Ingreso: {formatear_moneda(r['ingreso'])}"),
                                ft.Text(f"- Necesidades Básicas: {formatear_moneda(dist['necesidades_basicas'])}"),
                                ft.Text(f"- Gastos Personales: {formatear_moneda(dist['gastos_personales'])}"),
                                ft.Text(f"- Imprevistos: {formatear_moneda(dist['imprevistos'])}"),
                                ft.Text("- Ahorros:"),
                                ft.Text(f"    • Fondo Emergencia: {formatear_moneda(ahorros['fondo_emergencia'])}"),
                                ft.Text(f"    • Inversiones: {formatear_moneda(ahorros['inversiones'])}"),
                                ft.Text(f"    • Viajes y Tecnología: {formatear_moneda(ahorros['viajes_tecnologia'])}"),
                            ]),
                            padding=15
                        )
                    )
                )
        else:
            output.controls.append(ft.Text("No se encontraron registros para esa fecha."))

        page.update()

    date_picker = ft.DatePicker(on_change=filtrar_por_fecha)
    page.overlay.append(date_picker)

    boton_fecha = ft.ElevatedButton("Seleccionar fecha", on_click=lambda _: date_picker.pick_date())

    page.add(
        ft.Column([
            ft.Text("Consultar distribución por fecha", size=20, weight="bold"),
            boton_fecha,
            output
        ])
    )
