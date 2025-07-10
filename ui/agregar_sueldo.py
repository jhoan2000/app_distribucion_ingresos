import flet as ft
from datetime import datetime
from services.calculadora import calcular_distribucion
from services.storage import guardar_registro

def mostrar_modal_ingreso(page: ft.Page, registros: list, actualizar_vista_callback):
    ingreso_field = ft.TextField(label="Ingrese su saldo del mes", keyboard_type=ft.KeyboardType.NUMBER)

    def guardar_ingreso(e):
        try:
            monto = int(ingreso_field.value)
            fecha = datetime.now().strftime("%Y-%m-%d")
            dist = calcular_distribucion(monto)
            registro = {"fecha": fecha, "ingreso": monto, "distribucion": dist}
            registros.append(registro)
            guardar_registro(registros)
            dlg_ingreso.open = False
            actualizar_vista_callback()
            page.update()
        except ValueError:
            ingreso_field.error_text = "Ingrese un valor válido"
            page.update()

    def cerrar_modal(e=None):
        dlg_ingreso.open = False
        page.update()

    dlg_ingreso = ft.AlertDialog(
        title=ft.Text("Nuevo ingreso mensual"),
        content=ingreso_field,
        actions=[
            ft.TextButton("Cancelar", on_click=cerrar_modal),
            ft.TextButton("Guardar", on_click=guardar_ingreso),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    ingreso_field.value = ""
    page.dialog = dlg_ingreso
    dlg_ingreso.open = True
    page.update()
