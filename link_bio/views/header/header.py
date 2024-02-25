import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size 

def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                src='favicon.ico',
                fallback='NK',
                size='8',
                margin_x=Size.MEDIUM.value
            ),
            rx.vstack(
                rx.heading(
                    'Nakajito Kurosaki',
                    as_= 'h2'
                ),
                rx.text(
                    '@nakajito'
                ),

                rx.hstack(
                    link_icon('https://facebook.com'),
                    link_icon('https://facebook.com'),
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon(tag='download'),
                            rx.text('CV')
                        ),
                        
                    ),
                    href='#'
                ),
            ),
            margin_y=Size.MEDIUM.value
        ),
        rx.flex(
            info_text('+ 1', 'años de experiencia en python'),
            rx.spacer(),
            info_text('+ 99', 'tazas de café'),
            rx.spacer(),
            info_text('+ 5', 'proyectos concluidos'),
            width='100%',
            margin_y=Size.MEDIUM.value
        ),
        rx.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vel ligula vel justo mattis ultrices nec quis felis. Cras condimentum felis vel ullamcorper vehicula. Sed sed diam non lectus faucibus gravida. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean ornare velit efficitur posuere accumsan. Praesent tincidunt porta felis, eget varius dolor pretium et. Vestibulum nec ipsum non sapien bibendum venenatis a vitae eros. Proin mauris erat, mollis a mollis in, vulputate congue lorem. Donec pellentesque nulla non lorem sollicitudin, at bibendum orci bibendum. Quisque dictum scelerisque magna eget varius. Nunc nec ornare erat.')
    )