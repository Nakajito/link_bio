import reflex as rx
import link_bio.styles.styles as styles
def link_button(titulo:str, body:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag='arrow-up-right-square'
                ),
                rx.vstack(
                    rx.text(titulo, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                ),
            ),
            width = '100%'
        ),
        href=url,
        is_external=True,
        width='100%'
    )

