import flet as ft
from ui.home import pantalla_principal
from ui.calendario import pantalla_calendario
from utils.helpers import formatear_moneda, obtener_fecha_actual_formateada

# Aplicar formatear_moneda en todas las vistas
import ui.home
import ui.calendario

ui.home.formatear_moneda = formatear_moneda
ui.calendario.formatear_moneda = formatear_moneda

def main(page: ft.Page):
    def ir_a_home(e):
        page.clean()
        page.add(botones_navegacion)
        pantalla_principal(page)

    def ir_a_calendario(e):
        page.clean()
        page.add(botones_navegacion)
        pantalla_calendario(page)

    botones_navegacion = ft.Row([
        ft.ElevatedButton("🏠 Inicio", on_click=ir_a_home),
        ft.ElevatedButton("📅 Ver por fecha", on_click=ir_a_calendario),
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(botones_navegacion)
    pantalla_principal(page)

ft.app(target=main, view=ft.WEB_BROWSER)
