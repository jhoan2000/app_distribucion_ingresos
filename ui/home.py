import flet as ft
from services.storage import cargar_registros
from ui.agregar_sueldo import mostrar_modal_ingreso
from utils.helpers import formatear_moneda

def pantalla_principal(page: ft.Page):
    page.title = "Distribución Financiera"
    page.scroll = ft.ScrollMode.AUTO
    registros = cargar_registros()
    lista_registros = ft.Column()

    def mostrar_partidas():
        controles = []
        for registro in registros[::-1]:
            fecha = registro['fecha']
            ingreso = registro['ingreso']
            dist = registro['distribucion']
            ahorros = dist['ahorros']

            controles.append(
                ft.Card(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"Fecha: {fecha}", weight="bold"),
                            ft.Text(f"Ingreso: {formatear_moneda(ingreso)}"),
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
        return controles

    def actualizar_lista():
        lista_registros.controls = mostrar_partidas()
        page.update()

    def abrir_modal_agregar(e):
        mostrar_modal_ingreso(page, registros, actualizar_lista)

    lista_registros.controls = mostrar_partidas()

    page.add(
        ft.Row([
            ft.Text("Distribución de Dinero Mensual", size=24, weight="bold"),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        lista_registros,
        ft.Container(ft.IconButton(icon=ft.icons.ADD, tooltip="Agregar ingreso", on_click=abrir_modal_agregar))

    )
