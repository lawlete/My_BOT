import openai
from config import API_KEY

openai.api_key = API_KEY # cargamos la API_KEY

def generar_respuesta(pregunta):
  respuesta = openai.completions.create( ## creamos una instancia de Consulta de Competion
        model="text-davinci-003", # modelo a usar "gpt-3.5-turbo-instruct" "text-davinci-003"
        prompt=pregunta, # consulta o prompt
        max_tokens=160 # cantidad maxima de tokens
    )
  return respuesta.choices[0].text.strip()


def main():
    print("Bievenido al Chat...")
    
    while True:
      pregunta = input("Escribe tu pregunta o escribe \"salir\" para finalizar : ")
      
      if pregunta.lower() == "salir":
          print("Hasta Luego")
          break
      respuesta = generar_respuesta(pregunta)
      
      print("Respuesta: ", respuesta)
      
if __name__ == "__main__":
    main()  
        