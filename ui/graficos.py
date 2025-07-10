import flet as ft

def mostrar_graficos(page, registro):
    dist = registro['distribucion']
    ahorros = dist['ahorros']

    total_general = (
        dist['necesidades_basicas'] +
        dist['gastos_personales'] +
        dist['imprevistos'] +
        sum(ahorros.values())
    )

    def calc_pct(valor):
        return round((valor / total_general) * 100)

    # Gráfico general con % y valor
    grafico_general = ft.PieChart(sections=[
        ft.PieChartSection(
            value=dist['necesidades_basicas'],
            title=f"{calc_pct(dist['necesidades_basicas'])}%\n${dist['necesidades_basicas']:,.0f}",
            color=ft.colors.BLUE
        ),
        ft.PieChartSection(
            value=dist['gastos_personales'],
            title=f"{calc_pct(dist['gastos_personales'])}%\n${dist['gastos_personales']:,.0f}",
            color=ft.colors.GREEN
        ),
        ft.PieChartSection(
            value=dist['imprevistos'],
            title=f"{calc_pct(dist['imprevistos'])}%\n${dist['imprevistos']:,.0f}",
            color=ft.colors.RED
        ),
        ft.PieChartSection(
            value=sum(ahorros.values()),
            title=f"{calc_pct(sum(ahorros.values()))}%\n${sum(ahorros.values()):,.0f}",
            color=ft.colors.ORANGE
        ),
    ])

    total_ahorro = sum(ahorros.values())

    def pct_ahorro(v):
        return round((v / total_ahorro) * 100) if total_ahorro > 0 else 0

    # Gráfico de ahorro
    grafico_ahorro = ft.PieChart(sections=[
        ft.PieChartSection(
            value=ahorros['fondo_emergencia'],
            title=f"{pct_ahorro(ahorros['fondo_emergencia'])}%\n${ahorros['fondo_emergencia']:,.0f}",
            color=ft.colors.CYAN
        ),
        ft.PieChartSection(
            value=ahorros['inversiones'],
            title=f"{pct_ahorro(ahorros['inversiones'])}%\n${ahorros['inversiones']:,.0f}",
            color=ft.colors.INDIGO
        ),
        ft.PieChartSection(
            value=ahorros['viajes_tecnologia'],
            title=f"{pct_ahorro(ahorros['viajes_tecnologia'])}%\n${ahorros['viajes_tecnologia']:,.0f}",
            color=ft.colors.PURPLE
        ),
    ])

    dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text(f"Distribución del {registro['fecha']}", weight="bold"),
        content=ft.Column([
            ft.Text("📊 Distribución General", size=16, weight="bold"),
            grafico_general,
            ft.Divider(),
            ft.Text("📦 Detalle de Ahorros", size=16, weight="bold"),
            grafico_ahorro
        ], tight=True, scroll=ft.ScrollMode.ADAPTIVE),
        actions=[ft.TextButton("Cerrar", on_click=lambda e: cerrar_modal(page))],
    )
    page.dialog = dialogo
    dialogo.open = True
    page.update()

def cerrar_modal(page):
    page.dialog.open = False
    page.update()