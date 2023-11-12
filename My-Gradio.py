import gradio as gr
from distutils.version import StrictVersion


def saludo(nombre):
    return "Hola " + nombre + ", ¿Como estas??? "


demo = gr.Interface(
    fn=saludo,
    inputs = gr.components.Textbox(lines=10, placeholder="Dime tu nombre porfa"),
    outputs = "text"
)

demo.launch(share=True`)

