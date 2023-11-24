import gradio as gr
from transformers import pipeline

trans = pipeline("automatic-speech-recognition", 
                 model = "facebook/wav2vec2-large-xlsr-53-spanish")
clasificador = pipeline("text-classification", 
                        model = "pysentimiento/robertuito-sentiment-analysis")


def audio_a_text(audio):
  text = trans(audio)["text"]
  return text

def texto_a_sentimiento(text):
  return clasificador(text)[0]["label"]

demo = gr.Blocks()

with demo:
  gr.Markdown("Demo de uso de Bloques e integracion de Modelos")
  audio = gr.Audio(sources="microphone", type="filepath")

  texto = gr.Textbox()
  b1 = gr.Button("Transcribir")
  b1.click(audio_a_text, inputs=audio, outputs=texto)

  label = gr.Label()
  b2 = gr.Button("Clasificar")
  b2.click(texto_a_sentimiento, inputs=texto, outputs=label)

demo.launch()
