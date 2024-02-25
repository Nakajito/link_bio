# Se importa reflex
import reflex as rx


from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles


# Se crea la clase state 
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=styles.Size.DEFAULT.value
            ),
        ),
        rx.center(
            footer(),
        ),
    )


# se crea una variable para la aplicación
app = rx.App(
    # se cargan los estylos generales crados en styles.py
    style=styles.BASE_STYLE
)
# se asigna la página a la variable app
app.add_page(index)