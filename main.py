import os
import flet as ft
from ui.home import pantalla_principal
from ui.calendario import pantalla_calendario
from utils.helpers import formatear_moneda

# Aplicar formato a nivel de módulos
import ui.home
import ui.calendario
ui.home.formatear_moneda = formatear_moneda
ui.calendario.formatear_moneda = formatear_moneda

def main(page: ft.Page):
    page.title = "Distribución de Dinero"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.dialog = None

    def cambiar_pagina(index):
        page.controls.clear()
        page.controls.append(navegacion_inferior)
        if index == 0:
            pantalla_principal(page)
        elif index == 1:
            pantalla_calendario(page)
        page.update()

    # Barra inferior de navegación
    navegacion_inferior = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Por Fecha"),
        ],
        selected_index=0,
        on_change=lambda e: cambiar_pagina(e.control.selected_index),
    )
    
    page.controls.append(navegacion_inferior)
    pantalla_principal(page)

#ft.app(target=main)
#ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 5000)))


