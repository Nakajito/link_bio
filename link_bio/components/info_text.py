import reflex as rx
from link_bio.styles.styles import Size as Size

def info_text(title:str, body:str) -> rx.Component:
    return rx.box( 
        rx.text(
            title,
            font_weight='bold',
            as_='span'
        ),
        rx.text(
            f' {body}',
            as_='span'
        ),
        font_size=Size.MEDIUM.value
    )