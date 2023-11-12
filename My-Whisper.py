from openai import openai
from config import API_KEY_OPENAI_1

openai.api_key = API_KEY_OPENAI_1 # cargamos la API_KEY


audio_file= open("Primer-Audio_Corto.mp3", "rb")
transcript = openai.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)