# Se importa reflex
import reflex as rx


from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links

# Se crea la clase state 
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )


# se crea una variable para la aplicación
app = rx.App()
# se asigna la página a la variable app
app.add_page(index)