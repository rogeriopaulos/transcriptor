import os

from pydub import AudioSegment

app_dir = os.environ.get("OPENAI_API_KEY")
audio_file = ""

audio = AudioSegment.from_mp3(f"{app_dir}/audio/{audio_file}")

# O código abaixo segmenta o áudio em 3 partes de 10 minutos cada.
# Alterar os valores de início e fim para segmentar o áudio de acordo com a necessidade do caso.
inicio_primeiro = 0 * 60 * 1000  # Início do arquivo
fim_primeiro = 10 * 60 * 1000    # 10 minutos

inicio_segundo = 10 * 60 * 1000  # 10 minutos
fim_segundo = 20 * 60 * 1000     # 20 minutos

inicio_terceiro = 20 * 60 * 1000  # 20 minutos

primeiro_segmento = audio[inicio_primeiro:fim_primeiro]
segundo_segmento = audio[inicio_segundo:fim_segundo]
terceiro_segmento = audio[inicio_terceiro:]  # Até o final

primeiro_segmento.export(f"{app_dir}/audio/parte_1.mp3", format="mp3")
segundo_segmento.export(f"{app_dir}/audio/parte_2.mp3", format="mp3")
terceiro_segmento.export(f"{app_dir}/audio/parte_3.mp3", format="mp3")
