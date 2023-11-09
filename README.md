# My_BOT
Mi BOT
# Readme

## Descripción del proyecto
Este proyecto consiste en utilizar la API de OpenAI para generar respuestas a partir de preguntas ingresadas por el usuario. 
El código utiliza el modelo "text-davinci-003" de OpenAI para generar las respuestas.

## Configuración
Antes de ejecutar el código, asegúrate de tener una API key válida de OpenAI. Esta clave debe ser proporcionada en el archivo  
`config.py`  en la variable  `API_KEY` .

## Instalación
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala las dependencias necesarias ejecutando el siguiente comando:
pip install openai
## Uso
1. Ejecuta el archivo  `main.py`  para iniciar el chat.
2. Se te pedirá que ingreses una pregunta. Escribe tu pregunta y presiona Enter.
3. El programa generará una respuesta utilizando el modelo de OpenAI y la mostrará en la consola.
4. Puedes continuar haciendo preguntas hasta que decidas salir. Para salir, simplemente escribe "salir" y presiona Enter.

## Notas adicionales
- El código está configurado para utilizar el modelo "text-davinci-003" de OpenAI. Si deseas utilizar otro modelo, puedes modificar la variable  `model`  en la función  `generar_respuesta` .
- El código tiene una restricción de 160 tokens para las respuestas generadas. Si deseas cambiar este límite, puedes modificar el valor de  `max_tokens`  en la función  `generar_respuesta` .

¡Disfruta del chat y las respuestas generadas por OpenAI! Si tienes alguna pregunta o problema, no dudes en contactarme.

