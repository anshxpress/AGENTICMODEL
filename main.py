import google.generativeai as genai
import chainlit as cl
import os
import base64
from PIL import Image
import io

# Configure Gemini with API key
genai.configure(api_key="AIzaSyDCe2Dw7a6Eb-WXSS_SPx_5_oeCNepLIyg")

# Initialize Gemini model (text + vision)
model = genai.GenerativeModel("gemini-2.0-flash")

def append_messages(image_url=None, query=None, audio_transcript=None):
    message_list = []

    if image_url:
        # Instead of URLs, Gemini expects image bytes or PIL image
        img_bytes = base64.b64decode(image_url.split(",")[1])
        image = Image.open(io.BytesIO(img_bytes))
        message_list.append(image)

    if query and not audio_transcript:
        message_list.append(query)
    if audio_transcript:
        message_list.append(query + "\n" + audio_transcript)

    # Call Gemini model
    response = model.generate_content(message_list)
    return response

def image2base64(image_path):
    with open(image_path, "rb") as img:
        encoded_string = base64.b64encode(img.read())
    return encoded_string.decode("utf-8")

# Gemini does NOT have Whisper. For audio transcription,
# you’d need to use Google Speech-to-Text API.
def audio_process(audio_path):
    return "Audio transcription via Google Speech-to-Text API needed here."

@cl.on_message
async def main(msg: cl.Message):
    images = [file for file in msg.elements if "image" in file.mime]
    audios = [file for file in msg.elements if "audio" in file.mime]

    if len(images) > 0:
        base64_image = image2base64(images[0].path)
        image_url = f"data:images/png;base64,{base64_image}"
        text = None
    elif len(audios) > 0:
        text = audio_process(audios[0].path)
        image_url = None
    else:
        image_url = None
        text = None

    response_msg = cl.Message(content="")

    if len(images) == 0 and len(audios) == 0:
        response = append_messages(query=msg.content)
    elif len(audios) == 0:
        response = append_messages(image_url=image_url, query=msg.content)
    else:
        response = append_messages(query=msg.content, audio_transcript=text)

    response_msg.content = response.text

    await response_msg.send()
