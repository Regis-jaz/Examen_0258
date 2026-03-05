import flet as ft

def main(page: ft.Page):
    page.title = "registro de participantes"

    txt_nombre = ft.TextField(label="nombre completo", width=400)
    txt_correo = ft.TextField(label="correo electrónico", width=400)

    dropdown_taller = ft.Dropdown(
        label="taller de interes",
        width=300,
        options=[
            ft.dropdown.Option("pyton para principiantes"),
            ft.dropdown.Option("flet intermedio"),
            ft.dropdown.Option("analisis de datos con pandas"),
        ]
    )

    radio_pago = ft.RadioGroup(
        value="completo",
        content=ft.Row([
            ft.Radio(value="completo", label="pago completo"),
            ft.Radio(value="cuotas", label="pago por cuotas"),
        ])
    )

    check_portatil = ft.Checkbox(label="requiere computadora portatil")

    slider_nivel = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        label="nivel: {value}",
        value=1
    )

    txt_resumen = ft.Text(
        value="",
        size=16,
        color=ft.Colors.BLUE_900
    )

    def mostrar_resumen(e):
        nombre = txt_nombre.value
        correo = txt_correo.value
        taller = dropdown_taller.value
        pago = "pago completo" if radio_pago.value == "completo" else "pago por cuotas"
        portatil = "si" if check_portatil.value else "no"
        nivel = int(slider_nivel.value)

        resumen = f"""

Nombre: {nombre}

Email: {correo}

Taller: {taller}

Pago: {pago}

Requiere Portátil: {portatil}

Nivel de Experiencia: {nivel}

"""

        txt_resumen.value = resumen
        page.update()

    btn_resumen = ft.ElevatedButton(
        content=ft.Text("mostrar ficha del participante"),
        bgcolor=ft.Colors.GREEN_400,
        color=ft.Colors.WHITE,
        on_click=mostrar_resumen
    )

    page.add(
        ft.Text("registro de participantes", size=30, weight="bold"),
        txt_nombre,
        txt_correo,
        dropdown_taller,
        ft.Text("modalidad de pago:"),
        radio_pago,
        check_portatil,
        ft.Text("nivel de experiencia:"),
        slider_nivel,
        btn_resumen,
        ft.Divider(),
        txt_resumen
    )

ft.app(target=main)
