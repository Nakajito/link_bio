import reflex as rx

def navbar() -> rx.Component:
        return rx.hstack(
        rx.text(
            'Nakajito Kurosaki',
            height='40px'
        ),
        position='sticky',
        bg='green',
        padding_x='16px',
        padding_y='8px',
        z_index='999'
    )