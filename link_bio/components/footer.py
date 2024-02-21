import reflex as rx
# importar datetime para utilizar la fecha del sistema
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        # utilizar texto formateado f'2022 - {} '
        rx.link(f'2022 - { datetime.date.today().year } By NK |', href='https://bmweb.com.mx'),
        rx.text('Nakajito Kurosaki'),
    )