import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.box(
        rx.vstack(
            link_button(
                'Github',
                'Proyectos en Github',
                'https://github.com/nakajito'),

            link_button(
                'Portfolio',
                'Página web',
                'https://bmweb.com.mx'),
            width = '100%'
        )   
    )

