import flet as ft
from services.calculadora import calcular_distribucion
from services.storage import guardar_registro
from utils.helpers import obtener_fecha_actual_formateada, formatear_moneda

def mostrar_modal_ingreso(page: ft.Page, registros, on_guardar):

    ingreso_input = ft.TextField(
        label="Ingresa tu sueldo del mes",
        prefix_text="$ ",
        autofocus=True,
        keyboard_type=ft.KeyboardType.NUMBER,
        border="outline",
        width=300
    )

    mensaje_error = ft.Text("", color=ft.colors.RED_600)

    def guardar(e):
        ingreso_texto = ingreso_input.value.strip()
        if not ingreso_texto or not ingreso_texto.isdigit():
            mensaje_error.value = "❗ Por favor ingresa un número válido"
            page.update()
            return

        ingreso = int(ingreso_texto)
        fecha = obtener_fecha_actual_formateada()
        distribucion = calcular_distribucion(ingreso)
        nuevo_registro = {
            "fecha": fecha,
            "ingreso": ingreso,
            "distribucion": distribucion
        }

        registros.append(nuevo_registro)
        guardar_registro(nuevo_registro)
        on_guardar()
        page.dialog.open = False
        page.update()

    def cerrar(e):
        page.dialog.open = False
        page.update()

    modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("➕ Agregar Ingreso", size=20, weight="bold"),
        content=ft.Column([
            ingreso_input,
            mensaje_error
        ], tight=True, spacing=10),
        actions=[
            ft.TextButton("Cancelar", on_click=cerrar),
            ft.ElevatedButton("Guardar", on_click=guardar, icon=ft.icons.SAVE),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.dialog = modal
    modal.open = True
    page.update()
