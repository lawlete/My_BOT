import gradio as gr
from distutils.version import StrictVersion
import openai
from config import API_KEY_OPENAI_1

openai.api_key = API_KEY_OPENAI_1 # cargamos la API_KEY

def raices(ecuacion):
    mensaje= "Para la ecuacion: " 
    mensaje= mensaje + str(ecuacion)
    mensaje= mensaje + ", calcular las raices, la derivada, la integral "
    mensaje= mensaje + "y el limite cuando x tiende a 0 y a infinito"
    
    #print(mensaje)
    #print(" la Ecuacion es: ", str(ecuacion))
    respuesta = openai.completions.create( ## creamos una instancia de Consulta de Competion
            model="text-davinci-003", # modelo a usar "gpt-3.5-turbo-instruct" "text-davinci-003"
            prompt= mensaje, # consulta o prompt
            max_tokens=256, # cantidad maxima de tokens
            temperature=0.1
        )
    return respuesta.choices[0].text.strip()
   


#def chatGPT(ecuacion):
#    return raices(ecuacion)


demo = gr.Interface(
    fn=raices,
    inputs = gr.components.Textbox(
                lines=1,
                max_lines=3, 
                placeholder=""" 
                "Escribe la ecuacion para calcular
                las raices, la derivada, la integral,
                los limites de x cuando tiende a 0,
                y cuando x tiende a oo" 
                """),
    outputs=gr.outputs.Markdown()
)

demo.launch(share=True)

