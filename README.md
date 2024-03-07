# Melotts and Gemini

## This is a demo showing how [Melotts](https://github.com/myshell-ai/MeloTTS) and Gemini can be used together to create a chatbot that talks to you.
MeloTTS is a high-quality multi-lingual text-to-speech library by MyShell.ai.
You can read more about it [here](https://github.com/myshell-ai/MeloTTS#).

In this demo, I used melotts to convert the response recieved from [Google's Gemini API](https://ai.google.dev/) to convert the response into an audio file and then used playsound to play the file to make it seem as though the LLM is talking to us.

The model of Melotts was installed locally on my machine and was running locally. ([See installation instructions here](https://github.com/myshell-ai/MeloTTS/blob/main/docs/install.md))
Google Gemini was called using the code provided in [gemini_main.py](https://github.com/Kuber144/Melotts-and-Gemini/blob/main/gemini_main.py) file.
It waits for the text to be entered by the user and creates a chat with the LLM model.
As soon as a response is recieved, it calls the [melo_api.py](https://github.com/Kuber144/Melotts-and-Gemini/blob/main/melo_api.py) file and function in it to convert the text to speech.

Melotts is a fast tts model and has several configuration options and the user can choose them and modify the code as needed. (As this is only a demonstration more information about the options can be found [here](https://github.com/myshell-ai/MeloTTS/blob/main/docs/install.md#:~:text=melo%20%2D%2Dhelp-,Python%20API,-English%20with%20Multiple))

### A video showing how the model is running

https://github.com/Kuber144/Melotts-and-Gemini/assets/96476340/5bf99c26-ed33-4448-9b7d-9c436aa41e29



#### This demo can be taken further by using the nodejs implimentation of Gemini to further improve the functionality.
