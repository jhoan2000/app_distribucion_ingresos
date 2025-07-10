import flet as ft
from services.storage import cargar_registros
from ui.agregar_sueldo import mostrar_modal_ingreso
from utils.helpers import formatear_moneda


def pantalla_principal(page: ft.Page):
    page.title = "Distribución Financiera"
    page.scroll = ft.ScrollMode.AUTO
    registros = cargar_registros()
    lista_registros = ft.Column(spacing=20)

    def mostrar_partidas():
        controles = []
        for registro in registros[::-1]:
            fecha = registro['fecha']
            ingreso = registro['ingreso']
            dist = registro['distribucion']
            ahorros = dist['ahorros']

            controles.append(
                ft.Card(
                    content=ft.Container(
                        bgcolor=ft.colors.BLUE_GREY_50,
                        border_radius=10,
                        padding=15,
                        content=ft.Column([
                            ft.Text(f"📅 Fecha: {fecha}", weight="bold", size=16),
                            ft.Divider(),
                            ft.Text(f"💰 Ingreso: {formatear_moneda(ingreso)}", size=15),
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
        return controles

    def actualizar_lista():
        lista_registros.controls = mostrar_partidas()
        page.update()

    def abrir_modal_agregar(e):
        mostrar_modal_ingreso(page, registros, actualizar_lista)

    # Cabecera con botón de agregar
    page.add(
        ft.Container(
            bgcolor=ft.colors.BLUE_100,
            padding=15,
            border_radius=10,
            content=ft.Row([
                ft.Text("💸 Distribución de Dinero Mensual", size=22, weight="bold", expand=True),
                ft.FilledButton("➕ Agregar ingreso", icon=ft.icons.ADD, on_click=abrir_modal_agregar)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ),
        ft.Divider(),
        lista_registros
    )

    lista_registros.controls = mostrar_partidas()
