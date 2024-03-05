import pathlib
import textwrap
from melo_api import generate_tts
import google.generativeai as genai

GOOGLE_API_KEY=#YOUR API KEY OVER HERE

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
chat

while True:
  req=input()
  response=chat.send_message(req)
  generate_tts(response.text)
# In case there is some error or the loop exits then print chat history to see what was the last message
print(chat.history)