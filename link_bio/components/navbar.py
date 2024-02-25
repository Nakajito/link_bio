import reflex as rx
import link_bio.styles.styles as styles


def navbar() -> rx.Component:
        return rx.hstack(
        rx.text(
            'Nakajito Kurosaki',
        ),
        position='sticky',
        bg='grey',
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.MEDIUM.value,
        z_index='999',
        margin_bottom='2em',
        top = '0'
    )