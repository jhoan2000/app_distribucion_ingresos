import flet as ft
from services.storage import cargar_registros
from utils.helpers import formatear_moneda
from datetime import date

def pantalla_calendario(page: ft.Page):
    page.title = "Ver registros por fecha"
    registros = cargar_registros()
    resultado = ft.Column(spacing=15)

    def buscar_por_fecha(e):
        fecha_elegida = date_picker.value
        if not fecha_elegida:
            resultado.controls = [ft.Text("⚠️ Debes seleccionar una fecha.", color=ft.colors.RED)]
            page.update()
            return

        fecha_formateada = fecha_elegida.strftime("%Y-%m-%d")
        registros_en_fecha = [r for r in registros if r["fecha"] == fecha_formateada]

        if not registros_en_fecha:
            resultado.controls = [ft.Text(f"📅 No hay registros para {fecha_formateada}.")]
        else:
            resultado.controls = []
            for r in registros_en_fecha:
                dist = r["distribucion"]
                ahorros = dist["ahorros"]
                resultado.controls.append(
                    ft.Card(
                        content=ft.Container(
                            bgcolor=ft.colors.GREY_50,
                            border_radius=10,
                            padding=15,
                            content=ft.Column([
                                ft.Text(f"💰 Ingreso: {formatear_moneda(r['ingreso'])}", weight="bold", size=15),
                                ft.Text(f"🛒 Necesidades Básicas: {formatear_moneda(dist['necesidades_basicas'])}"),
                                ft.Text(f"👤 Gastos Personales: {formatear_moneda(dist['gastos_personales'])}"),
                                ft.Text(f"⚠️ Imprevistos: {formatear_moneda(dist['imprevistos'])}"),
                                ft.Text("📦 Ahorros:", weight="bold", size=14),
                                ft.Text(f"  🆘 Fondo Emergencia: {formatear_moneda(ahorros['fondo_emergencia'])}"),
                                ft.Text(f"  📈 Inversiones: {formatear_moneda(ahorros['inversiones'])}"),
                                ft.Text(f"  ✈️ Viajes y Tecnología: {formatear_moneda(ahorros['viajes_tecnologia'])}"),
                            ])
                        )
                    )
                )
        page.update()

    date_picker = ft.DatePicker(
    on_change=buscar_por_fecha,
    first_date=date(2023, 1, 1),
    last_date=date(2030, 12, 31)
    )

    page.overlay.append(date_picker)

    page.add(
        ft.Column([
            ft.Text("📅 Selecciona una fecha para ver registros", size=20, weight="bold"),
            ft.FilledButton("Elegir fecha", icon=ft.icons.CALENDAR_MONTH, on_click=lambda e: date_picker.pick_date()),
            resultado
        ], spacing=20)
    )
