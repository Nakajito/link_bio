import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button('Github', 'https://github.com/nakajito'),
        link_button('Portfolio', 'https://bmweb.com.mx'),
    )

