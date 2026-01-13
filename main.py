
from fasthtml.common import serve, Div, Span

from monsterui.all import (
    H1, H2, Card, Button, Form, Input,
    Container, ContainerT, Theme, fast_app
)

app, rt = fast_app(hdrs=Theme.blue.headers())
counter = 0

@rt
def index():
    return Container(
        H1(
            '🚀 counter app',
            cls='text-3xl font-weight-bold text-center mb-6 mt-6'
        ),

        Card(cls='p-6 text-center mb-4')(
            H2('click the buttons!', cls='mb-4'),
            Div(cls='flex items-center justify-center gap-4')(
                Button('-', hx_post='/dec', hx_target='#count'),
                Span(id='count', cls='text-2xl font-bold')(str(counter)),
                Button('+', hx_post='/inc', hx_target='#count'),
            ),
        ),

        Card(cls='p-6')(
            Form(hx_post='/hello', hx_target='#result')(
                Input(
                    name='name',
                    placeholder='your name',
                    cls='input mb-2'
                )
            ),
            Div(id='result', cls='text-center mb-4'),
        ),

        cls=ContainerT.sm
    )

@rt('/inc', methods=['POST'])
def inc():
    global counter
    counter += 1
    return str(counter)

@rt('/dec', methods=['POST'])
def dec():
    global counter
    counter -= 1
    return str(counter)

@rt('/hello', methods=['POST'])
def hello(name: str):
    return f'Hello, {name}!'


