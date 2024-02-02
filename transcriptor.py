from openai import OpenAI
import os

app_dir = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

audios_path = f'{app_dir}/audio/'
audios_file = ["parte_1.mp3", "parte_2.mp3", "parte_3.mp3"]
audios = [f"{audios_path}{audio}" for audio in audios_file]

for audio in audios:
    with open(audio, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text",
            language="pt"
        )

    transcription_path = f'{app_dir}/transcriptions'
    with open(f"{transcription_path}/{audio.split('/')[-1].split('.')[0]}.txt", "w") as transcription_file:
        transcription_file.write(transcript)
