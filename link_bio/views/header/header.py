import reflex as rx

def header() -> rx.Component:
    return rx.flex(
        rx.avatar(
            src='favicon.ico',
            fallback='NK',
            size='9',
            radius='full'
        ),
        rx.text(
            'Nakajito Kurosaki',
            weight='bold',
            size='4'
        ),
        rx.text(
            '@Nakajito', 
            color_scheme='gray'
        ),
        rx.button(
            'CV',
            color_scheme='indigo',
            variant='soft'

        ),
        direction='column',
        spacing='1'
    )