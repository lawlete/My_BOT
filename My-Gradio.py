import gradio as gr
from distutils.version import StrictVersion
import openai
from config import API_KEY_OPENAI_1

openai.api_key = API_KEY_OPENAI_1 # cargamos la API_KEY


def raices(ecuacion):
    respuesta = openai.completions.create( ## creamos una instancia de Consulta de Competion
            model="text-davinci-003", # modelo a usar "gpt-3.5-turbo-instruct" "text-davinci-003"
            prompt="Calcular las raices de la ecuacion: " + ecuacion # consulta o prompt
            max_tokens=256 # cantidad maxima de tokens
        )
    return respuesta.choices[0].text.strip()
   


def ChatGPT(ecuacion):
    return "La ecuacion " + ecuacion 
            + "tiene las siguientes raices" 
            + raices(ecuacion)


demo = gr.Interface(
    fn=chatGPT,
    inputs = gr.components.Textbox(lines=10, 
                                   placeholder="Escribe la ecuacion para cacular las raices "),
    outputs = "text"
)

demo.launch(share=True)

